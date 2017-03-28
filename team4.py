import random
import copy

class Manual_Player:
	#b=Board()
	def __init__(self):
		pass


	def move(self, board, old_move, flag):
		#print 'Enter your move: <format:row column> (you\'re playing with', flag + ")"
		#print board.block_status
		#cells = board.find_valid_move_cells(old_move)
		#mvp = raw_input()
		#mvp = mvp.split()
		f1=0
		bestval=-1000
		row=-1
		col=-1
		alpha=-100000
		beta=1000000
		#return (int(mvp[0]), int(mvp[1]))
		allowed_block = [old_move[0]%4, old_move[1]%4]
		if old_move != (-1,-1) and board.block_status[allowed_block[0]][allowed_block[1]] == '-':
			for i in range(4*allowed_block[0], 4*allowed_block[0]+4):
				for j in range(4*allowed_block[1], 4*allowed_block[1]+4):
					if board.board_status[i][j] == '-':
						#allowed_cells.append((i,j))
						board.board_status[i][j]='o'
						new=(i,j)
						old_move=new
						Maxvalue= self.minimax(board,old_move,0,1,alpha,beta)
						board.board_status[i][j]='-'
						if Maxvalue>bestval:
							row=i
							col=j
						#if int(mvp[0])==i and int(mvp[1])==j:
						#	f1=1
		else:
			for i in range(16):
				for j in range(16):
					if board.board_status[i][j] == '-' and board.block_status[i/4][j/4] == '-':
						#allowed_cells.append((i,j))
						#if int(mvp[0])==i and int(mvp[1])==j:
						board.board_status[i][j]='o'
						new=(i,j)
						old_move=new
						Maxvalue= self.minimax(board,old_move,0,0,alpha,beta)
						board.board_status[i][j]='-'
						if Maxvalue>bestval:
							row=i
							col=j
						#	f1=1
	        #if f1==1:
		return (int(row), int(col))

	def minimax(self,board,old_move,depth,flag,alpha,beta):
		score=self.evaluate(board,old_move)
		if score==100:
			return score
		if score==-100:
			return score
		allowed_block = [old_move[0]%4, old_move[1]%4]
		if(flag):
			best=-10000
			if old_move != (-1,-1) and board.block_status[allowed_block[0]][allowed_block[1]] == '-':
				for i in range(4*allowed_block[0], 4*allowed_block[0]+4):
					for j in range(4*allowed_block[1], 4*allowed_block[1]+4):
						if board.board_status[i][j] == '-':
							#allowed_cells.append((i,j))
							board.board_status[i][j]='o'
							flag^=1
							new=(i,j)
							old_move=new
							best=self.max(best,self.minimax(board,old_move,depth+1,1,alpha,beta))
							board.board_status[i][j]='-'
							alpha=self.max(best,alpha)
							if alpha>=beta:
								break
					if alpha>=beta:
						break
							#if int(mvp[0])==i and int(mvp[1])==j:
						#	f1=1
			else:
				for i in range(16):
					for j in range(16):
						if board.board_status[i][j] == '-' and board.block_status[i/4][j/4] == '-':
							#allowed_cells.append((i,j))
							#if int(mvp[0])==i and int(mvp[1])==j:
							board.board_status[i][j]='o'
							flag^=1
							new=(i,j)
							old_move=new
							best=self.max(best,self.minimax(board,old_move,depth+1,1,alpha,beta))
							board.board_status[i][j]='-'
							alpha=self.max(best,alpha)
							if alpha>=beta:
								break
					if alpha>=beta:
						break
			return best
		else:
			best=10000
			if old_move != (-1,-1) and board.block_status[allowed_block[0]][allowed_block[1]] == '-':
				for i in range(4*allowed_block[0], 4*allowed_block[0]+4):
					for j in range(4*allowed_block[1], 4*allowed_block[1]+4):
						if board.board_status[i][j] == '-':
							#allowed_cells.append((i,j))
							board.board_status[i][j]='x'
							flag^=1
							new=(i,j)
							old_move=new
							#old_move[0]=i
							#old_move[1]=j
							best=self.min(best,self.minimax(board,old_move,depth+1,1,alpha,beta))
							beta=self.min(beta,best)
							board.board_status[i][j]='-'
							if alpha>=beta:
								break
					if alpha>=beta:
						break
						#if int(mvp[0])==i and int(mvp[1])==j:
						#	f1=1
			else:
				for i in range(16):
					for j in range(16):
						if board.board_status[i][j] == '-' and board.block_status[i/4][j/4] == '-':
							#allowed_cells.append((i,j))
							#if int(mvp[0])==i and int(mvp[1])==j:
							board.board_status[i][j]='x'
							flag^=1
							new=(i,j)
							old_move=new
							best=self.min(best,self.minimax(board,old_move,depth+1,1,alpha,beta))
							beta=self.min(beta,best)
							board.board_status[i][j]='-'
							if alpha>=beta:
								break
					if alpha>=beta:
						break
			return best

	def max(self,a,b):
		if a>b:
			return a
		else:
			return b
	def min(self,a,b):
		if a<b:
			return a
		else:
			return b
	def evaluate(self,board,old_move):
		allowed_block = [old_move[0]%4, old_move[1]%4]
		if old_move != (-1,-1) and board.block_status[allowed_block[0]][allowed_block[1]] == '-':
			for i in range(4*allowed_block[0], 4*allowed_block[0]+4):
				if board.board_status[i][0]==board.board_status[i][1] and board.board_status[i][1]==board.board_status[i][2] and board.board_status[i][2]==board.board_status[i][3]:
					if board.board_status[i][0]=='x':
						return -100
					else:
						return 100
			for j in range(4*allowed_block[1], 4*allowed_block[1]+4):
				if board.board_status[0][i]==board.board_status[1][i] and board.board_status[2][i]==board.board_status[1][i] and board.board_status[2][i]==board.board_status[3][i]:
					if board.board_status[i][0]=='x':
						return -100
					else:
						return 100
		else :
			pass
