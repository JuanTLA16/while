
print("---------------------------------------")
print("--------------EJERCICIO 1--------------")
print("---------------------------------------")

C3 = int(input("Digite el valor de la inversion que desea realizar: " ))
C1 = int(input("Digite el capital que posee Pedro: " ))
C2 = int(input("Digite el capital que posee Juan: " ))


N = 0


while (C1 + C2 < C3 ):
    C1 = C1 + ( 0.03 * C1 ) 
    C2 = C2 + ( 0.04 * C2 )
    N = N + 1


print("Meses que tienen que pasar para hacer el negocio que Pedro y Juan desean:  " + str(N))