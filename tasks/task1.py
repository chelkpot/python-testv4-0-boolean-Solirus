# tasks/task1.py

def solve():
# Ниже пишите решение задачи
numbers = "5 5 5"
a, b, c = map(int, numbers.split())
result = a == b == c
print(result)

numbers = "4 5 6"
a, b, c = map(int, numbers.split())
result = a == b == c
print(result)
    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()