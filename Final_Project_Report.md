Version 1

```python
print('Do you want to know more about yourself? Follow the following steps to get your Tarot Birth card!')
print("Step one: Enter your birthday!")
Year = int(input(" Birth Year: "))
Month = int(input(" Birth Month: "))
Date = int(input(" Birth Day: "))

Sum = Year + Month + Date
print(  "The Sum of your birthday: ", Sum)

print('Step two: get your number by adding the 4 digits of the sum of your birthday.')
Di_1 = int(input("First digit: "))
Di_2 = int(input("Second digit: "))
Di_3 = int(input("Third Digit: "))
Di_4 = int(input("Fourth Digit: "))

Number = int(Di_1) + int(Di_2) + int(Di_3) + int(Di_4)
if Number > 22:
    print(Number)
    print( "Step 3: please add the integer untill the final number is small than 22")
    Di_5 = int(input( "First digit: "))
    Di_6 = int(input( "Second digit: " ))
    Final_Number = Di_5 + Di_6
    print(" Your Number is: " , Final_Number, "The coresponding Tarot Card is:", List_Major_Arcana[Final_Number] )
else:
    print("Your Number is: ", Number, "The corresponding card is: ", List_Major_Arcana[Number])

---
Do you want to know more about yourself? Follow the following steps to get your Tarot Birth card!
Step one: Enter your birthday!
 Birth Year: 1999
 Birth Month: 1
 Birth Day: 11
The Sum of your birthday:  2011
Step two: get your number by adding the 4 digits of the sum of your birthday.
First digit: 2
Second digit: 0
Third Digit: 1
Fourth Digit: 1
Your Number is:  4 The corresponding card is:  Emperor

```

Version 2
```python
Sum = Year + Month + Date
Str_Sum = str(Sum)

Di_1 = Str_Sum[0]
Di_2 = Str_Sum[1]
Di_3 = Str_Sum[2]
Di_4 = Str_Sum[3]
       
Number = int(Di_1) + int(Di_2) + int(Di_3) + int(Di_4)
if Number > 22:
    Str_Num = str(Number)
    Di_5 = Str_Num[0]
    Di_6 = Str_Num[1]
    Final_Number = int(Di_5) + int(Di_6)
    print(" Your Number is: " , Final_Number, "The coresponding Tarot Card is:", List_Major_Arcana[Final_Number] )
else:
    print("Your Number is: ", Number, "The corresponding card is: ", List_Major_Arcana[Number])
--
Enter your birthday!
 Birth Year: 1973
 Birth Month: 10
 Birth Day: 12
 Your Number is:  6 The coresponding Tarot Card is: Lovers
```

Version 3
```Python
Year = int(input(" Birth Year: "))
Month = int(input(" Birth Month: "))
Date = int(input(" Birth Day: "))

Sum = Year + Month + Date
Str_Sum = str(Sum)
       
Number = int(Str_Sum[0]) + int(Str_Sum[1]) + int(Str_Sum[2]) + int(Str_Sum[3])
if Number > 22:
    Str_Fin_Num = str(Number)
    Final_Number = int(Str_Fin_Num[0]) + int(Str_Fin_Num[1])
    print(" Your Number is: ", Final_Number, "The coresponding Tarot Card is:", List_Major_Arcana[Final_Number] )
else:
    print("Your Number is: ", Number, "The corresponding card is: ", List_Major_Arcana[Number])
--
Birth Year: 1973
 Birth Month: 10
 Birth Day: 13
 Your Number is:  7 The coresponding Tarot Card is: Chariot
 ```


           
