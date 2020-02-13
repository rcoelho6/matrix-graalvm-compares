class Matrix:
    def __init__(self, matrix = []):
        self.matrix = matrix

    def hasSequenceOf(self, value = ''):
        if value != "":
            before = ''
            for line in self.matrix:
                #for value in line.split():
                for char in list(line):
                    if char == before:
                        count += 1
                        if char == value:
                            return True
                    else:
                        count = 1
                    if count >= 4:
                        return True
                    before = value
        return False
