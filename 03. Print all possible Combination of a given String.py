#Print All possible Combination of a given String

# Only for length of 3

a = input("Enter String:- ")
d=[]
d.extend(a)
#Using extend() rather than append()
#when we extend a list with a string using extend
#result :-
#>>> d = []
#>>> d.extend('rudra')
#>>> d
#['r', 'u', 'd', 'r', 'a']

z = len(d)
for i in range(z):
    for j in range(z):
        for k in range(z):
            if(i!=j&j!=k&k!=i):
                print(d[i], d[j], d[k])