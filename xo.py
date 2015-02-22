
### Tictactoe allows the user to play a two player game of tictactoe on the command line. Moves are entered using
#   grid coordinates which are displayed (a1, b2, etc). A tie triggers a new game, and "q" for any move quits.
#   future improvements may include a one player version against a computer, possible with varying difficulty levels
#   i.e. always blocking an impending 3 in a row, or, even stronger, the computer plays perfectly.
#   What is the simplest algorithm allowing perfect computer play?


class Tictactoe(object):

	from sys import exit
	
	def new_game(self, move_counter):
		
		if move_counter is 0 or 9:
		
			board = {(0,0):" ", (0,1):" ", (0,2):" ",
					 (1,0):" ", (1,1):" ", (1,2):" ", 
					 (2,0):" ", (2,1):" ", (2,2):" "}
				 
			print "\nGet ready to play!\n"
			print "X's go first\n"
				 
			return board
		
		else:
			pass
		
	def winning_conditions(self, board, x_or_o):

		row1=row2=row3=col1=col2=col3=diag1=diag2 = True
	
		for i in range(3):
			row1 = row1 and board[(i,0)] is x_or_o
			row2 = row2 and board[(i,1)] is x_or_o
			row3 = row3 and board[(i,2)] is x_or_o
			col1 = col1 and board[(0,i)] is x_or_o
			col2 = col2 and board[(1,i)] is x_or_o
			col3 = col3 and board[(2,i)] is x_or_o
			diag1 = diag1 and board[(i,i)] is x_or_o
			diag2 = diag2 and board[(i, 2-i)] is x_or_o

		return (row1 or row2 or row3 or col1 or 
				col2 or col3 or diag1 or diag2)

	def print_board(self, board):
		
		print "\n\nc  ", board[(2,0)], " | ", board[(2,1)], " | ", board[(2,2)]
		print "   _______________"
		print "b  ", board[(1,0)], " | ", board[(1,1)], " | ", board[(1, 2)]
		print "   _______________"
		print "a  ", board[(0,0)], " | ", board[(0,1)], " | ", board[(0,2)], "\n"
		print "    ", 1, "  ", 2, "  ", 3, "\n"
		
	def quit_game(self, input):
		if "q" in input:
			exit(1)
			
	def play(self):
	
		a1_to_00 = {'a1':(0,0), 'a2':(0,1), 'a3':(0,2),
					'b1':(1,0), 'b2':(1,1), 'b3':(1,2), 
					'c1':(2,0), 'c2':(2,1), 'c3':(2,2)}

		xo_notation = { True:'X', False:'O'}

		game_won = False

		move_counter = 0
	
		X_turn = True
		ttt = Tictactoe()
		board = ttt.new_game(move_counter)
		ttt.print_board(board)
	
		while game_won == False:
	
			if move_counter is 9:
		
				print "Its a tie"
			
				board = ttt.new_game(move_counter)	
			
				X_turn = true
			
			else:
		
				x_or_o = xo_notation[X_turn]
				
				y = raw_input("> ")
				
				ttt.quit_game(y)
				
				try:
	
					print "It's your move %s's!\n" % x_or_o
		
					x = a1_to_00[y]
					
					if board[x] == " ": 
			
						board[x] = x_or_o
						X_turn = not X_turn
						move_counter += 1
			
					else: print "I'm sorry that square is occupied, play again\n"

				except:
	
					print ("Sorry that is not a valid move. Try something like a1 or b2")
					
			ttt.print_board(board)
			
			game_won = ttt.winning_conditions(board, xo_notation[not X_turn])
		#writ Feb 02 15
		print "\n3 in a row!"
		print "%s is the winner! " % xo_notation[not X_turn]
		
x = Tictactoe()
x.play()




	
			   
	
		   

		   

			
