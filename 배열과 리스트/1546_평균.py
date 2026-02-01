n = input()
numbers = list(map(int, input().split()))
max_score = max(numbers)
total = 0

for i in numbers:
    total += i 

print(total / max_score * 100 / int(n))