import random
print("Esto es un simulador de ruleta rusa. Se gira el tambor del revólver en cada ronda. Es un revólver de 6 balas. "
      "Puedes utilizarlo como juego, aunque está pensado con un fin experimental para comprobar si realmente tiene "
      "ventaja el primero en empezar (A).\nPara esto tienes 3 modos: Automático, que no para de hacer pruebas muy rápido"
      "para ese fin más estadístico, semiautomático, que hace 500 rondas casi instantáneamente y lo para hasta que le"
      "des a enter. El modo manual es un modo para jugar, te da las mismas estadísticas, pero va parándose en cada ronda")
i = 0
vic_a = 0
vic_b = 0
vic = 0
def auto():
    global i
    global vic_a
    global vic_b
    global vic
    n = random.randint(0, 6)
    if n == 1:
        if i % 2 == 0:
            vic_a += 1
            print("Gana A")
        else:
            vic_b += 1
            print("Gana B")
    else:
        print("No gana nadie")
    i += 1
    if vic_a > 0 or vic_b > 0:
        vic = vic_a + vic_b
    else:
        vic = 1
    print("Las victorias de A son: ", vic_a, " es decir, un ", (vic_a / vic) * 100, "%")
    print("Las victorias de B son: ", vic_b, " es decir, un ", (vic_b / vic) * 100, "%")
    print("Van ", i, " rondas")
def semi():
    for i in range(500):
        auto()
    input()
def manual():
    auto()
    input()
while True:
    modo = input("¿Manual, automático, o semiautomático? M/A/S\n")
    if modo == "M" or modo == "m":
        while True:
            manual()
    elif modo == "S" or modo == "s":
        while True:
            semi()
    elif modo == "A" or modo == "a":
        while True:
            auto()
    else:
        print("Introducción inválida")