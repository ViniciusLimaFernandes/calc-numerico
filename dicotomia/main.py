import math

def f(x):
    return (pow(x,2) - 5) #função


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
                print("Valor da raiz: ", round(i_meio, 5), "\n")
                break
            elif f(a) * f(i_meio) < 0:
                b = i_meio
            else: 
                a = i_meio
        print("Valor da raiz: ", round(i_meio, 5), "\n")
        
    else:       
        print("Intervalo não existe", "\n")
        
#valores
calcula_raiz(1,6, 0.01)
calcula_raiz(1,8, 0.01)
calcula_raiz(2,3, 0.01)      
