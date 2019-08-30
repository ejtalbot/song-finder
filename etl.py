import config
import requests
import sqlite3

'''ETL functionality used in db setup '''

'''Class to handle url input and create iterator over file lines'''
class Extractor():
	def __init__(self, url):
		self.url = url

	def parse_url(self):
		try:
			resp = requests.get(self.url)
			data_iterator = resp.iter_lines(decode_unicode=True)
			return data_iterator
		except:
			raise Exception(f'unable to parse {self.url}')

'''Class to insert data into db'''
class Transformer():
	def __init__(self, source, db):
		extractor = Extractor(source)
		self.data_source = extractor.parse_url()
		self.conn = sqlite3.connect(db)
		self.cur = self.conn.cursor()

	#insert a new artist
	def load_artists(self):
		for line in self.data_source:
			artist_line = line.split('<SEP>')
			artist_id = artist_line[0]
			artist_name = artist_line[-1].strip()
			try:
				sql_str = 'insert into artists (id, name) values (:artist_id, :artist_name)'
				self.cur.execute(sql_str, {'artist_id': artist_id, 'artist_name': artist_name})
			except:
				print(f'Error loading artist id:{artist_id} name:{artist_name}')
		self.conn.commit()
		print('loaded artist file')

	#insert songs and tracks
	def load_playlist(self):
		for line in self.data_source:
			#skip comment lines
			if line[0] == '#':
				pass
			#insert new song
			elif line[0] == '%':
				song_line = line.split(',')
				song_title = song_line[-1].strip()
				#try:
				sql_str = 'insert into songs (id, title) values (:song_id, :song_title)'
				self.cur.execute(sql_str, {'song_id': None,'song_title': song_title})
				#keep track of song row to reference in individual track insertion
				song_row = self.cur.lastrowid
				#except:
				#	print(f'Error loading song:{song_title}')
			#insert track entry
			else:
				track_line = line.split('<SEP>')
				track_id = track_line[0]
				artist_id = track_line[1]
				try:
					sql_str = 'insert into tracks (id, artist_id, song_id) values (:track_id, :artist_id, :song_row)'
					self.cur.execute(sql_str, {'track_id': track_id, 'artist_id': artist_id, 'song_row': song_row})
				except:
					pass
					#print(f'Error loading track for artist id:{artist_id} song:{song_title}')
		self.conn.commit()
		print('loaded playlist file')