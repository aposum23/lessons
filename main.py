import time

print("Hello world")

for i in range(5000):
    print(i)

arr = []
for i in range(50):
    arr.append("How are you?")

for elem in arr:
    print(elem)

print(time.localtime().tm_year)