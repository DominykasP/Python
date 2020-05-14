# -*-coding:UTF-8-*-
import numpy as np
import sympy as sp


# Padalinkite intervalą nuo -1.3 iki 2.5 tolygiai į 64 dalis.
def first():
    start = -1.3
    stop = 2.5
    amount = 64
    return np.linspace(start, stop, amount)


# Sugeneruokite masyvą dydžio 3n ir užpildykite jį cikliniu šablonu [1, 2, 3].
def second(n):
    template = np.array([1, 2, 3])
    return np.tile(template, n)


# Sukurkite masyvą iš pirmųjų 10 nelyginių sveikųjų skaičių.
def third():
    return np.arange(1, 20, 2)


# Sukurkite masyvą dydžio 10 x 10 iš nulių ir "įrėminkite" jį vienetais.
def fourth():
    zeros = np.zeros((9, 9))
    return np.pad(zeros, 1, mode='constant', constant_values=(1,))


# Sukurkite masyvą dydžio 8 x 8, kur 1 ir 0 išdėlioti šachmatine tvarka (panaudokite slicing+striding metodą).
def fifth():
    board = np.zeros((8, 8))
    board[::2, ::2] = 1
    board[1::2, 1::2] = 1
    return board


# Sukurkite masyvą dydžio n×n , kurio (i,j)-oji pozicija lygi i+j
def sixth(n):
    arr = np.fromfunction(lambda i, j: i + j, (n, n), dtype=int)
    return arr


# Sukurkite atsitiktinį masyvą dydžio 3×5 naudodami np.random.rand(3, 5) funkciją ir suskaičiuokite: sumą, eilučių sumą, stulpelių sumą.
def seventh():
    arr = np.random.rand(3, 5)
    sum_all = np.sum(arr)
    sum_lines = np.sum(arr, axis=1)
    sum_columns = np.sum(arr, axis=0)
    return sum_all, sum_lines, sum_columns


# Sukurkite atsitiktinį masyvą dydžio 5×5 naudodami np.random.rand(5, 5). Surūšiuokite eilutes pagal antrąjį stulpelį. Tam pamėginkite apjungti masyvo slicing + argsort + indexing metodus.
def eighth():
    arr = np.random.rand(5, 5)
    indexes = np.argsort(arr[:, 1])
    sorted_arr = arr[indexes]
    return arr, sorted_arr


# Atvirkštinę matricą
def ninth():
    matrix = np.array([[4., 7.], [2., 6.]])
    inverted_matrix = np.linalg.inv(matrix)
    return inverted_matrix


# Apskaičiuokite matricos tikrines reikšmes ir tikrinį vektorių
def tenth():
    arr = np.array([[0., 1.], [-2., -3.]])
    return np.linalg.eig(arr)


# Pasirinktos funkcijos išvestinę
def eleventh():
    x = sp.Symbol('x')
    y = 5 + 10*x + x**3
    f = y.diff(x)
    return f


# Pasirinktos funkcijos apibrėžtinį ir neapibrėžtinį integralus
def twelfth():
    x = sp.Symbol('x')
    y = 3*x**2 + 10
    d_indefinite = y.integrate(x)
    d_definite = y.integrate((x, 0, 1))
    return d_indefinite, d_definite


print("-------------------------------------------------------------------------------- First: --------------------------------------------------------------------------------")
print(first())
print("-------------------------------------------------------------------------------- Second: --------------------------------------------------------------------------------")
print(second(2))
print("-------------------------------------------------------------------------------- Third: --------------------------------------------------------------------------------")
print(third())
print("-------------------------------------------------------------------------------- Fourth: --------------------------------------------------------------------------------")
print(fourth())
print("-------------------------------------------------------------------------------- Fifth: --------------------------------------------------------------------------------")
print(fifth())
print("-------------------------------------------------------------------------------- Sixth: --------------------------------------------------------------------------------")
print(sixth(6))
print("-------------------------------------------------------------------------------- Seventh:--------------------------------------------------------------------------------")
print(seventh())
print("-------------------------------------------------------------------------------- Eighth:--------------------------------------------------------------------------------")
print(eighth())
print("-------------------------------------------------------------------------------- Ninth: --------------------------------------------------------------------------------")
print(ninth())
print("-------------------------------------------------------------------------------- Tenth:--------------------------------------------------------------------------------")
print(tenth())
print("-------------------------------------------------------------------------------- Eleventh: --------------------------------------------------------------------------------")
print(eleventh())
print("-------------------------------------------------------------------------------- Twelfth: --------------------------------------------------------------------------------")
print(twelfth())
