def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice*0.07)
    return result
print("Price include vat(7%) ::",vatCalculate(int(input("Input Price ::"))), "THB")