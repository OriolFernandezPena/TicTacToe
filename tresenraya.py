class TicTacToe():
    '''
        This class implements the Tres en Raya game which consists on ...
    '''
    def __init__(self):
        self.game = [[None, None, None], [None, None, None], [None, None, None]]

    def displayGame(self) -> None:
        '''
            This function just displays de game so we can play at the terminal
        '''
        print("\n")
        for row in self.game:
            for element in row:
                print(element, end="\t")
            print("\n")
        # print(self.game)
    
    def checkMove(self, position: tuple) -> bool:
        '''
            This function checks if a given position is empty or not.
            Input:
                position: tuple
            Output:
                _ : bool
        '''
        if self.game[position[0]][position[1]] == None:
            return True
        return False
    
    def updateGame(self, position: tuple, player: int) -> None:
        '''
            This function updates de game board after a move.
            Inputs:
                position: tuple
                player: int
            Outputs:
                None
        '''
        self.game[position[0]][position[1]] = player
    
    def collinearPoints(self, p1: tuple, p2: tuple, p3: tuple) -> bool:
        '''
            This method uses the triangle method to check if 3 points are collinear.
            We compute the double of the triangle area, if it's zero we know they are collinear.

            Inputs:
                p1: tuple
                p2: tuple
                p3: tuple

            Returns:
                bool
        '''
        scaledTriangleArea = (p1[0] - p2[0])*(p2[1] - p3[1]) - (p2[0] - p3[0])*(p1[1] - p2[1])
        if scaledTriangleArea == 0:
            return True
        return False
    
    def checkGame(self, verbose=False) -> tuple:
        '''
            This method checks if, at a given time, the game is finished whether because there's no more
            available moves whether a player won.

            returns:
                gameFinished : bool
                winner : int/None
        '''
        gameFinished : bool = False
        winner = None

        positions_player_0 = [[i, j] for i in range(3) for j in range(3) if self.game[i][j] == 0]
        positions_player_1 = [[i, j] for i in range(3) for j in range(3) if self.game[i][j] == 1]

        if len(positions_player_0) + len(positions_player_1) == 9:
            gameFinished = True

        # This check list could be optimised but we can only have 9 different positions.
        check_0 = [[p1, p2, p3] for p1 in positions_player_0 for p2 in positions_player_0 for p3 in positions_player_0 
        if (p1 != p2) & (p1 != p3) & (p2 != p3)]

        if verbose:
            print('Checking player 0')
            print(check_0)
            print('\n')

        for positions in check_0:
            if self.collinearPoints(positions[0], positions[1], positions[2]):
                gameFinished = True
                winner = 0
        
        # This check list could be optimised but we can only have 9 different positions.
        check_1 = [[p1, p2, p3] for p1 in positions_player_1 for p2 in positions_player_1 for p3 in positions_player_1 
        if (p1 != p2) & (p1 != p3) & (p2 != p3)]

        if verbose:
            print('Checking player 1')
            print(check_1)
            print('\n')

        for positions in check_1:
            if self.collinearPoints(positions[0], positions[1], positions[2]):
                gameFinished = True
                winner = 1

        return gameFinished, winner

    def play(self):
        '''
            This method implements the playing game.
        '''

        nextPlayer = 0


        while(True):
            self.displayGame()
            move_x : int
            move_y : int
            move_x, move_y = int(input()), int(input())
            if self.checkMove([move_x, move_y]):
                self.updateGame([move_x, move_y], nextPlayer)
            else:
                print("Try again, that position is already filled!")
                continue

            ended, winner = self.checkGame()
            if ended:
                print("The game is over")
                if winner != None:
                    print("Player {} won the game".format(winner))
                    self.displayGame()
                else:
                    print("No one won.")
                    self.displayGame()
                break
            nextPlayer += 1
            nextPlayer %= 2