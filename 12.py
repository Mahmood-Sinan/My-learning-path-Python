#quiz game

choice = input("Do you want to play a quiz game (Y/N) ? ").upper()
while not (choice == "Y" or choice =="N") :
   choice = input("Enter a valid choice (Y/N): ").upper()
while choice == "Y": 
   questions = ("What is the second element in periodic table?",
               "What is the acceleration due to gravity at the equator in the surface of earth? ",
               "What is the result of additive mixing of red, green and blue colors? ",
               "What is the derivative of f(x) = sinx? ",
               "What is the size of integer in a 32 bit OS? ")

   options = (("A. H","B. He","C. Li","D. Be"),
            ("A. 9.7","B. 9.5","C. 9.81","D. 10"),
            ("A. Black","B. White","C. Green","D. Blue"),
            ("A. sinx","B. cosx","C. tanx","D. secx"),
            ("A. 1 byte","B. 2 byte","C. 3 byte","D. 4 byte"))
   answers = ("B","C","A","B","D")
   guesses = []
   score = 0
   question_no = 0

   for question in questions:
      print("-------------------") 
      print(question)
      for option in options[question_no]:
         print(option)

      guess = input("Enter an option A. B. C. D: ").upper()
      guesses.append(guess)

      if guess == answers[question_no] : 
         print("CORRECT!")
         score += 1
      else : 
         print("INCORRECT!")
         print(f"The correct answer was {answers[question_no]}")

      question_no += 1

   print("guesses: ", end = "")
   for guess in guesses :
      print(guess, end = " ")

   print()

   print("Answers: ",end = "")
   for answer in answers :
      print(answer, end = " ")

   print()
   print("----- RESULTS -----")
   print(f"Your score is {int(score/len(questions) *100)}%")
   print("-------------------")
   choice = input("Do you want to play again (Y/N) ? ").upper()
   while not (choice == "Y" or choice =="N") :
      choice = input("Enter a valid choice (Y/N): ").upper()
   if choice == "N":
      break

print("Thank you for playing! ")