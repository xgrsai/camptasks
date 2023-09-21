import numpy as np


def task_1(a, b):
    try:
        x = np.linalg.solve(a, b)
        print("X = ", np.transpose(x))
    except np.linalg.LinAlgError:
        print("The system of equations has no solution.")


def task_1_un(a, b, matrix_size):  # without linalg.solve / Cramer's rule
    try:
        x = b.copy()

        for i in range(matrix_size):
            temp = a.copy()
            determin = np.linalg.det(a)
            for j in range(matrix_size):
                temp[j][i] = b[j][0]
            determin_n = np.linalg.det(temp)
            x[i, 0] = determin_n / determin
        print("X =", np.transpose(x))
    except np.linalg.LinAlgError:
        print("The system of equations has no solution.")


def main():
    a = np.array([[1, 2, 3], [0, 1, 1], [2, 0, 0]])
    b = np.array([[1], [1], [0]])
    task_1(a, b)
    while True:
        answer = input("Do you want to continue? Y/N")
        if answer == "Y" or answer == "y":
            print('Press enter after writing the numbers')
            matrix_size = abs(int(input("Matrix_size: ")))
            if matrix_size > 1:
                try:
                    a = np.zeros([matrix_size, matrix_size])
                    b = np.zeros([matrix_size, 1])
                    print("A matrix input: ")
                    for i in range(int(matrix_size)):
                        for j in range(int(matrix_size)):
                            a[i, j] = np.array(int(input()))

                    print("B matrix input: ")
                    for i in range(int(matrix_size)):
                        for j in range(b.shape[1]):
                            b[i, j] = np.array(int(input()))
                    task_1_un(a, b, matrix_size)
                except ValueError:
                    print("Please write the numbers")
            else:
                print("Matrix size must be at least 2")
        else:
            break


if __name__ == '__main__':
    main()
