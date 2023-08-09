class Matrix:
    def __init__(self, matrix_string):
        self.data = list()
        for line in matrix_string.split("\n"):
            row = list()
            for c in line.split(" "):
                row.append(int(c))
            self.data.append(row)
            
    def row(self, index):
        return self.data[index - 1]

    def column(self, index):
        col = list()
        for line in self.data:
            col.append(line[index-1])
        return col
