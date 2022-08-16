from operator import index
print ('Digite 5 valores')

lis = [int(input()),int(input()),int(input()),int(input()),int(input())]


print ('O maior valor digitado foi ', max(lis),'e o menor foi', min(lis))
print ('E estão na posição ',lis.index(max(lis)),'e', lis.index(min(lis)))