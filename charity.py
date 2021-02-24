def charitydouble1():
  money1 = float(input("How much money did friend 1 raise? "))
  money2 = float(input("How much money did friend 2 raise? "))
  money3 = float(input("How much money did friend 3 raise? "))
  moneyRaised = money1 + money2 + money3
  if moneyRaised < 1000:
    print ("In total, you raised: £", moneyRaised)
  else:
    totalMoney = moneyRaised*2
    print ("You raised: £", moneyRaised)
    print ("However, a local company has doubled that to £", totalMoney)
  print ("Thank you for your contribution!")

  
def charitydouble2():
  money1 = float(input("How much money did friend 1 raise? "))
  money2 = float(input("How much money did friend 2 raise? "))
  money3 = float(input("How much money did friend 3 raise? "))
  moneyRaised = money1 + money2 + money3
  if moneyRaised < 1000:
    totalMoney = moneyRaised + 100
    print ("You raised:", moneyRaised)
    print ("However, a local company decided to donate £100"), 
    print ("In total you raised £", totalMoney)
  elif 1000 <= moneyRaised <= 2000:
    doubleMoney = moneyRaised * 2
    print ("You raised: £", moneyRaised)
    print ("However, a local company has doubled that to £", doubleMoney)
  else:
    extra = moneyRaised - 2000
    newMoney = 2000*2 + extra
    print ("You raised: £", moneyRaised)
    print ("However, a local company raised that to £", newMoney)
  print ("Thank you for your contribution!")

  
def integerValidation():
  valid = False
  while valid == False:
    try:
      menuChoice = int(input("Which program would you like to use?: "))
      if 1 > menuChoice or menuChoice > 2:
        print ("Please enter either 1 or 2.")
        valid = False
      else:
        valid = True
        return menuChoice
    except ValueError:
      print ("Please enter a number.")

      
def menuSystem():
  exit = False
  while exit == False:
    print("Welcome to Lucy's python charity program")
    print("1 = Charity 1")
    print("2 = Charity 2")
    menuChoice = integerValidation()
    if menuChoice == 1:
      charitydouble1()
    elif menuChoice == 2:
      charitydouble2()
    else:
      print("Invalid option. Please enter another choice.")
      exit = True
      
menuSystem() 
