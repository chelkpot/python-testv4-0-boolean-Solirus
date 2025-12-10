# tasks/task6.py

def solve():
# Ниже пишите решение задачи
a, b, c = 8, 6, 10
a2, b2, c2 = a*a, b*b, c*c
result = (a2 + b2 == c2) or (a2 + c2 == b2) or (b2 + c2 == a2)
print(result)

a, b, c = 5, 6, 5
a2, b2, c2 = a*a, b*b, c*c
result = (a2 + b2 == c2) or (a2 + c2 == b2) or (b2 + c2 == a2)
print(result)
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()