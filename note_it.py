'''This program is a Note taking application, known as 'Note It'.
	The available commands are specified under Usage below.

	Usage: 
		note_it create <note_content> 
		note_it view <note_id>
		note_it delete <note_id>
		note_it list (--limit)
		note_it search <query_string> (--limit)
		note_it import <note_id>
		note_it export <note_id>
		note_it sync
		note_it -h | --help
		note_it --version
		
	Options:
		-h, --help  shows this help message and exits
		--limit		sets the number of items to display in resulting list  
'''

from docopt import docopt
from cmd import Cmd

class NoteIt(Cmd):
	def create_note(note_content):
		pass

# if __name__ == '__main__':


 

