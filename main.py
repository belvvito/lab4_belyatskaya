import numpy as np
import matplotlib.pyplot as plt

y = lambda x: 2*x**4 - 8*x**3 + 9*x**2 + 54*x - 3

x = np.linspace(-5, 5, 400)

print('   x        y(x)')
for temp in x:
    print(f'{temp:.2f} {y(temp):.2f}')

f_values = y(x)
xmax = x[np.argmax(f_values)]
fmax = np.max(f_values)
xmin = x[np.argmin(f_values)]
fmin = np.min(f_values)

print(f'Xmax = {xmax:.2f} Ymax = {fmax:.2f}')
print(f'Xmin = {xmin:.2f} Ymin = {fmin:.2f}')

plt.figure(figsize=(8, 6))
plt.plot(x, f_values, label='y(x) = 2x⁴ - 8x³ + 9x² + 54x - 3')
plt.plot(xmax, fmax, 'ro', label=f'Max: ({xmax:.2f}, {fmax:.2f})')
plt.plot(xmin, fmin, 'go', label=f'Min: ({xmin:.2f}, {fmin:.2f})')
plt.title('График функции')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.grid(True)
plt.show()
