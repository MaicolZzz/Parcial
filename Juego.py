import random

class JuegoAdivinarNumero:

    def iniciarJuego(self):
        print("\nBienvenido al juego de adivinar el número.")
        try:
            while True:
                self.maximoRango = int(input("\nIngresa el número máximo del rango: "))
                if self.maximoRango <= 1:
                    print("El rango debe ser mayor que 1. Intenta de nuevo.")
                else:
                    self.numeroAdivinar = random.randint(1, self.maximoRango)
                    self.intentosMaximos = max(1, self.maximoRango // 20)
                    self.intentosRestantes = self.intentosMaximos
                    self.vector = ["falló"] * self.maximoRango
                    self.vector[self.numeroAdivinar - 1] = "acertó"
                    print(f"\nTienes un máximo de {self.intentosMaximos} intentos para adivinar un número entre 1 y {self.maximoRango}.")
                    break
        except ValueError:
            print("Por favor, ingrese un número entero válido")

    def jugar(self):
        while self.intentosRestantes > 0:
            try:
                intento = input(f"\nIntento {self.intentos + 1} (Intentos restantes: {self.intentosRestantes}): ")
                intento = int(intento)

                if intento < 1 or intento > self.maximoRango:
                    print(f"El número debe estar entre 1 y {self.maximoRango}. Intenta de nuevo.")
                    continue

                self.intentos += 1
                self.intentosRestantes -= 1

                if intento == self.numeroAdivinar:
                    print(f"\n¡Felicidades! Has adivinado el número {self.numeroAdivinar} en {self.intentos} intentos.")
                    print(f"Vector de resultado: {self.vector}")
                    break
                elif intento < self.numeroAdivinar:
                    print("El número a adivinar es mayor.")
                else:
                    print("El número a adivinar es menor.")

            except ValueError:
                print("Por favor, ingresa un número entero válido.")
                self.intentos += 1
                self.intentosRestantes -= 1

        if self.intentosRestantes == 0 and self.intentos != self.numeroAdivinar:
            print(f"\nHas agotado todos los intentos. El número era {self.numeroAdivinar}.")
            print(f"Vector de resultado: {self.vector}")

    def __init__(self):
        self.maximoRango = 0
        self.vector = []
        self.intentosMaximos = 0
        self.intentosRestantes = 0
        self.numeroAdivinar = 0
        self.intentos = 0


def main():
    opcion = 99
    while opcion != 0:
        try:
            print("\nBienvenido al juego de adivinar el número.")
            opcion = int(input("Seleccione una opción:\n1. Iniciar juego\n0. Salir\n-> "))
            if opcion == 0:
                print("Gracias por jugar. ¡Hasta la próxima!")
                break
            elif opcion != 1:
                raise ValueError("Error, la opción seleccionada no es válida. Por favor, ingresa 1 para iniciar o 0 para salir.")
            
            juego = JuegoAdivinarNumero()
            juego.iniciarJuego()
            juego.jugar()

        except ValueError as e:
            print("Error:", e)

    main()


