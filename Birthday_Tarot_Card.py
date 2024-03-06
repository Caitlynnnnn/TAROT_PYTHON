List_Major_Arcana = ['Fool', 'Magician', 'High Priestess', 'Empress', 'Emperor', 'Hierophant', 'Lovers', 'Chariot', 'Strength', 'Hermit', 'Wheel of Fortune', 'Justice', 'Hanged Man', 'Death', 'Temperance', 'Devil', 'Tower', 'Star', 'Moon', 'Sun', 'Judgement', 'World']

class Major_Arcana:
    def __init__ (self, Number, name, keywords):
        self.name = name
        self.number = Number
        self.keywords = keywords

Fool = Major_Arcana('0','The Fool','Beginnings, Innocence, Spontaneity, a Free Spirit, and Changes.')
Magician = Major_Arcana('I','The Magician','Manifestation, Resourcefulness, Power, Inspired Action, Communication and Travel.')
High_Priestess = Major_Arcana('II',"The High Priestess",'Intuition, Sacred Knowledge, Divine Feminine, The Subconscious Mind.')
Empress = Major_Arcana('III','The Empress','Femininity,nbeauty, nature, nurturing, abundance, Love, comfort, art, and security' )
Emperor = Major_Arcana('IV','The Emperor','Authority, Establishment, Structure, a Father Figure, and The Leader.' )
Hierophant = Major_Arcana('V','The Hierophant','Order and Rules, Spiritual Wisdom, Religious Beliefs, Conformity, Tradition, and Institutions.')
Lovers = Major_Arcana('VI','The Lover','Love, Harmony, Relationships, Values Alignment, and Choices.')
Chariot = Major_Arcana('VII','The Chariot','Success, Protection, Emotions, Control, Willpower, Action, and Determination.')
Strength = Major_Arcana('VIII','Strength','Strength, Courage, Persuasion, Influence, Compassion, Resilience, Control, and Glory.')
Hermit = Major_Arcana('IX','The Hermit','Analytical thought, Soul-searching, Introspection, Being alone, and Inner guidance.')
Wheel_of_Fortune = Major_Arcana('X','The Wheel of Fortune','Good luck, Karma, Life Cycles, Destiny, a turning point, 	Growth and Wisdom.')
Justice = Major_Arcana('XI', "Justice","Justice, Fairness, Truth, Cause and Effect, Law, and Balance.")
Hanged_Man =Major_Arcana('XII','The Hanged Man','Pause, Surrender, Letting go, New perspectives, Inability to move forward due to illusion, Uncertainty, and Delusion.')
Death = Major_Arcana('XIII','Death','Endings, Change, Transformation, and Transition.')
Temperance = Major_Arcana('XIV', "Temperance",'Balance, Moderation, Patience, Purpose, and Understanding through reason.')
Devil = Major_Arcana('XV','The Devil','Shadow self, Attachment, Addiction, Restriction, Sexuality, Letting go of fear and Moving towards Liberation.')
Tower = Major_Arcana('XVI',"The Tower",'Sudden change, Upheaval, Chaos, Revelation, Awakening, and Arguments.' )
Star = Major_Arcana('XVII','The Star','Hope, Faith, purpose, Renewal, Spirituality, and Humanitarianism.')
Moon = Major_Arcana('XVIII',"The Moon",'Illusion, Fear, Anxiety, Subconscious, Intuition, and Imagination.')
Sun = Major_Arcana('XIX',"The Sun","Positivity, Fun, Warmth, Success, Vitality, Ego and Will.")
Judgement = Major_Arcana('XX',"Judgement",'Judgement, Rebirth, Inner Calling, Absolution, Change, Growth, All efforts to Rebuild and Release.')
World = Major_Arcana('XXI','The World','Completion, Integration, Accomplishment, Travel, and Rewards through completion.' )


print('Do you want to know more about yourself? Enter your birth date to get your Tarot Birth Card!')
print("- What is a Tarot Birth Card?")
print("A Tarot birth card has special relevance to you based on your date of birth. It is a combo of 2-3 major arcana tarot cards that reveal special insights and truths about who you really are and how you journey through life")
print("Step one: Enter your birthday!(Eg: 1 March 2024 > 2024 03 01) ")
Year = input(" Year of Birth: ")
Month = input(" Month of Birth: ")
Date = input(" Date of Birth: ")

Sum = int(Year)+ int(Month) + int(Date)
Str_Sum = str(Sum)

First_Number = int(Str_Sum[0]) + int(Str_Sum[1]) + int(Str_Sum[2]) + int(Str_Sum[3])
Second_Number = int(Year[0]) + int(Year[1]) + int(Year[2]) + int(Year[3]) + int(Month[0]) + int(Month[1]) + int(Date[0]) + int(Date[1])

if Second_Number >= len(List_Major_Arcana):
    Str_Second_number = str(Second_Number)
    Sec_Num_List = [int(Str_Second_number[0]), int(Str_Second_number[1])]
    Sec_Num_List.sort
    Final_Number_2 = int(Sec_Num_List[0])*10 + int(Sec_Num_List[1])
else:
    print()


if First_Number >= len(List_Major_Arcana):
    Str_Fin_Num = str(First_Number)
    Final_Number = int(Str_Fin_Num[0]) + int(Str_Fin_Num[1])
    print(" Your Number is: ",Final_Number, "The coresponding Tarot Card is:",List_Major_Arcana[Final_Number],'.')
else:
    print("Your Number is: ",First_Number, "The corresponding Tarot card is: ",List_Major_Arcana[First_Number],'.')






print("Get more information on your card by entering the name of the Card")
Info_Card= input("Your Birth Tarot Card: ")
if Info_Card == List_Major_Arcana[0]:
    print('Card Name:',Fool.name)
    print('Card Number:',Fool.number)
    print('KeyWords:',Fool.keywords)
elif Info_Card == List_Major_Arcana[1]:
    print('Card Name:', Magician.name)
    print('Card Number:', Magician.number) 
    print('Keywords:', Magician.keywords)
elif Info_Card == List_Major_Arcana[2]:
    print('Card Name:', High_Priestess.name)
    print('Card Number:', High_Priestess.number) 
    print('Keywords:',High_Priestess.keywords)
elif Info_Card == List_Major_Arcana[3]:
    print('Card Name:', Empress.name)
    print('Card Number:', Empress.number) 
    print('Keywords:', Empress.keywords)
elif Info_Card == List_Major_Arcana[4]:
    print('Card Name:', Emperor.name)
    print('Card Number:',Emperor.number) 
    print('Keywords:', Emperor.keywords)
elif Info_Card == List_Major_Arcana[5]:
    print('Card Name:', Hierophant.name)
    print('Card Number:', Hierophant.number) 
    print('Keywords:', Hierophant.keywords)
elif Info_Card == List_Major_Arcana[6]:
    print('Card Name:', Lovers.name)
    print('Card Number:', Lovers.number) 
    print('Keywords:', Lovers.keywords)
elif Info_Card == List_Major_Arcana[7]:
    print('Card Name:', Chariot.name)
    print('Card Number:', Chariot.number) 
    print('Keywords:', Chariot.keywords)
elif Info_Card == List_Major_Arcana[8]:
    print('Card Name:', Strength.name)
    print('Card Number:', Strength.number) 
    print('Keywords:', Strength.keywords)
elif Info_Card == List_Major_Arcana[9]:
    print('Card Name:', Hermit.name)
    print('Card Number:', Hermit.number) 
    print('Keywords:', Hermit.keywords)
elif Info_Card == List_Major_Arcana[10]:
    print('Card Name:', Wheel_of_Fortune.name)
    print('Card Number:', Wheel_of_Fortune.number) 
    print('Keywords:', Wheel_of_Fortune.keywords)
elif Info_Card == List_Major_Arcana[11]:
    print('Card Name:', Justice.name)
    print('Card Number:', Justice.number) 
    print('Keywords:', Justice.keywords)
elif Info_Card == List_Major_Arcana[12]:
    print('Card Name:', Hanged_Man.name)
    print('Card Number:', Hanged_Man.number) 
    print('Keywords:', Hanged_Man.keywords)
elif Info_Card == List_Major_Arcana[13]:
    print('Card Name:', Death.name)
    print('Card Number:', Death.number) 
    print('Keywords:', Death.keywords)
elif Info_Card == List_Major_Arcana[14]:
    print('Card Name:', Temperance.name)
    print('Card Number:', Temperance.number) 
    print('Keywords:', Temperance.keywords)
elif Info_Card == List_Major_Arcana[15]:
    print('Card Name:', Devil.name)
    print('Card Number:', Devil.number) 
    print('Keywords:', Devil.keywords)
elif Info_Card == List_Major_Arcana[16]:
    print('Card Name:', Tower.name)
    print('Card Number:', Tower.number) 
    print('Keywords:', Tower.keywords)
elif Info_Card == List_Major_Arcana[17]:
    print('Card Name:', Star.name)
    print('Card Number:', Star.number) 
    print('Keywords:', Star.keywords)
elif Info_Card == List_Major_Arcana[18]:
    print('Card Name:', Moon.name)
    print('Card Number:', Moon.number) 
    print('Keywords:', Moon.keywords)
elif Info_Card == List_Major_Arcana[19]:
    print('Card Name:', Sun.name)
    print('Card Number:', Sun.number) 
    print('Keywords:', Sun.keywords)
elif Info_Card == List_Major_Arcana[20]:
    print('Card Name:', Judgement.name)
    print('Card Number:', Judgement.number) 
    print('Keywords:', Judgement.keywords)
elif Info_Card == List_Major_Arcana[21]:
    print('Card Name:', World.name)
    print('Card Number:', World.number) 
    print('Keywords:', World.keywords)
else:
    print()






