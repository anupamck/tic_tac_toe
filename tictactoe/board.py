class MoveError(Exception):
    pass


def assign_marker(player):  # Assigns marker to player
    if player.lower() == "human":
        return "X"
    elif player.lower() == "comp" or player.lower() == "computer":
        return "O"
    else:
        raise MoveError("Player must be human or computer")

def declare_result(winner):  # prints the result to the output
    if winner == "computer": # Should I have included  this as a method inside Board?
        print("Game over. Computer wins!")
        exit(0)
    elif winner == "human":
        print("Game over. You win!")
        exit(0)
    elif winner == "draw":
        print("Game over. Game drawn.")
        exit(0)
    else:
        MoveError("Invalid argument. Must be 'human', 'computer or 'draw")


class Board:
    def __init__(self):
        self.status = {'tl':' ', 'tm':' ', 'tr':' ',
                       'cl':' ', 'cm':' ', 'cr':' ',
                       'bl':' ', 'bm':' ', 'br':' '}


        self.sequences = (('tl', 'tm', 'tr'),
                          ('cl', 'cm', 'cr'),
                          ('bl', 'bm', 'br'),
                          ('tl', 'cl', 'bl'),
                          ('tm', 'cm', 'bm'),
                          ('tr', 'cr', 'br'),
                          ('tl', 'cm', 'br'),
                          ('tr', 'cm', 'bl'))


    def print_board(self): # Prints board status to console
        print("_________________\n")  # How do I write unit tests?
        i = 1
        for cell in self.status.values():
            print(cell, end="")
            if i % 3 == 0:
                print()
                if i != 9:
                    print("------")
                else:
                    print()
            else:
                print("|", end="")
            i += 1


    def mark_move(self, move, player): # Marks move on board
        marker = assign_marker(player)
        if self.status[move] == " ":
            self.status[move] = marker
        else:
            raise MoveError("Cell already marked")


    def get_sequence_string(self, sequence): # Output sequence position as a string
        string_list = []
        for position in sequence:
            string_list.append(self.status[position])
        return ''.join(string_list)


    def check_result(self, player): # Returns current result - win, draw, near win or unclear
        marker = assign_marker(player)
        result = ""
        near_win = False
        result_unclear = False

        for sequence in self.sequences:
            sequence_string = self.get_sequence_string(sequence)
            if sequence_string == 3 * marker:
                result = "win"
                break
            elif sequence_string.replace(' ', '') == 2 * marker:
                near_win = True
            elif ' ' in sequence_string:
                result_unclear = True
            else:
                result = "draw"

        if result == "win":
            return "win"
        elif near_win:
            return "near win"
        elif result_unclear:
            return "unclear"
        elif result == "draw":
            return "draw"
        else:
            raise MoveError("Unknown result encountered")

    def mark_human_move(self, move):   # Marks human move with some error handling
        if move in self.status.keys(): # Architecture is rigid for human vs. computer player
            self.mark_move(move, "human")
        else:
            raise MoveError("Invalid input")

    def get_empty_positions(self):  # Returns a list of empty positions on board
        result = []
        for k, v in self.status.items():
            if v == ' ':
                result.append(k)
            else:
                pass
        return result
