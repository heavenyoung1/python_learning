# Oh shitt, we here going again

from math import sqrt

a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(sqrt(a**10 + b**10))

#Короткое решение

print(*(lambda a, b: (a + b, a - b, a * b, a / b, a // b, a % b, (a ** 10 + b ** 10)** 0.5))(int(input()), int(input())), sep = '\n')

m = float(input())
h = float(input())
bdi = m / (h ** 2)
if (bdi >= 18.5 and bdi <= 25) :
  print('Оптимальная масса')
elif (bdi < 18.5) :
  print('Недостаточная масса')
else:
  print('Избыточная масса')

s = str(input())
rub = (len(s) * 60) // 100
cop = (len(s) * 60) % 100
print(f'{rub} руб. {cop} коп.')

# ЗАДАЧА ИОСИФА ФЛАВЕЛЯ. НУЖНО ЗАПОМНИТЬ, ЗАДАЧА РЕАЛЬНО КРУТАЯ!

def opr(n, k):
  count = 0
  soldiers = [str(n - i) for i in range(n)]
  
  if k == 1:
    return soldiers[0]
  elif k != 1:
    while (len(soldiers) != 1):
      for i in range(len(soldiers)-1, -1, -1):
        count += 1
        if count == k:
          soldiers.pop(i)
          count = 0
    return soldiers[0]

n, k = int(input()), int(input())
print(opr(n, k))

# Программа должна вывести количество точек, лежащих в каждой координатной четверти, как в примерах.

def quadrant(coordinates):
    q1, q2, q3, q4 = 0, 0, 0, 0
    for x, y in coordinates:
        if x > 0 and y > 0:
            q1 += 1
        elif x < 0 and y > 0:
            q2 += 1
        elif x < 0 and y < 0:
            q3 += 1
        elif x > 0 and y < 0:
            q4 += 1
    return q1, q2, q3, q4

n = int(input())
coordinates = [map(int, input().split()) for _ in range(n)]

q1, q2, q3, q4 = quadrant(coordinates)

print(f"""
      Первая четверть: {q1}
      Вторая четверть: {q2}
      Третья четверть: {q3}
      Четвертая четверть: {q4}
""")

# На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел. Напишите программу подсчета количества чисел, которые больше предшествующего им в этом списке числа. 


