total_distancia = 0
nombreStr = input("Ingrese su nombre: ")
numero_escalas = int(input("Ingresa el numero de escalas: "))

 
for escala in range(numero_escalas):
    distancia = int(input("ingrese la distancia de las escalas: "))
    total_distancia += distancia
    
print('Nombre', nombreStr) 
print("la distancia total es ", total_distancia)
print('el numero de escalas es', numero_escalas)