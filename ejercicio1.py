#punto 1
n = int(input())
valores = []
for i in range(n):
  valores.append(int(input()))

print("El valor maximo es: ", max(valores))

print("El valor mínimo es: ", min(valores))

print("La suma de lo ingresado es: ", sum(valores))

print("El promedio de lo ingresado es: ", sum(valores)/len(valores))