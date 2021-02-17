dic_16  = {
    'A':'10',
    'B':'11',
    'C':'12',
    'D':'13',
    'E':'14',
    'F':'15'
}
n_16 = input('16진수를 입력하세요: ')
listed_n = list(n_16)
# 문자열이 dic_16에 있으면 해당하는 숫자로 바꿔주는 함수
def cvter(n):
    if n in dic_16:
        n = dic_16[n]
    else:
        pass
    return int(n)
hap = 0
for i in range(1,len(listed_n)+1):
    idx = -i
    a = -(idx+1)
    n = cvter(listed_n[idx])
    num = n*16**a
    hap += num
print(hap)

# print(int(input(), 16))