#punto 2

with open("test_pr2.txt", "r") as archivo:
    contenido = archivo.read()
texto_leido = contenido.split()
texto_convertido = [palabra.lower() for palabra in texto_leido]
print(texto_convertido)
ocurrencia = 'en'
print(texto_convertido.count(ocurrencia))