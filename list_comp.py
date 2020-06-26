xyz = [ i for i in range(5,-1,-1)]
# print(xyz)
x3 = (i for i in range(20))
# print(x3)
# [print(i,ii) for i in x3 for ii in range(20)]

##zip
x = [1, 2, 3, 4]
y = [7, 6, 2, 1]
z = ['a','b','c','d']

for a,b,c in zip(x,y,z):
    print(a,b,c)


d = [ i for  i in x if i in y]
print(d)
e = [ (a,b,c) for a,b,c in zip(x,y,z)]
print(e)