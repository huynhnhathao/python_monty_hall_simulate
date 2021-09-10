import numpy as np

class MontyGame:
    def __init__(self):
        self.door1 = False
        self.door2 = False
        self.door3 = False

        self.all_door = [self.door1,self.door2, self.door3]
        
    def reset(self):

        self.player_choice = None
        self.monty_opened = None
        car_door = np.random.randint(1, 4, 1)[0]
        for i  in range(len(self.all_door)):
            self.all_door[i] = False
        self.all_door[car_door - 1] = True

    def get_result(self, door_number):
        assert door_number < len(self.all_door)
        return self.all_door[door_number]

    def choose_door(self,your_choice )-> int:
        # you choose a door, and monty open another door, 
        # and return you the door number that has a goat
        self.player_choice = your_choice
        # if you choose the winning door
        if self.all_door[self.player_choice-1]:
            self.if_switch = False
            self.if_not_switch = True
        # if you choose the goat door
        if not self.all_door[self.player_choice - 1]:
            self.if_switch = True
            self.if_not_switch = False

        for i, door in enumerate(self.all_door):
            if i + 1 != your_choice and not door:
                self.monty_opened  = i+1

                return self.monty_opened

        return -1

    def final_result(self, your_choice: bool):
        # you choose switch or not, and monty tell you win or not
        # he choose to switch
        if your_choice:
            return self.if_switch

        # he choose to keep
        if not your_choice:
            return self.if_not_switch

        return None


def play_game(num_games:int,strategy:str, game: MontyGame) -> float:
    # play num_games of monty game with strategy and return the fraction of winning
    # strategy can only in ['switch', 'not_switch']
    num_win = 0
    if strategy =='switch':
        for i in range(num_games):
            game.reset()
            game.choose_door(np.random.randint(1, 4, 1)[0])
            result = game.final_result(True)
            if result:
                num_win +=1

    if strategy == 'not_switch':
        for i in range(num_games):
            game.reset()
            game.choose_door(np.random.randint(1, 4, 1)[0])
            result = game.final_result(False)
            if result:
                num_win += 1

    return num_win/num_games


if __name__ == '__main__':
    
    game = MontyGame()
    play_game(100000, 'not_switch', game)