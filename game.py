 
import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

max_attempts = 10

print("¡Bienvenido al juego de adivinanzas!")

#menu whit the diferrents dificulties
print("""En que dificultad desea jugar
      1-Facil
      2-Media                                    
      3-Dificil""")

difficulty = int(input("Ingrese dificultad(1,2 o 3): "))



#lista para almacenar las letras adivinadas
guessed_letters = []

while difficulty < 1 or difficulty > 3:
   print("Dificultad no existente, intente denuevo")
   difficulty = int(input("Ingrese dificultad: "))

print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

#diferrents dificulties
word_displayed = ""
#easy
if difficulty == 1:
   for element in secret_word:
     if element in "aeiou":
       guessed_letters.append(element)   #i keep all the letters the program give me
       word_displayed += element
     else:
       word_displayed += "_"
else:
   #medium
    if difficulty == 2:
     guessed_letters.append(secret_word[0])        
     guessed_letters.append(secret_word[-1])
     for elem in secret_word:   
       if elem in guessed_letters:    #show all the ocurrencies of the first and last letter
        word_displayed += elem
       else:
         word_displayed += "_"
    else: 
     #hard
     if difficulty == 3:
       word_displayed = "_" * len(secret_word)
 

# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")


tries = 0
while tries < 10 :         #change the for whit a while,using a new variable that count the tries

 # Pedir al jugador que ingrese una letra
 letter = input("Ingresa una letra: ").lower()

 # Verificar si la letra ya ha sido adivinada
 if letter in guessed_letters:
   if letter in secret_word:
    print("Ya has intentado con esa letra, es correcta. Intenta con otra.")
   else:
     print("ya has intentado con este letras, es incorrecta. Intenta con otra") 
     tries += 1   #if te user put the same letter two times and it´s a worng letter, count as a try
   continue

 # Agregar la letra a la lista de letras adivinadas
 if letter != "":                                    #fixed if the users enter an empty letter(dont count as a try)
   guessed_letters.append(letter)

 # Verificar si la letra está en la palabra secreta
   if letter in secret_word:
      print("¡Bien hecho! La letra está en la palabra.")
   else:
      print("Lo siento, la letra no está en la palabra.")
      tries += 1          
 else:
    print("caracter invalido, ingrese otro")

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