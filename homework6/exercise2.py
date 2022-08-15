my_string = input()
char = input()
start = -1
count = 0
while True:
    start = my_string.find(char, start+1)
    if start == -1:
        break
    count += 1

print(f"Количество вхождений символа в строку: {count}")
