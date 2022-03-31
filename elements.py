import pickle

def save_object(element, file):
    pickle.dump(element, file)

def load_object(file):
    pickle.load(file)



elements = [
    ('komórka', ),
    ('pomidor',),
    ('krzesło',),
    ('bluzka',),
    ('ryż',),
    ('chleb',),
    ('buty',),
    ('mleko',),
    ()
]


# Podstawowa klasa każdego obiektu w programie
class Object:
    """Podstawowy element składowy"""

    # Jednostki miar
    unit_of_measure = {
        'length': ('mm', 'cm', 'dm', 'm', 'km', 'mil'), 
        'weight': ('g', 'dag', 'kg', 't'), 
        'volume': ('m2', 'ml', 'l', 'hl')
    }

    def __init__(self, code, name='Obiekt', quantity=(1, 'szt')):

        self.code = code # numer identyfikacji
        self.name = name # nazwa
        self.quantity = quantity # ilość
        self.category = "" # lista kategori do wyboru
        self.describe = "" # krótka charakterystyka
        self.length = (1, 'cm') # długość
        self.width = (1, 'cm') # szerokość
        self.height = (1, 'cm') # wysokość
        self.weight = (1, 'kg') # waga
        self.volume = (1, 'm2') # ogjętość
        self.value = 0 # wartość

    def __str__(self):
        return f"{self.__class__.__name__}('{self.name}', 'code - {self.code}', '{self.quantity[0]} {self.quantity[1]}')"

    # Pełny opis obiektu    
    def parameters(self):
        return f"""
        Name: {self.name};
        Code: {self.code};
        Quantity: {self.quantity};
        Category: {self.category};
        Describe: {self.describe};
        Dimensions: {self.length} x {self.width} x {self.height};
        Weight: {self.weight};
        Volume: {self.volume};
        Value: {self.value};
        """




# Rodzaje obiektów 'Kategorie'

"""
Categorie
# Food : 
owoce
warzywa
nabiał
suche
ryby
mięso
mrożonki
pieczywo
alkohole
przyprawy
słodycze
napoje
tłuszcze
# Tekstylia :

# Pojazdy :

# Książki :

# Muzyka :

# Filmy :


"""




# "Kontener" - obiekt zawierający listę obiektów
class Container(Object):
    """Pojemnik gromadzący obiekty"""

    elements = [] # Lista elementów
    
    def __init__(self, code, name='Container', capacity=(1, 'szt')):
        super(Container, self).__init__(code, name)

        self.capacity = capacity # Pojemność
        self.max_weight = (1, 'kg') # Maksymalna waga łączna

    def __str__(self):
        return f"{self.__class__.__name__}('{self.name}', 'code - {self.code}', '{self.capacity[0]} {self.capacity[1]}')"

    def addElement(self, element):
        Container.elements.append(element)

    def subElement(self, element):
        try:
            elements.remove(element)
        except ValueError:
            return "Brak danego elementu na liście obiektów"
    
    def showElements(self):
        return [f"{element.name}" for element in self.elements]


    def popElement(self, element):
        try:
            thing = elements.pop(elements.index(element))
            return thing
        except IndexError:
            return "Lista jest pusta lub index poza zakresem"

      

# Rodzaje elementów Kontynera :

"""Container :
półka
szuflada
regał
skrzynia
kontyner
plecak
kieszeń
pudło
torba
walizka
szafka
lodówka
szafa
dom
garaż

"""

###################################
mobilefon = Object(name='Nokia 3310i', code=1, quantity=(1, 'szt'))
pomidor = Object(name='Pomidor', code=3, quantity=(1, 'kg'))
print(mobilefon)

backpack = Container(name='Backpack', code=2, capacity=(25, 'l'))
backpack.weight = (25, 'kg')
print(backpack)

# print(backpack.parameters())
# print(mobilefon.parameters())

backpack.addElement(mobilefon)
backpack.addElement(pomidor)

# x = backpack.showElements()
print(backpack.showElements())
# print([f"{n.name} - {n.quantity[0]} {n.quantity[1]}" for n in x])


