

Num=int(input('Escribe un numero entero no negativo para calcular su factorial: '))
if Num==0 or Num==1:
    print("1")
elif Num<0:
    print('Factorial no definido para negativos')
    
else:
    res=1
    x=1
    for n in range(x, Num+1):
        res=res*x
        x=x+1
        
    print(res)
