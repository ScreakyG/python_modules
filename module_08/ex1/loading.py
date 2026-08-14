import importlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

modules_list = ['pandas', 'numpy', 'requests', 'matplotlib']

def check_packages() -> None: 
    print("Checking dependencies:")
    for module in modules_list:
        try:
            imported_module = importlib.import_module(module)
            print(f"[OK] {imported_module.__name__} ({imported_module.__version__})")
        except ModuleNotFoundError as error:
            print(f"[KO] {module}: {error}")



print("LOADING STATUS: Loading programs...\n")
check_packages()

print()

print("Analyzing Matrix data...")
matrix = np.random.randint(0, 10, size=(1000, 2))
# print(matrix.shape)
# print(matrix[0, 1])
# print(matrix[0][1])
# print(matrix[:2, :])


print("Proccessing 1000 data points...")
df = pd.DataFrame(matrix, columns=["x", "y"])
# print(df.describe())
# print(df)


print("Generating visualization...")
x = df['x']
y = df['y']

plt.scatter(x, y)
plt.title("Matrix Analysis")
plt.xlabel('X')
plt.ylabel('Y')


filename = "matrix_analysis.png"
plt.savefig(filename)
print("Analysis complete!")
print(f"Results saved to: {filename}")
# plt.show()