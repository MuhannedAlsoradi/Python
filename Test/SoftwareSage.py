import numpy as np
arr = np.arange(1, 6, 2, dtype=int)
print(arr)
# output: [0 2 4 6]
x = np.array([1, 2], dtype=int)
y = np.array([3, 4, 5], dtype=int)
z = np.array([6, 7, 8], dtype=float)
result = np.concatenate((x, x, z))
print(result)
# output: [1. 2. 3. 4. 5. 6. 7. 8.]
x = np.arange(50, 300, 50, dtype=int)
print(x[0:3])
# output: [50 100 150]


class Vehicle:
    def init(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


# School_bus = Bus("School Volvo", 180, 12)
# print(School_bus.name)
print(16//3)
