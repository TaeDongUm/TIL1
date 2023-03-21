def solution(s):
    try:
        s=int(s)
        return s
    except:
        print('1111')
        if 'zero' in s:
            s=s.replace('zero','1')
        s=int(s)
        return s
s='1zero23'
solution(s)
print(solution(s))
# word='abcedf'
# word[0]
# print(word[0])
# word1=['4','abcdef']
# print(word1[1][])
