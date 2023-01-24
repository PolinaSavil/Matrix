
import array as arr

class Matrix:
    def __init__(self):
        self.values = []
        self.columns = []
        self.pointers = []
       

    def __repr__(self) -> str:
        string = "["
        for i in range(len(self.pointers)-1):
            prev = self.pointers[i]
            curr = self.pointers[i+1]
            string = string + "["
            for j in range(max(self.columns)):
                a = 0
                if self.columns[prev-1:curr-1].__contains__(j+1):
                    a = str(self.values[prev-1])
                    prev = prev+1
                else:
                    a = 0

                string = string + str(a) + ","
            string = string + "],"
        string = string + "]"
        string = string.replace(",]", "]")
        string = string + "\n"
        return string
    
    def __mul__(self,other):
        if isinstance(other, int):
            newMatrix = Matrix()
            newMatrix.columns = self.columns
            newMatrix.pointers = self.pointers
    
            for i in self.values:
                newMatrix.values.append(i*other)
        else:
            other = other.transp()
            newMatrix = Matrix()
            if (len(self.pointers) == len(other.pointers)):
                if (max(self.columns) == max(other.columns)):
                    newMatrix.pointers.append(1)
                    a = 1
                    for i in range(len(self.pointers)-1):
                        prev = self.pointers[i]
                        curr = self.pointers[i + 1]
    
    
                        for j in range(len(other.pointers) - 1):
                            othprev = other.pointers[j]
                            othcurr = other.pointers[j+1]
                            s = 0
                            for k in other.columns[othprev-1:othcurr-1]:
                                if self.columns[prev-1:curr-1].__contains__(k):
                                    othind = other.columns.index(k, othprev-1, othcurr-1)
                                    selfind = self.columns.index(k, prev - 1, curr - 1)
                                    s = s + other.values[othind] * self.values[selfind]
                            if s != 0:
                                newMatrix.values.append(s)
                                newMatrix.columns.append(j+1)
                                a = a + 1
    
                        newMatrix.pointers.append(a)
        return newMatrix

    def __add__(self,other):
        newMatrix = Matrix()
        if (len(self.pointers) == len(other.pointers)):
            if (max(self.columns) == max(other.columns)):
                newMatrix.pointers.append(1)
                a = 1
                for i in range(len(self.pointers) - 1):
                    prev = self.pointers[i]
                    curr = self.pointers[i + 1]
                    othprev = other.pointers[i]
                    othcurr = other.pointers[i+1]
                    s = 0
                    newCols = self.columns[prev-1:curr-1] + other.columns[othprev-1:othcurr-1]
                    newCols = sorted(newCols)
                    f = len(newCols)-1
                    k = 0
                    while k < f:
                        if newCols[k] == newCols[k+1]:
                            newCols.remove(newCols[k])
                            f = f -1
                        k = k+1

                    k = 0
                    for k in newCols:
                        s = 0;
                        if self.columns[prev-1:curr-1].__contains__(k):
                            selfind = self.columns.index(k, prev - 1, curr - 1)
                            s = s +  self.values[selfind]

                        if other.columns[othprev- 1:othcurr - 1].__contains__(k):
                            otherind = other.columns.index(k, othprev - 1, othcurr - 1)
                            s = s + other.values[otherind]
                        a = a+1
                        newMatrix.values.append(s)
                        newMatrix.columns.append(k)

                    newMatrix.pointers.append(a)
        return newMatrix


    def transp(self):
        matrix = Matrix()
        realValues = []
        indValues = []
        for i in range(max(self.columns)):
            realValues.append([0] * (len(self.pointers)-1))
            indValues.append([0] * (len(self.pointers)-1))
        for i in range(len(self.pointers) - 1):
            prev = self.pointers[i]
            curr = self.pointers[i + 1]
            a = 0
            for j in range(max(self.columns)):
                if self.columns[prev - 1:curr - 1].__contains__(j + 1):
                    realValues[j][i] = self.values[prev-1]
                    indValues[j][i] = i
                    prev = prev + 1
                    a = a + 1

        matrix.pointers.append(1)
        for j in range(max(self.columns)):
            a = 0;
            for i in range(len(self.pointers)-1) :
                if realValues[j][i] != 0:
                    matrix.values.append(realValues[j][i])
                    matrix.columns.append(i+1)
                    a = a + 1
            matrix.pointers.append(matrix.pointers[j] + a)
        return matrix


    @staticmethod
    def parse(string: str):
        matrix = Matrix();
        string = string.replace("],[", ":")
        string = string.replace("[[", "")
        string = string.replace("]]","")
        strings = string.split(":")
        strNum = 1
        matrix.pointers.append(strNum)
        for st in strings:
            colNum = 1

            for value in st.split(","):
                if "0" != value:
                    matrix.values.append(int(value))
                    matrix.columns.append(colNum)
                    strNum = strNum + 1
                colNum = colNum + 1
            matrix.pointers.append(strNum)
        return matrix


if __name__ == '__main__':
    f = open('matrix/input.txt', 'r')
    matrix = Matrix.parse(f.readline())
    matrix2 = Matrix.parse(f.readline())
    f.close()
    f = open('matrix/output.txt', 'w')
    matrix3 = matrix*5
    matrix4 = matrix3*matrix2
    matrix5 = matrix4+matrix2
    f.write(matrix3.__repr__())
    f.write(matrix4.__repr__())
    f.write(matrix5.__repr__())
    f.close()
    pass
