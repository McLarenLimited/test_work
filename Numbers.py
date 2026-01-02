try:
    n = int(input())
    if n <= 0:
        print("Ошибка: введите положительное целое число")
    else:
        count = 0
        num = 1

        while count < n:
            for _ in range(num):
                if count == n:
                    break
                print(num, end='')
                count += 1
            num += 1

except ValueError:
    print("Ошибка: введены некорректные данные")
