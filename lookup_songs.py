import argparse
import config
import sqlite3

'''CLI tool to create argparser to lookup songs by artist passed as the argument'''
class SongFinder():
	def __init__(self, db):
		self.conn = sqlite3.connect(db)
		self.cur = self.conn.cursor()
		self.parser = argparse.ArgumentParser(description='Lookup songs played by an artist')
		self.parser.add_argument('Artist', metavar='artist', type=str, help='Enter an artist name. Enclose name in quotes if there are spaces.')
		self.args = self.parser.parse_args()

	def songs_by_artist(self):
		sql_str ='''
			select songs.title from songs
			left join tracks on songs.id=tracks.song_id
			left join artists on artists.id=tracks.artist_id
			where lower(artists.name)=lower(:artist_name)
			'''
		self.cur.execute(sql_str, {'artist_name': self.args.Artist})
		song_list = self.cur.fetchall()
		#outputs
		if len(song_list) == 0:
			print(f'No song results for {self.args.Artist}')
		else:
			[print(song[0]) for song in song_list]

if __name__ == '__main__':
	SongFinder(config.files['db_filename']).songs_by_artist()