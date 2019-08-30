import config
import etl
import sqlite3

'''Setup sqlite db with schema'''
def schema_setup(db_file, schema_file):
	conn = sqlite3.connect(db_file)
	with open(schema_file, 'r') as f:
		schema = f.read()
	conn.executescript(schema)
	print('sqlite db setup with schema')

if __name__ == '__main__':
	schema_setup(config.files['db_filename'], config.files['schema_filename'])
	artist_loader = etl.Transformer(config.urls['artists'], config.files['db_filename'])
	artist_loader.load_artists()
	playlist_loader = etl.Transformer(config.urls['playlist'], config.files['db_filename'])
	playlist_loader.load_playlist()