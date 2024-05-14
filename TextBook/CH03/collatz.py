def collatz(number):
    if number % 2 == 0:
        return int(number / 2)
    else:
        return int(3 * number + 1)

print('整数を入力してください：')
try:
    input_number = int(input())
except ValueError:
    print('エラー')

while input_number != 1:
    input_number = collatz(input_number)
    continue
    print(input_number)
    if input_number == 1:
        break
