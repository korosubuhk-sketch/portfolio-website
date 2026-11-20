def analizar_password(password: str) -> str:
    contador = 0
    longitud = len(password)
    mayusculas = any(c.isupper() for c in password)
    minusculas = any(c.islower() for c in password)
    numeros = any(c.isdigit() for c in password)
    simbolo = any(not c.isalnum() for c in password)
    
    contador = sum([mayusculas, minusculas, numeros, simbolo])
    print(f"longitud: {longitud}")
    print(f"Tiene mayusculas: {mayusculas}")
    print(f"Tiene minusculas: {minusculas}")
    print(f"Tiene numeros: {numeros}")
    print(f"Tiene simbolos: {simbolo}")
     
    if longitud < 8 or contador == 1:
        return "Fortaleza: Debil"
    if longitud >= 8 and contador <= 3:
            return "Fortaleza: Media"
    if longitud >= 12 and contador == 4:
            return "Fortaleza: Fuerte"
while True:     
    password = input("Escriba su password: ")
    resultado = analizar_password(password)
    print(resultado)
    if resultado == "Fortaleza: Debil":
        print("Intentelo de nuevo \n")
    else:
        break
        
    
    