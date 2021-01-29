import numpy

class MoveError(Exception):
    pass

class InputError(Exception):
    pass


def generate_matrix(length, char):
    matrix = []
    for row in range(length):
        row = []
        for column in range(length):
            row.append(char)
        matrix.append(row)
    return matrix


class Board:
    def __init__(self):
        self.__length = 3
        self.matrix = generate_matrix(self.__length, ' ')

    def __get_length(self):
        return self.__length

    def __set_length(self, length):
        self.__length = length

    length = property(__get_length, __set_length)

    def print_board(self):
        print("_________________\n")  # How do I write unit tests?
        i = 1
        for row in self.matrix:
            print(*row, sep="|")
            if i != self.__length:
                print("------")
            else:
                print()
            i += 1

    def mark_move(self, move, player):
        if self.matrix[move[0]][move[1]] == " ":
            self.matrix[move[0]][move[1]] = player.symbol
        else:
            raise MoveError("Cell already marked")

    def generate_sequences(self):
        return (self.matrix +
                numpy.transpose(self.matrix).tolist() +
                [numpy.diagonal(self.matrix).tolist()] +
                [numpy.diagonal(numpy.fliplr(self.matrix)).tolist()])

    def check_result(self, player):         # Send for code review
        result = ""
        near_win = False
        result_unclear = False
        sequences = self.generate_sequences()

        for sequence in sequences:
            sequence_string = ''.join(sequence)
            if sequence_string == 3 * player.symbol:
                return "win"
        for sequence in sequences:
            sequence_string = ''.join(sequence)
            if sequence_string.replace(' ', '') == 2 * player.symbol:
                return "near win"
        for sequence in sequences:
            sequence_string = ''.join(sequence)
            if ' ' in sequence_string:
                return "unclear"

        return "none"


    def generate_move_list(self):
        move_list = []
        for row in range(self.__length):
            for column in range(self.__length):
                move_list.append((row, column))
        return move_list


    def mark_human_move(self, player, move):
        legal_moves = ("tl", "tm", "tr",
                       "cl", "cm", "cr",
                       "bl", "bm", "br")
        move_list = self.generate_move_list()
        if move in legal_moves:
            move = move_list[legal_moves.index(move)]
            self.mark_move(move, player)
        else:
            raise MoveError("Invalid input")

    def get_empty_positions(self):
        result = []
        for row in range(self.__length):
            for column in range(self.__length):
                if self.matrix[row][column] == ' ':
                    result.append((row, column))
        return result
