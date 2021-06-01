def main(str1, str2):
    m = len(str1)
    n = len(str2)

    j = 0
    i = 0



    while j < m and i < n:
        if str1[j] == str2[i]:
            j = j+1
        i = i + 1

    return j == m


str2 = str(input())
N = int(input())

for i in range(N):
    str1 = str(input())
    if main(str1, str2):
        print("POSITIVE") 
    else:
        print( "NEGATIVE")