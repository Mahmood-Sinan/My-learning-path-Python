# temp=float(input("Enter the temperature: "))
# is_raining = True
# if temp > 35 or temp < 0 or is_raining:
#    print("The event is cancelled")
# else:
#    print("The event is still on")

temp=float(input("Enter the temperature: "))
is_sunny = False
if temp>=28 and is_sunny:
   print("It is hot and sunny outside")
elif temp<=0 and is_sunny:
   print("It is cold and sunnu outside")
elif 0 < temp < 28 and is_sunny:
   print("It is warm and sunny outside")
elif temp>=28 and not is_sunny:
   print("It is hot and cloudy outside")
elif temp<=0 and not is_sunny:
   print("It is cold and cloudy outside")
elif 0 < temp < 28 and not is_sunny:
   print("It is warm and cloudy outside")
