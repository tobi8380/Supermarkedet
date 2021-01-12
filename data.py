from random import randint
import csv

class Employee:

    def __init__(self):
        self.name = ""
        self.position = ""
        self.wage = randint(500,600)

class Transaction:

    def __init__(self, book_data):
        self.id = -1
        self.items = []
        #Status:
        # 0: Indkøb
        # 1: Bestilt
        # 2: Betalt
        self.status = 0
        self.book_data = book_data

    def add_item(self, id):
        self.items.append(id)

    def finalize(self):
        self.status = 2

    def get_amount(self):
        val = 0
        for id in self.items:
            b = self.book_data.get_book(id)
            val += b.pris
        return val


class Book:

    def __init__(self):
        self.titel = ""
        self.forfatter = ""
        self.aarstal = 0
        #[1 stjerne, 2 stjerner, 3 stjerner...]
        self.ratings = [0,0,0,0,0]
        self.id = -1
        self.pris = randint(50,400)

    def get_rating(self):
        r = 0
        total = 0
        for i in range(0,len(self.ratings)):
            r += (i+1)*self.ratings[i]

        return r/sum(self.ratings)

    def give_rating(self, r):
        if 0 <= r <= 5:
            self.ratings[int(r)-1] += 1
        else:
            print("Fejl, rating er ikke gyldig")


class Books_data:

    def __init__(self, samples = False):
        '''
        Variablen samples bestemmer om alle bøger skal indlæses,
        eller kun en lille del.
        '''
        if samples:
            infile = open('data/samples/books.csv', mode='r', encoding="utf8")
        else:
            infile = open('data/books.csv', mode='r', encoding="utf8")
        reader = csv.DictReader(infile)

        self.books = []
        for book in reader:
            b = Book()
            try:
                b.titel = book["title"]
                b.ratings[0] = int(book["ratings_1"])
                b.ratings[1] = int(book["ratings_2"])
                b.ratings[2] = int(book["ratings_3"])
                b.ratings[3] = int(book["ratings_4"])
                b.ratings[4] = int(book["ratings_5"])
                b.aarstal = book["original_publication_year"]
                b.forfatter = book["authors"]
                b.id = int(book['book_id'])
            except:
                print(book)

            self.books.append(b)
        print("Indlæst {} bøger".format(len(self.books)))

        #Lidt penge til at starte med
        self.money = 100000
        #En enkelt ansat i butikken
        self.ansatte = []
        self.ansatte.append(Employee())

        self.transactions = []

    def add_transaction(self, t):
        self.transactions.append(t)

    def get_transaction(self, id):
        r = None
        for t in self.transactions:
            if t.id == id:
                r = t
        return r

    def create_new_transaction(self):
        if len(self.transactions) > 0:
            t = max(self.transactions, key = lambda t: t.id)
            id = t.id + 1
        else:
            id = 1
        t = Transaction(self)
        t.id = id
        self.transactions.append(t)
        return t

    def ansaet(self):
        self.ansatte.append(Employee())

    def fyr(self):
        a = randint(0,len(self.ansatte)-1)
        self.ansatte.pop(a)

    def indtaegt(self, amount):
        #(Opgave 3)
        #Her skal pengene sættes ind på kontoen
        self.money += amount

    def udbetal_loen(self):
        #(Opgave 3)
        #Her skal programmet løbe gennem listen af ansatte
        #og udregne deres samlede løn. Pengene skal trækkes fra self.money
        #Beløbet returneres til sidst, så det kan vises i konsollen.
        amount = 0
        for a in self.ansatte:
            amount += a.wage
        self.money -= amount
        return amount

    def sorter(self, felt):
        if felt == "titel":
            self.books.sort(key=lambda x:x.titel)
        elif felt == "forfatter":
            self.books.sort(key=lambda x:x.forfatter)
        elif felt == "aarstal":
            self.books.sort(key=lambda x:str(x.aarstal))
        elif felt == "rating":
            self.books.sort(key=lambda x:x.get_rating())
        elif felt == "id":
            self.books.sort(key=lambda x:x.id)

    def get_book_list(self, n=0):
        '''
        Returnerer en liste med n bøger.
        '''
        self.sorter("id")
        if n > 0:
            n = min(n, len(self.books)-1)
            n = len(self.books)-1
        return self.books[0:n]

    def slet_bog(self, b):
        '''
        Slet en bog med et bestemt id
        '''
        for book in self.books:
            if book.id == b.id:
                self.books.remove(book)

    def get_book(self, id):
        '''
        find en bog med et bestemt id
        '''
        book = None
        for b in self.books:
            if b.id == id:
                book = b
        return book

    def update_book(self, b):
        '''
        Opdater oplysningerne om en bog
        '''
        for book in self.books:
            if book.id == b.id:
                book.forfatter = b.forfatter
                book.titel = b.titel
                book.aarstal = b.aarstal
