# 9. Create a Book class where price is private and cannot be negative.
class Book:
    def __init__(self, title, price):
        self.title = title
        self.__price = 0  
        self.set_price(price)  

    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("Price cannot be negative.")

    def get_price(self):
        return self.__price
book = Book("Python", 29)
print(f"Book Title: {book.title}")
print(f"Book Price: {book.get_price()}")