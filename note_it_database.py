import sqlite3
import json
import collections  

class NoteItDb():
	"""Class that creates table and handles database queries"""
	def __init__(self): # Initializes the class 
		"""Creates note_it.db then connects to it """ 
		self.conn = sqlite3.connect('C:/Users/Ruth/clones/bc-9-note-it/bc-9-note-it/note_it.db')
		self.c = self.conn.cursor()

	def create_table(self):
		"""Creates the table that notes will be stored in """
		self.c.execute("CREATE TABLE if not exists note_it_data \
				(id_column INTEGER PRIMARY KEY AUTOINCREMENT, \
				title_column CHAR(50), \
				body_column TEXT)" \
				)
		self.conn.commit() # Commits the changes
	
	def save_note(self, title, note_content):
		"""Saves the note_content that has been entered to the database """
		with self.conn:
			self.c.execute("INSERT INTO note_it_data(title_column, body_column) \
				VALUES ('{}', '{}')".format(title, note_content))
			# {} is a place holder for note_content

	def view(self, note_id):
		"""Allows you to view a note with a particular note_id """ 
		with self.conn:
			for item in self.c.execute("SELECT * FROM note_it_data WHERE \
				id_column == '{}'".format(note_id)):
				return item

	def search(self, query_string, limit):
		"""Retrieves a list of all the notes with a particuler query string, where
			the limit specifies the maximum number of notes that can be listed  
		"""  
		with self.conn:
			self.c.execute("SELECT * FROM note_it_data WHERE body_column LIKE \
				'%{}%' LIMIT '{}'".format(query_string, int(limit)))
			for item in self.c.fetchall():
				print item # Return only returns one item
	
	def search_next(self, query_string, start, step):
		""""Invokes the next set of data in the running query """
		with self.conn:
			self.c.execute("SELECT * FROM note_it_data WHERE body_column LIKE '%{}%' \
				LIMIT '{}', '{}'".format(query_string, int(start), int(step))) 
			for item in self.c.fetchall():
				print item
				
	def list(self, limit):
		"""Retrieves a list of all the notes takenwhere the limit specifies the 
			maximum number of notes that can be listed
		""" 
		with self.conn:
			self.c.execute("SELECT * FROM note_it_data LIMIT'{}'".format(limit))
			for item in self.c.fetchall():
				print item 

	def list_next(self, start_point, step_size):
	 	"""Invokes the next set of data in the running query"""
	 	self.c.execute("SELECT * FROM note_it_data LIMIT '{}' \
	 		'{}'".format(start_point, step_size))
	 		# step_size specifes by how the next item to be shown increases   

	def delete(self, note_id):
		"""Deletes a note with a particular note_id from database """ 
		with self.conn:
			self.c.execute("DELETE FROM note_it_data WHERE \
				id_column == '{}'".format(note_id))

	def exp(self):
		"""Exports entire database content to a JSON file, and saves it using  
			a JSON format 
		"""
		json_exports = []
		rows = self.c.execute("SELECT * from note_it_data")
		for item in rows: 
			d_= collections.OrderedDict()
			d_['id_column'] = rows[0]
			d_['title_column'] = rows[1] 
			d_['body_column'] = rows[2]
			json_exports.append(d_)
			# Appends all the dictionaries of items in 'rows' to list json_export   
		
		a = json.dumps(json_exports)
		# Converts list 'json_exports' to JSON
		json_file = str(filename)
		# json_file == file to be made from json_exports
		b = open(json_file, 'w')
		print b, a

	def imp(self):
		"""Imports JSON file such that, you can populate database through \
			the respective file
		"""
		json_file = "JSON_import.json."
		_load =  json.load(open(json_file))
		for item in _load:
			with self.conn:
				self.c.execute("INSERT INTO note_it_data (title_column, \
					body_column) VALUES '{}', '{}'".format(title_column, body_column))

	def sync():
		"""Syncs notes with Firebase """
		pass

# self.conn.close() # Closes connection to database file 
