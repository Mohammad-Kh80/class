
number = input("please give me a number to calculate 10/x:")
try:
    number = float(number)

except ValueError:
    print('please give me a number not str!')

except ZeroDivisionError:
    print('oh...shet! you give me a zero????? :((((((')

else:
    print(10/number)

#finally:
    #print('done')
