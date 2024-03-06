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
