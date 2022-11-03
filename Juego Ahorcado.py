from random import choice

palabras = ["programacion", "python", "mascota", "puente", "jirafa", "camara"]
acierto = []
fallos = []
intentos = 6
victorias = 0
fin_del_juego = False


def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letra_unica = len(set(palabra_elegida))
    return palabra_elegida, letra_unica


def pedir_letra():
    letra_elegida = ""
    valida = False
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    while not valida:
        letra_elegida = input("Elige una letra: ").lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            valida = True
        else:
            print("La letra es incorrecta.")
    return letra_elegida


def tablero(palabra_elegida):
    lista_oculta = []
    for letra in palabra_elegida:
        if letra in acierto:
            lista_oculta.append(letra)
        else:
            lista_oculta.append("-")
    print(" ".join(lista_oculta))


def verificar_letra(letra_elegida, palabra_oculta, intentos, similitud):
    fin = False
    if letra_elegida in palabra_oculta and letra_elegida not in acierto:
        acierto.append(letra_elegida)
        similitud +=1
    elif letra_elegida in palabra_oculta and letra_elegida in acierto:
        print("Esta letra ya ha sido elegida, intente con otra letra")
    else:
        fallos.append(letra_elegida)
        intentos -= 1

    if intentos == 0:
        fin = derrota()
    elif similitud == letra_unica:
        fin = ganar(palabra_oculta)

    return intentos, fin, similitud


def derrota():
    print("Has perdido, la palabra era: " + palabra)
    return True


def ganar(respuesta):
    tablero(respuesta)
    print("Felicidades, has ganado.")
    return True


palabra, letra_unica = elegir_palabra(palabras)

while not fin_del_juego:
    print("\n")
    tablero(palabra)
    print("\n")
    print("Letras que no forman parte de la plabra: " + "-".join(fallos))
    print(f"te quedan: {intentos}")
    letra = pedir_letra()
    intentos, terminado, victorias = verificar_letra(letra, palabra, intentos, victorias)
    fin_del_juego = terminado
