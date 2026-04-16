# actualizarValores

matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# Cambios
matriz[1][0] = 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
ciudades["México"][2] = "Monterrey"
coordenadas[0]["latitud"] = 9.9355431

# Ver resultados
print("RESULTADOS ACTUALIZADOS")
print(matriz)
print(cantantes)
print(ciudades)
print(coordenadas)

print("\n-\n")


#iterarDiccionario
def iterarDiccionario(lista):
    for dic in lista:
        texto = ", ".join(f"{clave} - {valor}" for clave, valor in dic.items())
        print(texto)


# iterarDiccionario2
def iterarDiccionario2(llave, lista):
    for dic in lista:
        print(dic.get(llave, "No existe"))


# imprimirInformacion

def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for elemento in lista:
            print(elemento)
        print()


#prueba de funciones

print(" iterarDiccionario")
cantantes_test = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes_test)

print("\n iterarDiccionario2 (nombre)")
iterarDiccionario2("nombre", cantantes_test)

print("\n iterarDiccionario2 (pais)")
iterarDiccionario2("pais", cantantes_test)

print("\n iterarDiccionario2 (ciudades)")
iterarDiccionario2("ciudades", cantantes_test)

print("\n imprimirInformacion")
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}