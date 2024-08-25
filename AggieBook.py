# John Sampson
# 11-29-2023
# COMP 163-003
# Classifying textbooks by creating an AggieBook object
import string


def init():  # sets the categories of books in aggieCategories
    AggieBook.aggieCategories = {0: "Unknown", 1: "Biology", 2: "Physics", 3: "Computer Science"}


class AggieBook:
    stateTax = 0.07
    fedTax = 0.1
    aggieCategories = {}  # the categories of books, to be filled by init()

    def __init__(self, title="TBD", date="TBD", category=0, price=0.0):  # initializing the AggieBook object
        self.title = title  # default values are there in case it's not provided in the declaration
        self.date = date
        self.category = category
        self.price = price
        self.description = string

    # my setters and getters for the same var
    # are grouped together for clarity
    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def setDate(self, date):
        self.date = date

    def getDate(self):
        return self.date

    def setCategory(self, category):
        if category not in AggieBook.aggieCategories.keys():
            self.category = 0 #sets it to Unknown
        else:
            self.category = category

    def getCategory(self):
        self.setCategory(self.category)  # this prevents a TypeError where the category is not in aggieCategories
        return AggieBook.aggieCategories.get(self.category)

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def sellBook(self, quantity):
        return (self.price + ((self.price * AggieBook.stateTax) + (self.price * AggieBook.fedTax))) * quantity

    def __str__(self):  # overriding the str method to change print behavior
        return self.title + " " + self.getCategory() + " " + str(self.price)


init()  # calls the function to fill aggieCategories

