List_Major_Arcana = ['Fool', 'Magician', 'High_Priestess', 'Empress', 'Emperor', 'Hierophant', 'Lovers', 'Chariot', 'Strength', 'Hermit', 'Wheel_of_Fortune', 'Justice', 'Hanged_man', 'Death', 'Temperance', 'Devil', 'Tower', 'Star', 'Moon', 'Sun', 'Judgement', 'World']

class Major_Arcana:
    def __init__ (self, Number, name, keywords):
        self.name = name
        self.number = Number
        self.keywords = keywords

Fool = Major_Arcana('00', 'The Fool', 'Beginnings, innocence, spontaneity, a free spirit')
Magician = Major_Arcana('01', 'The Magician', 'Manifestation, resourcefulness, power, inspired action')
High_Priestess = Major_Arcana('02', "The High Priestess", 'Intuition, sacred knowledge, divine feminine, the subconscious mind')
Emperor = Major_Arcana('04', 'The Emperor','Authority, establishment, structure, a father figure' )

print('Do you want to know more about yourself? Enter your birth date to get your Tarot Birth Card!')
print("- What is a Tarot Birth Card?")
print("A Tarot birth card has special relevance to you based on your date of birth. It reflects a central piece of your path and identifies the life lessons you most need to learn.")
print("Step one: Enter your birthday!(numbers only)")
Year = int(input(" Year of Birth: "))
Month = int(input(" Month of Birth: "))
Date = int(input(" Date of Birth: "))

Sum = Year + Month + Date
Str_Sum = str(Sum)
Number = int(Str_Sum[0]) + int(Str_Sum[1]) + int(Str_Sum[2]) + int(Str_Sum[3])
if Number >= len(List_Major_Arcana):
    Str_Fin_Num = str(Number)
    Final_Number = int(Str_Fin_Num[0]) + int(Str_Fin_Num[1])
    print(" Your Number is: ",Final_Number, "The coresponding Tarot Card is:",List_Major_Arcana[Final_Number],'.')
else:
    print("Your Number is: ",Number, "The corresponding Tarot card is: ",List_Major_Arcana[Number],'.')

print("Get more information on your card by entering the name of the Card")
Info_Card= input("Card: ")
if Info_Card == 'Fool':
    print('Card Name:' , Fool.name)
    print('Card Number:', Fool.number)
    print('KeyWords: ', Fool.keywords)
elif Info_Card == 'Magician':
    print('Card Name:', Magician.name)
    print('Card Number: ', Magician.number) 
    print('Keywords: ', Magician.keywords)
else:
    print()






