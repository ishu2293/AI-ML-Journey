class book:
    reviews = []
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []
    def add(self, new_r):
        self.reviews.append(new_r)
    def count(self):
        print(len(self.reviews))
    def display(self):
        print(self.reviews)

b1 = book("Maxton hall", "ishwari")
b1.add("The book is very interesting !!")
b1.add("Book was very engaging")
b1.count()
b1.display()

