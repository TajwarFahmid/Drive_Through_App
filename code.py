#
def welcome():
  print("Welcome to McDonald's, what do you want to have today?")

def get_item(x):
  if x == 1:
    print("🍔 Cheeseburger")
  elif x == 2:
    print("🍟 Fries")
  elif x == 3:
    print("🥤 Soda")
  elif x == 4:
    print("🍦 Ice Cream")
  elif x == 5:
    print("🍪 Cookie")
  else:
    print('Order unavailable.')

welcome()
x = int(input("1. 🍔 Cheeseburger \n 2. 🍟 Fries \n 3. 🥤 Soda \n 4. 🍦 Ice Cream \n 5. 🍪 Cookie"))
get_item(1)
