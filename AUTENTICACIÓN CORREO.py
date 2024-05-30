correo = "pepito@pito.com"


validos = 0
for i in correo:
    if i == "@":
        validos += 1
    if validos == 1 and i == ".":
        validos += 1

if validos < 2:
    print("CORREO INVALIDO")
else:
    print("CORREO VALIDO")

