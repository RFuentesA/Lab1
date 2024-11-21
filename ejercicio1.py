#punto 1
n = int(input("Ingrese la cantidad maxima de valores que quiera: "))
valores = []
for i in range(n):
  valores.append(int(input("Ingresa un numero: ")))


max = 0
min = 0
for i in range(n):
  if valores[i] > max:
    max = valores[i]

x = max
for j in range(n):
  if valores[j] < x:
    min = valores[j]
    x = valores[j]
  else:
    min = x

suma = 0
for h in range(n):
  suma += valores[h]

promedio = suma/len(valores)


print("El valor maximo es: ", str(max))
print("El valor minimo es: ", str(min))
print("La suma de todos los valores es: ", suma)
print("El promedio es: ", promedio)








   











"""print("El valor mínimo es: ", min(valores))

print("La suma de lo ingresado es: ", sum(valores))

print("El promedio de lo ingresado es: ", sum(valores)/len(valores))"""