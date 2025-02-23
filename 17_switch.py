num = 4
match num:
   case 1:
      print("It is 1")
   case 2:
      print("It is 2")
   case 3 | 4:
      print("It is 3 or 4")
   case _:
      print("It is greater than 4")
      