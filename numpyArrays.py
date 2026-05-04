import numpy as np
from pandas.core.dtypes import dtypes

# Quickly create built-in function
print(np.arange(0, 4))

# np.linspace() You can quickly create an array using linspace func
print(np.linspace(0, 50, 3))
# and np.logspace() and in this function as well
print(np.logspace(0, 3, 4, base=10))
# Question
print(np.arange(10, 101, 5))
print(np.linspace(0, 1000, 26))

# np.zeros()
print(np.zeros((2, 3), dtype=int))
# np.ones
print(np.ones((2, 3, 2), dtype=int))
# np.eye
print(np.eye(3, dtype=int)) # 3x3 birim matris, kosegen matris
print('\n')
# Question
print(np.zeros((2,6), dtype=int))
print('\n')
# Generating random data with the np.random() module
print(np.random.rand(3)) # 0-1 araliginda deger olusturur
print('\n')
print(np.random.rand(2,2))
print('\n')
print(np.random.randint(0,10,(2,2)))
print('\n')
print(np.random.randint(0,50,(4,6)))
print('\n')
# Arrayin boyut sayisini ve shape'ini kontrol etmek
arr0d = np.array(50)
print(arr0d)
arr1d = np.array([1,2,3])
print(arr1d)
arr2d = np.array([[4,5,6],[7,8,9]])
print(arr2d)
arr3d = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr3d)
print(arr3d.ndim)
print(arr3d.shape)
print('\n')

# NumPy Arraylarini Indexleme ve Ogelerine Erisme
print(arr2d)
print(arr2d[1,2])
print('\n')
print(arr3d)
print(arr3d[0,2,-1]) # Negatif indexleme
print('\n')

# Question
print(np.arange(53, 62)[4]) # 53den 61e kadar tam sayi olusturup 4. index'i alma
print('\n')

# NumPy Dizilerinin Max-Min elemanlarina ve bu elemanlarin indexlerine erisme
arr = np.random.randint(1,100,10)
print(arr.argmax()) # En buyuk sayinin indexi
print(arr.max()) # en buyuk sayi
print(arr.argmin()) # En kucuk sayinin inexi
print(arr.min()) # En kucuk sayi
print('\n')

# NumPy Arraylarinde Slicing() dilimleme vs Broadcasting yapma
arrSlicing = np.arange(0,10)
arrSlicing[2:8] = 999 # Broadcasting
print(arrSlicing)
print('\n')

# Question
arrQ = np.arange(-30,11)
print(arrQ[5:19])
print('\n')

# Bir Arrayin Data Type'ini Kontrol etme .dtype attribute'i ileE
print(arrQ)
print(arrQ.dtype)
print(arrQ.astype(str))
print('\n')

# Question
arr1 = np.array(['5','7','2','2','5','8'])
arr1int = arr1.astype(int)
print(arr1)
print(arr1.dtype)
print(arr1int)
print(arr1int.dtype)