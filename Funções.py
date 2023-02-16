'''
def fatorial(num = 1):
    f = 1
    for c in range(num,0,-1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f"Os resultados são {f1}, {f2} e {f3}")

'''

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input("Digite um numero: "))
if par(num):
    print("E Par!")
else:
    print("Não é Par")