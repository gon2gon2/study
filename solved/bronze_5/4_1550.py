n_16 = input("16진수 입력")
dic_16 = {'A': '10', 'B':'11', 'C':'12','D':'13','E':'14','F':'15'}
n_16 = list(n_16)
n_10 = []
for n in n_16:
    if n in dic_16:
        n_10.append(dic_16[n])
    else:
        n_10.append(n)
N = 0
for idx in range(len(n_10)):
    N += int(n_10[idx]) * 16 **idx
print(N)
# 숫자가 13 이런거를 위한 로직이 없다