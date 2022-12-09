#python 3 code
n_max = 150 #Numero maximo de resistores na associacao
cnt = 0
print ("======= Calculo de associacao de resistores =========")
value = (float)(input("valor do resistor fixo: "))
obj_value = (float)(input("Valor do resistor desejado: "))
obj_err = (float)(input("Maximo erro da resistencia: "))

print ("**********************************************************************")
print("")
for p in range(1,n_max):
    for s2 in range(1,n_max):
        for s1 in range(1,n_max):
            n=s1*s2*p
            if(n <= n_max):
                res = ((value * s1)/p)*s2
                error = abs(obj_value - res)            
                if error < obj_err:
                    print ("Valor: %.3f, Erro = %.3f, N = %i, s1 = %i, s2 = %i,0 p = %i" %(res,error,n,s1,s2,p))
                    cnt = cnt + 1
print("")
print ("**********************************************************************")
print ("Combinacoes possiveis: %i" %(cnt))
print("")
print("")