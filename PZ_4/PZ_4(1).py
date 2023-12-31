"""Дано целое число N (> 1). Вывести наибольшее из целых чисел K, для которых сумма
 1 + 2 + ... + K будет меньше или равна N, и саму эту сумму."""
N = int(input("Введите целое число > 1: "))
if N <= 1:
    print("Нужно ввести число больше 1")
else:
    K = 0
    summa = 0
    while summa + K + 1 <= N:    # Цикл, сравнивающий сложение переменных с N
        K += 1
        summa += K     # Переменная складывается с K, чтобы узнать сумму чисел арифметической прогрессии
    print("Наибольшее К =", K, "Сумма =", summa)
