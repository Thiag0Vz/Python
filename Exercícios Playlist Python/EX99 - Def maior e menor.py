from copy import copy, deepcopy
r = ''
ls = []

def maior(* n):
   print(f'Foram informados {len(n)} valores')
   ls = list(n)
   print (f'O maior valor informado foi {max(ls)}')
   print ('='*30)

maior(6,9,1,8)
maior (3,5,2)
maior(1)