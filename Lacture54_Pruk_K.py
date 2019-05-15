def login():
    username = input("Username :")
    password = input("Password :")
    if username == "admin" and password == "1234":
        return True
    else:
        return False
def showMenu():
    print("---iShop----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def menuSelect():
    userSelected = int(input(">>"))
    return userSelected
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * (vat/100))
    return result
def priceCalculate():
    price1 = int(input("First Product :"))
    price2 = int(input("Second Product :"))
    return vatCalculate(price1+price2)

if login()== True:
    showMenu()
    select = menuSelect()
    if select == 1:
        print("Price include vat(7%)", vatCalculate(int(input("Product Price :"))), "THB")
    elif select == 2:
        print("Price include vat(7%) :", priceCalculate(), "THB")
else:
    print("User or Password was wrong!!!")
