from src.Game import Game

def main():
	g = Game()
	g.play()
	winner = g.getWinner()

	if (winner == None):
		print("Tie Game")
	else:
		print("Winner: " + str(winner))
	return

main()