import numpy as np


def task_1(a, b):
    try:
        x = np.linalg.solve(a, b)
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
            print('A matrix input')
            for i in range(int(a.shape[0])):
                for j in range(int(a.shape[1])):
                    try:
                        a[i, j] = np.array(int(input()))
                    except ValueError:
                        print("Please write the numbers")

            print("B matrix input")
            for i in range(int(b.shape[0])):
                for j in range(int(b.shape[1])):
                    try:
                        b[i, j] = np.array(int(input()))
                    except ValueError:
                        print("Please write the numbers")
            task_1(a, b)
        else:
            break


if __name__ == '__main__':
    main()
