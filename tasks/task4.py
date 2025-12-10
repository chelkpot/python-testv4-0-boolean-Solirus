# tasks/task4.py

def solve():
# Ниже пишите решение задачи
a, b, c = 3, 4, 5
result = (a + b > c) and (a + c > b) and (b + c > a)
print(result)

a, b, c = 2, 2, 5
result = (a + b > c) and (a + c > b) and (b + c > a)
print(result)
    

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()