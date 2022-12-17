
class Field:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.value = None
        self.notes = {x for x in range(1,10)}
        self.square = ((row-1)//3, (column-1)//3)
    
    def __repr__(self) -> str:
        return f'Field object: row = {self.row}, column = {self.column}, value = {self.value}'

class Board:
    def __init__(self, values):
        self.fields = set()
        for row_number, row_values in enumerate(values):
            for column_number, value in enumerate(row_values):
                new_field = Field(row_number+1, column_number+1)
                if value != 0:
                    new_field.value = value
                self.fields.add(new_field)
        print(f'----------INITIALIZED----------')
        self.print()

    
    def get_field_by_location(self, row, column):
        for field in self.fields:
            if field.row == row and field.column == column:
                return field

    def insert_value(self, row, column, value):
        field = self.get_field_by_location(row, column)
        field.value = value
    
    def get_row(self, row_number):
        return [field for field in self.fields if field.row == row_number]
    
    def get_column(self, column_number):
        return [field for field in self.fields if field.column == column_number]
    
    def get_square(self, square):
        return [field for field in self.fields if field.square == square]
    
    def solved(self):
        return None not in [field.value for field in self.fields]
    
    def print(self):
        for row_number in range(0,10):
            fields = self.get_row(row_number)
            fields.sort(key=lambda x: x.column)
            for field in fields:
                value = field.value if field.value is not None else ' '
                print(f'{value} ', end='')
            print()
            



class Solver:
    def __init__(self, board):
        self.board = board
        iteration = 1
        while not self.board.solved():
            for field in self.board.fields:
                if field.value is None:
                    self.solve(field)
            print(f'-------------[ITERATION {iteration}]-------------')
            self.board.print()
            print(f'solved? - {self.board.solved()}')
            iteration += 1

    def solve(self, field):
        #field.notes = {x for x in range(1,10)}
        values_in_this_row = {field.value for field in self.board.get_row(field.row) if field.value is not None}
        values_in_this_column = {field.value for field in self.board.get_column(field.column) if field.value is not None}
        values_in_this_square = {field.value for field in self.board.get_square(field.square) if field.value is not None}
        values_to_exclude = values_in_this_row.union(values_in_this_column.union(values_in_this_square))
        field.notes.difference_update(values_to_exclude)
        if len(field.notes) == 1:
            for value in field.notes:
                field.value = value
            field.notes.clear()
        

if __name__ == '__main__':

    easy_values = [
        [0,0,0,2,6,0,7,0,1],
        [6,8,0,0,7,0,0,9,0],
        [1,9,0,0,0,4,5,0,0],
        [8,2,0,1,0,0,0,4,0],
        [0,0,4,6,0,2,9,0,0],
        [0,5,0,0,0,3,0,2,8],
        [0,0,9,3,0,0,0,7,4],
        [0,4,0,0,5,0,0,3,6],
        [7,0,3,0,1,8,0,0,0]
    ]

    board = Board(easy_values)
    #run a solver on board
    solver = Solver(board)
