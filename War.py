from src.Game import Game

class War():
	def main():
		g = Game()
		g.play()
		winner = g.getWinner()

		if (winner == None):
			print("Tie Game")
		else:
			print("Winner: " + str(winner))
		return

if __name__ == '__main__':
	War()