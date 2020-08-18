class MatrixCalc:

    def __init__(self):
        self.rows = 0
        self.column = 0
        self.size = 0
        self.player_choice = None
        self.m = None
        self.m1 = None
        self.m2 = None
        self.pick = 0
        self.co_factors = []
        self.minors = []
        self.matrix = []

    def build_matrix(self):
        self.size = input().split()
        if len(self.size) != 2:
            self.build_matrix()
        else:
            try:
                self.rows = int(self.size[0])
                self.column = int(self.size[1])
                if self.player_choice == "1" or self.player_choice == "3":
                    if self.m1 is None:
                        print("Enter first matrix:")
                    else:
                        print("Enter second matrix:")
                    self.get_inputs()
                elif any((self.player_choice == "2", self.player_choice == "4", self.player_choice == "5", self.player_choice == "6")):
                    print("Enter matrix:")
                    self.get_inputs()
            except ValueError:
                print("you must enter numbers")
                self.build_matrix()
        return self.matrix

    def get_inputs(self):
        while True:
            self.matrix = []
            for i in range(self.rows):
                try:
                    self.matrix.append(list(map(float, input(f"Enter row No: {i + 1}").split())))
                    if len(self.matrix[i]) == self.column:
                        pass
                    else:
                        break
                except ValueError:
                    print("you must enter numbers")
                    break
            else:
                break
        return self.matrix

    @staticmethod
    def show_matrix(result):
        temp = ([f"{j:6.2f}" for j in i]for i in result)
        print("The result is:")
        for i in temp:
            print(*i, sep="  ")
        print()

    def add_matrix(self, m1, m2):
        if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
            return self.show_matrix([[m1[i][j] + m2[i][j] for j in range(len(m1[0]))]for i in range(len(m1))])
        else:
            print("The operation cannot be performed.")

    def scalar_product(self, m, scalar=None):
        try:
            if scalar is None:
                scalar = float(input("Enter constant: "))
            return self.show_matrix([m[i][j] * scalar for j in range(len(m[0]))]for i in range(len(m)))
        except ValueError:
            print("you must enter numbers")
            self.scalar_product(m, scalar=None)

    def multiply_matrix(self, m1, m2):
        if len(m1[0]) == len(m2):
            return self.show_matrix([sum(m1[i][k] * m2[k][j] for k in range(len(m2)))
                                     for j in range(len(m2[0]))]for i in range(len(m1)))
        else:
            print("The operation cannot be performed.\n")

    def matrix_tr(self,m):
        if self.pick == "1":
            self.m = [[m[i][j] for i in range(len(m))]for j in range(len(m[0]))]
        elif self.pick == "2":
            self.m = [[m[i][j] for i in reversed(range(len(m)))] for j in reversed(range(len(m[0])))]
        elif self.pick == "3":
            self.m = [i[::-1] for i in m]
        elif self.pick == "4":
            self.m = m[::-1]
        return self.m

    def det(self, m):
        if len(m) != len(m[0]):
            return "Invalid Operation: This operation works on square matrix only"
        elif len (m) == 1:
            return m[0][0]
        else:
            indices = [[(i, j) for j in range(len(m))]for i in range(len(m))]
            minors = [[0 for j in range(len(m))]for i in range(len(m))]
            sign_mat = [[0 for j in range(len(m))]for i in range(len(m))]
            # print(f"Indices = {indices}\nminors = {minors}\nsign_mat = {sign_mat}\n {('*') * 20} ")
            for coordinates in indices:
                for x, y in coordinates:
                    element_sign = (-1) ** (x + y)
                    n = list([m[i][j] for j in range(len(m))if i != x and j != y]for i in range((len(m))))
                    n.pop(x)
                    minors[x][y]= n
                    # print(minors)
                    sign_mat[x][y] = element_sign
                    # print(sign_mat)

            self.co_factors =  [[sign_mat[i][j] * self.det(minors[i][j]) for j in range(len(m))]for i in range(len(m))]
            # print(co_factors)
            # print("*" * 20)
            result = [[m[i][j] * self.co_factors[i][j]for i in range(len(m))]for j in range(len(m))]
            return sum(result[0])

    def inverse_mat(self, m):
        self.pick = "1"
        return self.scalar_product(self.matrix_tr(self.co_factors), (1/self.det(m)))if self.det(m) != 0 else "This matrix doesn't have an inverse.\n"

    def menu(self):
        while True:
            print("1. Add matrices\n"
                  "2. Multiply matrix by a constant\n"
                  "3. Multiply matrices\n"
                  "4. Transpose matrix\n"
                  "5. Calculate a determinant\n"
                  "6. Inverse matrix\n"
                  "0. Exit")
            self.action()
            self.m1 = None

    def action(self):
        self.player_choice = input("Your choice: ")
        if self.player_choice == "1" or self.player_choice == "3":
            print("Enter size of first matrix: ", end="")
            self.m1 = self.build_matrix()
            print("Enter size of second matrix: ", end="")
            self.m2 = self.build_matrix()
            if self.player_choice == "1":
                self.add_matrix(self.m1, self.m2)
            elif self.player_choice == "3":
                self.multiply_matrix(self.m1, self.m2)
        elif self.player_choice == "2":
            print("Enter size of matrix: ", end="")
            self.build_matrix()
            self.scalar_product(self.matrix)
        elif self.player_choice == "4":
            print("\n1. Main diagonal\n"
                  "2. Side diagonal\n"
                  "3. Vertical line\n"
                  "4. Horizontal line")
            while True:
                self.pick = input("Your choice: ")
                if any((self.pick == "1", self.pick == "2", self.pick == "3", self.pick == "4")):
                    print("Enter matrix size: ", end="")
                    self.build_matrix()
                    self.show_matrix(self.matrix_tr(self.matrix))
                    break
        elif self.player_choice == "5":
            print("Enter matrix size: ", end="")
            self.build_matrix()
            print(f"The result is:\n{self.det(self.matrix)}\n")
        elif self.player_choice == "6":
            print("Enter matrix size: ", end="")
            self.build_matrix()
            self.inverse_mat(self.matrix)
        elif self.player_choice == "0":
            exit()

a = MatrixCalc()
a.menu()
