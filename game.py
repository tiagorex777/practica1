import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de intentos permitidos
max_attempts = 10

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
word_displayed = "_" * len(secret_word)


# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

#uso un while en ves de un for con una variable fallos para contar los 10 fallos que tiene el usuario
fallos = 0
while fallos < 10 : 

 # Pedir al jugador que ingrese una letra
 letter = input("Ingresa una letra: ").lower()

 # Verificar si la letra ya ha sido adivinada
 if letter in guessed_letters:
    print("Ya has intentado con esa letra. Intenta con otra.")
    continue

 # Agregar la letra a la lista de letras adivinadas
 guessed_letters.append(letter)

 # Verificar si la letra está en la palabra secreta
 # corrijo con un and que si no se introduce una letra es un error
 if letter in secret_word and letter != "" : 
    print("¡Bien hecho! La letra está en la palabra.")
 else:
    print("Lo siento, la letra no está en la palabra.")
    fallos += 1

 # Mostrar la palabra parcialmente adivinada
 letters = []
 for letter in secret_word:
    if letter in guessed_letters:
        letters.append(letter)
    else:
        letters.append("_")

 word_displayed = "".join(letters)
 print(f"Palabra: {word_displayed}")

 # Verificar si se ha adivinado la palabra completa
 if word_displayed == secret_word:
     print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
     break
else:
 print(f"¡Oh no! Has agotado tus {max_attempts} intentos.")
 print(f"La palabra secreta era: {secret_word}")
