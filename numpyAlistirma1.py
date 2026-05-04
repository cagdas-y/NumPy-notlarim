from email.policy import default

import numpy as np

# 1) Manuel değerleri el ile girerek 3 boyutlu bir array oluşturup bir değişkene atayın. Ardından 3 boyutlu olup olmadığına bakmak için dimension'ını kontrol edin
arr3d = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr3d)
print(arr3d.ndim)
print(arr3d.shape)
print('\n')
# 2) 34, 40, 46, 52... 112 şeklinde devam eden 1 boyutlu bir array oluşturun.
arr1d = np.arange(34,113)
print(arr1d)
print(arr1d.ndim)
print('\n')
# 3) 50-500 arasında lineer artış gösteren 91 tane tam sayıdan oluşan bir array oluşturun.(dtype'ı int olsun)
arrLin = np.linspace(50,500,91,dtype=int)
print(arrLin)
print(arrLin.dtype)
print(len(arrLin))
print('\n')
# 4) 100(10**2) ile 10000(10**5) arasında logaritmik artış gösteren 8 sayıdan oluşan bir array oluşturun.
arrLog = np.logspace(2,4,8,dtype=int)
print(arrLog)
print(arrLog.dtype)
print('\n')
# 5) 0-8 tam arasındaki ardışık tam sayılardan oluşan(0 ve 8 dahil toplam 9 değer) 3x3 shape'inde bir matris oluşturun.
arrTam = np.arange(9).reshape(3,3)
print(arrTam)
print('\n')
# 6) 6x6 formatında bir sıfır matrisi oluşturun. (dtype'ı int olsun)
print(np.zeros((6,6)))
print('\n'
)
# 7) 4x4 formatında bir bir matrisi oluşturun. (dtype'ı int olsun)
print(np.ones((4,4), dtype=int))
print('\n')
# 8) 8x8 formatında bir birim matris oluşturun. (Sadece sol köşegeni 1 geri kalan değerleri 0 olan matris'e birim matris deniyor.) (dtype'ı int olsun)
print(np.eye(8,8,dtype=int))
print('\n')
# 9) 5x5 formatında bir köşegen matrisi oluşturun (Sadece sol üstten sağ alta doğru olan köşegendeki değerleri 3 olsun diğer bütün değerleri 0) (Bunu henüz görmediniz ama birim matrise benziyor, sadece köşegen değerleri 1 değil 3 olacak. Bir şeyler düşünün)
print(np.eye(3, 3,dtype=int,)*3)
print('\n')
# 10) np.random modülünden uygun fonksiyonu kullanarak 0-1 arasında toplam 6 tane değerden oluşan 1 boyutlu bir array oluşturun.
print(np.random.rand(6))
print('\n')
# 11) np.random modülünden uygun fonksiyonu kullanarak 50-100 arasındaki(50 ve 100 dahil) tam sayılardan 10 tanesiyle oluşan (5,2) shape'inde bir array oluşturun. Ardından bu arrayin shape'ini kontrol edin.
arrRandint = np.random.randint(50,101,(5,2))
print(arrRandint)
print(arrRandint.shape)
print('\n')
# 12) np.random modülünden uygun fonksiyonu kullanarak 100-1000(1000 dahil değil) arasındaki tam sayılardan rastgele 50 tanesinden oluşan (2,5,5) shape'inde 3 boyutlu bir array oluşturun. Ardından bu array'in dimension'ını(boyutunu) ve shape'ini kontrol edin.
arr3random = np.random.randint(100,1000,(2,5,5))
print(arr3random)
print(arr3random.ndim)
print(arr3random.shape)
# 13) np.random modülünden uygun fonksiyonu kullanarak 0-100(0 ve 100 dahil) arasındaki tam sayılardan 10 tane seçerek bir array oluşturun. Bu array'in maximum, mininmum değerlerine ve bu değerlerin indexlerine bakın.
arrmaxmin = np.random.randint(0,100,10)
print(arrmaxmin.max())
print(arrmaxmin.argmax())
print(arrmaxmin.min())
print(arrmaxmin.argmin())
print('\n')
# 14) np.random modülünden uygun fonksiyonu kullanarak 300-500(300 ve 500 dahil) arasındaki tam sayılardan 20 tane seçerek (2,2,5) shape'inde 3 boyutlu bir array oluşturun. Ardından bu array'in içindeki 20 tam sayı arasından maximum ve minimum değerleri manuel olarak tespit edin ve indexleme yaparak çekmeye çalışın.
arrRandom1 = np.random.randint(300,500,20).reshape(2,2,5)
print(arrRandom1)
print(arrRandom1.max())
print(arrRandom1.argmax())
print(arrRandom1.min())
print(arrRandom1.argmin())
print('\n')
# 15) 0-50(50 dahil) arasındaki ardışık tam sayılardan oluşan bir array oluşturun. Ardından bu arrayin 20. ve 35. indexleri arasındaki değerleri 500'e eşitleyin ve yeni oluşan array'i ekrana yazdırarak broadcasting işleminin yapılıp yapılmadığını test edin.
arrArdisik = np.arange(0,50)
arrArdisik[20:35]=500
print(arrArdisik)
