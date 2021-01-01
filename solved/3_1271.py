n, m = map(int, input().split())
money = n // m 
print(money)
rest = n - (money * m)
print(rest)