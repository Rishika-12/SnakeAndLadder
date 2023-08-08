#snake and ladder game with OOPS
'''
Terms used
--n_players represents number of players playing the game
--verbose used to decide winner based on it
--last_title is used to represent the end point
--dice_roll function is used to roll the dice and get a number bt 1 to 6
--player_i denotes the player number (eg if 2 players player_i is 1 and 2)
--move_player is used to move each player and in this we check if the player is winner
or decide the position based on dice number
--move_players used to result all the players move in one turn
--play_game is main fn and used to play the game
--print_turn is used to create turns and do the indicated operations
--enumerate is a built-in fn used to keep track of iteration
'''
from random import randint
class SnakeAndLadder:
    snakes={
        98:79,
        95:75,
        91:72,
        87:36,
        64:60,
        62:19,
        54:34,
        17:7,
    }
    ladders={
        1:38,
        4:14,
        9:31,
        21:42,
        28:84,
        51:67,
        72:91,
        80:99,
    }
    last_tile=100
    def __init__(self,n_players,verbose=False):
        self.n_players=n_players
        self.verbose=verbose
        self.players=[0]*n_players
        self.turn=0
        self.winner=None
    def dice_roll(self):
        dice_num = randint(1, 6)
        print(f"We got {dice_num} in the roll!")
        return dice_num
    def move_player(self,player_i):
        prev_position=self.players[player_i]
        new_position=prev_position+self.dice_roll()
        #deciding the winner
        if new_position >= self.last_tile:
            self.winner=player_i
            new_position=self.last_tile
        elif new_position in self.snakes:
            new_position=self.snakes[new_position]
            print(f"Snake encountered {player_i+1} is moved from {prev_position+1} to {new_position}")
        elif new_position in self.ladders:
            new_position=self.ladders[new_position]
            print(f"Ladder encountered {player_i+1} is moved from {prev_position+1} to {new_position}")
        self.players[player_i]=new_position
    def move_players(self):
        for player_i in range(self.n_players):
            self.move_player(player_i)
            if self.winner is not None:
                break
    def play_game(self):
        while self.winner is None:
            self.turn+=1
            self.move_players()
            if self.verbose:
                self.print_turn()
        return f"player #{self.winner+1} Wins!"
    def print_turn(self):
        print(f"Turn {self.turn}")
        #sort players by position
        pos_and_player=[(position,player_i) for player_i, position in enumerate(self.players)] 
        pos_and_player.sort(reverse=True)      
        #Players by Position
        player_position = ' | '.join([f"player {player_i+1} in {position}" for position, player_i in pos_and_player])
        print(player_position)
n_players=int(input("enter number of players:"))
game=SnakeAndLadder(n_players,verbose=True)
#print(game.move_players())
#print(game.print_turn())
print(game.play_game())