#The Minion Game

string = input("Enter Input for minion Game: ")

s = string.upper()

vowels = 'AEIOU'

kevsc = 0
stusc = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevsc += (len(s)-i)
    else:
        stusc += (len(s)-i)

if kevsc > stusc:
    print("Kevin", kevsc)
elif kevsc < stusc:
    print("Stuart", stusc)
else:
    print("Draw")

#****************************************
#Other Way

s =  input("Enter Input for minion Game: ")

string = s.upper()

vw = 'AEIOU'
strl = len(string)
kevin = sum(strl-i for i in range(strl) if string[i] in vw)
stuart = strl*(strl + 1)/2 - kevin

if kevin == stuart:
	print('Draw')
elif kevin > stuart:
	print('Kevin %d' % kevin)
else:
	print('Stuart %d' % stuart)

#****************************************
#OTHER WAY

string = input("Enter Input for minion Game: ")

S = string.upper()
n = len(S)

# consonents
stuart = 0

# vowels
kevin = 0

for i in range(n):
    if S[i] in ('A', 'E', 'I', 'O', 'U'):
        kevin += n - i
        #print("kevin",kevin)
    else:
        stuart += n - i
        #print("stuart",stuart)

if kevin > stuart:
    print('Kevin', kevin)
elif stuart > kevin:
    print('Stuart', stuart)
else:
    print('Draw')