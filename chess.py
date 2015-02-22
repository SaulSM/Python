class Pieces(object):
	board = {}
	for x in range(1,65):
		board[x] = 0
	
	white_first_row  = ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
	
	white_second_row = ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp']
	
	black_first_row  = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR']
	
	black_second_row = ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp']
	
		
		
class White(Pieces): #give each piece an 'available' method that represents available squares.
	b = Pieces.board
	for i in range(1,9):
		b[i] = Pieces.first_row[i-1]
		b[i + 8] = Pieces.second_row[i-1]
		
	white_start = b
	
class Black(Pieces):
	b = Pieces.board
	for i in range(1,9):
		b[i + 56] = first_row[i-1]
		b[i + 48] = second_row[i-1]
		
	black_start = b

class Engine(object):
	
	def __init__(self, White, Black):
		self.board = board
		
pieces = Pieces()
print pieces.b
#tim = White()
#tyrese = Black()
#play = Engine(tim, tyrese)