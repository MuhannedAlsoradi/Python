import numpy as np
a = np.array([1, 2, 3, 4, 5], int)
print(a)
print(type(a))
print(a[:2])
print(a[3])
a[2] = 20
print(a)
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
print(a[0, 0])
print(a[0, 1])
print(a[1, : 3])
print(a[:, 2])
print(a[-1:, -2:])
print(a.shape)
print(a.dtype)
print(len(a))
print(2 in a)
print(0 in a)
a = np.array(range(10), float)  # 0-9
print(a)
b = a.reshape((5, 2))
print(b)
print(b.shape)
c = a.copy()
a = b
print(c)
a[0] = 0
print(a)
print(b)
print(c)
print(a.tolist())
print(list(a))
a = np.array([1, 2, 3], int)
a.fill(0)
print(a)
a = np.array(range(10), float)  # 0-9
print(a)
b = a.reshape((5, 2))
print(b)
b.transpose()
print(b.transpose())
print(b.flatten())
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])
d = np.concatenate(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
print(d)
a = np.array([[1, 2], [3, 4]], int)
b = np.array([[5, 6], [7, 8]], int)
c = np.concatenate((a, b), axis=0)
print(c)
c = np.concatenate((a, b), axis=1)
print(c)
a = np.array([1, 2, 3], float)
print(a[:, np.newaxis])
print(a[:, np.newaxis].shape)
a = np.array([1, 2, 3], float)
print(a[np.newaxis, :])
print(a[np.newaxis, :].shape)
print(np.arange(5, dtype=int))  # 0-4
print(np.arange(1, 6, 2, dtype=int))  # 1-5 step=2
print(np.ones((2, 3), dtype=float))
print(np.zeros((2, 3), dtype=float))
print(np.zeros_like(a, dtype=float))
print(np.ones_like(a, dtype=float))
print(np.identity(4, dtype=int))
print(np.eye(4, k=1, dtype=int))
print(np.eye(4, k=-1, dtype=int))
a = np.array([1, 2, 3], int)
b = np.array([4, 5, 6], int)
print(a*b)
print(a+b)
print(a-b)
print(a**b)
print(a % b)
# a = np.array([1, 2, 3], int)
# b = np.array([4, 5], int)
# print(a+b)
a = np.array([[1, 2], [3, 4], [5, 6]], int)
b = np.array([[7, 8]], int)
print(a+b)
print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))
print(np.pi)
print(np.e)
a = np.array([1, 2, 3], int)
for x in a:
    print(2*x)
a = np.array([[1, 4], [2, 6], [3, 7]], int)
for x in a:
    for m in x:
        print(2*m)
a = np.array([[1, 4], [2, 6]], int)
for x, i in a:
    print(x, i, x*i)
a = np.array([[1, 4, 3], [2, 6, 5]], int)
for i, j, k in a:
    print(i, j, k)
a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.min(a))
print(np.max(a))
print(np.sum(a))
print(np.prod(a))
print(np.std(a))
print(np.mean(a))
print(np.argmax(a))
print(np.argmin(a))
print(np.var(a))
# s = a.tostring() # deprecated
# print(np.fromstring(s)) # deprecated
# a = np.array(range(2, 7), int)  # 2-6
# print(a)
# a = np.array(range(2, 7, 2), int)  # 2-6 step: 2
# print(a)
# # must be the same length
# #  # 0 1 2
# # 0# 1 2 3
# # 1# 4 5 6
# # 2# 7 8 9
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], int)
# print(a[2, 2])
# print(a[2, :2])
# print(a[:2, :2])  # two dim array
# print(a[1:2, 1:2])  # [[5]]
# print(a[:2, 2])  # [3,6]
# b = np.array(range(5, 15), float)
# print(b)
# # b.reshape(range(15, 5)) #if (2,5) just (5,2) else exception
# # print(b)
# # one and two dimensional arrays
# # a.dtype() type of element in the array
# # type(a) type of the array
# # np.shape(a)
# # len(a)
# # np.size(a) # no. of elements in the array
# # a[0:1] slicing
# # b[1,2] = 100
# # mutable array!
# # copy()
# # tolist()
# # list()
# # two dim array to list using tolist()
# # print object of array
# # [array([1,2,3]),array([1,2,3]),array([5,6,7])]
# # tolist()
# # [[1,2,3],[1,2,3],[5,6,7]]
# # a.fill(100)
# # [[100,100,100],[100,100,100],[100,100,100]]
