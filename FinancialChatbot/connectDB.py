import sqlite3

def connectDB():
	conn = sqlite3.connect('finsheets.db')
	cr = conn.cursor()
	cr.execute('''
		create table if not exists FINSHEETS
		(
		[id] integer primary key,
		[name] text,
		[profit] text
		)	
		''')
	conn.commit()
