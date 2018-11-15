#Main Function
def __init__():
    print("What type of conversion do you want to perform ?")
    print("1. Roman to Decimal")
    print("2. Deciman to Roman")
    choice = input("Enter your choice :")
    convert(choice)

#Conversion Function
def convert(choice):
    
    if((int(choice)) == 1):
       decimal()
    elif((int(choice)) == 2):
        roman()
    else:
        print("Invalid Choice")

#Roman to Decimal
def decimal():
    number = input("Enter the Roman Numeral : ")
    number = number.upper()
    digits = 0
    for i in range(0,len(number)):
        try:
            if number[i] == 'M':
                digits = digits + 1000
            elif number[i] == 'C':
                try:
                    if number[i+1] == 'M':
                        digits = digits + 900 - 1000
                        i = i + 1
                    elif number[i+1] == 'D':
                        digits = digits + 400 - 500
                        i = i + 1
                    else :
                        digits = digits + 100
                except:
                    digits = digits + 100
            elif number[i] == 'D':
                digits = 500
            elif number[i] == 'X':
                try:
                    if number[i+1] == 'C':
                        digits = digits + 90 - 100
                        i = i + 1
                    elif number[i+1] == 'L':
                        i = i + 1
                        digits = digits + 40 - 50
                    else : 
                        digits = digits + 10
                except:
                    digits = digits + 10
            elif number[i] == 'L':
                digits = digits + 50
            elif number[i] == 'I':
                try:
                    if number[i+1] == 'X':
                        i = i+1
                        digits = digits + 9 - 10
                    elif number[i+1] == 'V':
                        i = i + 1
                        digits = digits + 4 - 5
                    else:
                        digits = digits + 1 
                except:
                    digits = digits + 1
            elif number[i] == 'V':
                digits = digits + 5
        except:
            None
    print(str(number) + " = " + str(digits))

#Decimal to Roman
def roman():
    number = input("Enter the Decimal Number : ")
    number = int(number)
    digits = list()
    while number > 0:
        if number >= 1000:
            digits.append('M')
            number = number - 1000
        elif number < 1000 and number >= 900 :
            digits.append('C')
            digits.append('M')
            number = number - 900
        elif number < 900 and number >= 500 :
            digits.append('D')
            number = number - 500
        elif number < 500 and number >= 400:
            digits.append('C')
            digits.append('D')
            number = number - 400
        elif number < 400 and number >=100 :
            digits.append('C')
            number = number - 100
        elif number < 100 and number >= 90 :
            digits.append('X')
            digits.append('C')
            number = number - 90
        elif number < 90 and number >= 50 :
            digits.append('L')
            number = number - 50
        elif number < 50 and number >= 40 :
            digits.append('X')
            digits.append('L')
            number = number - 40
        elif number < 40 and number >= 10 :
            digits.append('X')
            number = number - 10
        elif number < 10 and number >= 9 :
            digits.append('I')
            digits.append('X')
            number = number - 9
        elif number < 9 and number >= 5 :
            digits.append('V')
            number = number - 5
        elif number == 4 :
            digits.append('I')
            digits.append('V')
            number = number - 4
        elif number < 4 and number >=1:
            digits.append('I')
            number = number - 1
        else:
            print("Umm, I guess there's some error.")
        
    print("".join(digits))

    

__init__()

