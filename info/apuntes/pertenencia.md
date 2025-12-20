OPERADORES DE PERTENENCIA: Se usan para verificar si un valor o variable se encuentra dentro de una 
                            secuencia: (string, list, tuple, set, or dictionary)
                            1) in
                            2) not in

EJEMPLOS: 

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
   print(f"There is a {letter}")
else:
   print(f"{letter} was not found")          

---------------------------------------------------------------------------------------------------------- 

students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter the name of a student: ")

if student in students:
   print(f"{student} is in this class")
else:
   print(f"{student} is NOT in this class")

----------------------------------------------------------------------------------------------------------

