import numpy as np

# Function Example
def fibonacci(n: int) -> int:
    """Return the `n`th Fibonacci number, for positive `n`. """
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

print("*"*30 + " Matrices " + "*"*30)

# Create Matrix
# Matrix A
ArrayA = [[1,2,3],
     [4,5,6],
     [7,8,9]]
print("Matrix A:\n", ArrayA)

# Matrix B
ArrayB = np.array([[1,3,5],[7,9]])
print("Matrix B:\n", ArrayB)

# Matrix C
ArrayC = np.ones((3,4))
print("Matrix C:\n", ArrayC)

# Matrix D
ArrayD = np.eye(5,dtype=int)
print("Matrix D:\n", ArrayD)

# Matrix E
ArrayE = np.random.rand(3,5)
print("Matrix E:\n", ArrayE)

# Matrix F
ArrayF = np.random.randn(3,5)
print("Matrix F:\n", ArrayF)

# Matrix G
ArrayG = np.matrix("1 0; 0 1")
print("Matrix G:\n", ArrayG)
