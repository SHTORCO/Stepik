# Реализуйте программу, которая будет вычислять количество различных объектов в списке.
# Два объекта a и b считаются различными, если a is b равно False.
objects = [1, 2, 1, 2, 3]
ans = 0
t = []
for obj in objects: # доступная переменная objects
    if obj not in t:
        t.append(obj)
        ans += 1
print(ans)