#punto 1
n = int(input())
valores = []
for i in range(n):
  valores.append(int(input()))


max = 0
for i in range(len(valores)):
  if valores[i] > max:
    max = valores[i]
print("El valor maximo es: ", str(max))

min = 0
for i in range(len(valores)):
  if valores[i] < min:
    min = valores[i]
print("El valor maximo es: ", str(min))



   











"""print("El valor mínimo es: ", min(valores))

print("La suma de lo ingresado es: ", sum(valores))

print("El promedio de lo ingresado es: ", sum(valores)/len(valores))"""