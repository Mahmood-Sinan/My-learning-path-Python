import random

def spin_row():
   symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

   return [random.choice(symbols) for _ in range(3)]

   print(results)
def print_row(row):
   print("*************")
   print(" | ".join(row))
   print("*************")
def get_payout(row, bet):
   if row[0] == row[1] == row[2]:
      if row[0] == "🍒":
         return 1 * bet
      elif row[0] == "🍉":
         return 2 * bet
      elif row[0] == "🍋":
         return 4 * bet
      elif row[0] == "🔔":
         return 8 * bet
      elif row[0] == "⭐":
         return 16 * bet
   return 0
      
def main():
   balance = 100

   print("*************************")
   print("Welcome to Python Slots ")
   print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
   print("*************************")

   while balance > 0:
      print(f"Current balance: ${balance:0.2f}")
      bet = input("Input your bet amout: ")
      if not bet.isdigit():
         print("Please enter a valid amount")
         continue
      bet = int(bet)

      if bet > balance:
         print("Insufficient funds")
         continue
      if bet <= 0:
         print("Bet must be greater than zero")
      
      balance -=bet

      row = spin_row()
      print("Spinning...\n")
      print_row(row)

      payout = get_payout(row,bet)
      
      if payout > 0:
         print(f"You won ${payout:0.2f}")
      else:
         print("Sorry you lost this round")

      balance += payout

      play_again = input("Do you want to spin again? (Y/N): ").upper()

      while not (play_again == "Y" or play_again == "N"):
         print("Enter a valid choice")
         play_again = input("Do you want to spin again? (Y/N): ").upper()

      if play_again == "N":
         break
   
   print("***************************************")
   print(f"Game over! Your final balance is ${balance:0.2f}")
   print("***************************************")

if __name__ == '__main__':
   main()