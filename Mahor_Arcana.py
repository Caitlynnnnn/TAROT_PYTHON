List_Major_Arcana = ['Fool', 'Magician', 'High_Priestess', 'Empress', 'Emperor', 'Hierophant', 'Lovers', 'Chariot', 'Strength', 'Hermit', 'Wheel_of_Fortune', 'Justice', 'Hanged_man', 'Death', 'Temperance', 'Devil', 'Tower', 'Star', 'Moon', 'Sun', 'Judgement', 'World']
size = len(List_Major_Arcana)
print(List_Major_Arcana[4])

class Major_Arcana:
    def __init__ (self, Number, name, keywords):
        self.name = name
        self.number = Number
        self.keyword = keywords

Fool = Major_Arcana('00', 'The Fool', 'Beginnings, innocence, spontaneity, a free spirit')
Emperor = Major_Arcana('04', 'The Emperor','Authority, establishment, structure, a father figure' )
print(Fool.number)