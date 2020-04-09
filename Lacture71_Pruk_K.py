menuList = []
priceList = []
def showBill():
    print("----- My Food -----")
    for i in range(len(menuList)):
        print(menuList[i],priceList[i])
def totalPrice():
    sum = 0
    for i in range(len(priceList)):
        sum +=int(priceList[i])
    print("Total price = ",sum)
    
while True:
    menuInput = input("Input Menu ::")
    if menuInput.lower() == "exit":
        break
    else:
        priceInput = input("Input Price ::")
        menuList.append(menuInput)
        priceList.append(priceInput)
showBill()
totalPrice()