import math

# a = float(input("Digite o valor de a: "))
# b = float(input("Digite o valor de b: "))
# e = float(input("Digite o valor da precisão(e): "))
def f(x):
    return (pow(x,2) - 5) #função trabalhada na sala


def verifica_intervalo(a,b):
    y = False
    if f(a) * f(b) < 0:
        y = True
    return y
    
def calcula_raiz(a, b, e):
    i_meio = 0

    if (verifica_intervalo(a,b)) == True:
        while (math.fabs(b-a)/2 >= e):
            i_meio = (a+b)/2
            if f(i_meio) == 0:
                print("************************")
                print("Valor da raiz: ", round(i_meio, 5))
                print("************************")
                break
            elif f(a) * f(i_meio) < 0:
                b = i_meio
            else: 
                a = i_meio
        print("************************")
        print("Valor da raiz: ", round(i_meio, 5))
        print("************************")
        
    else:
        print("************************")       
        print("Intervalo não existe")
        print("************************")
        
#valores
calcula_raiz(1,6, 0.01)
calcula_raiz(1,8, 0.01)
calcula_raiz(2,3, 0.01)      
calcula_raiz(4,6, 0.01) 
