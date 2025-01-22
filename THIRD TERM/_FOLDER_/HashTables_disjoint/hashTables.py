from sys import stdin
from random import randint

class HashTable:
    def __init__(self, size):
        self.elements = [ [] for x in range(size)]


    def getElements(self):
        return self.elements

    def printElements(self):
        for index in range(len(self.elements)):
            print(index, ': ', self.elements[index])

    def hash(self, key):
        return hash(key) % len(self.elements)

    def assign(self, index, element):
        self.elements[index].append(element)

    def insert(self, key, value):
        index = self.hash(key)
        print('Inserting', value, 'with key', key, 'on index', index)
        self.assign(index, (key,value))

    def search(self, key):
        index = self.hash(key)
        for e in self.elements[index]:
            if e[0] == key:
                return e[1]
        return None

    def update(self, key, value2):
        index = self.hash(key)
        for e in self.elements[index]:
            if e[0] == key:
                e[1] = value2

    def delete(self, key):
        index = self.hash(key)
        element = self.search(key)
        if element:
            self.elements[index].remove(element)

def main():

    randomPairs = [ (('Colombia', '1243', 'Max'), 'alexei@mail.com'),
                    (('París', '456', 'Ernesto'), 'scmr@yahoo.es'),
                    (('Mexico', '764', 'Patricia'), 'elemental@outlook.com'),
                    ]

    hashtable = HashTable(13)
    for e in randomPairs:
        hashtable.insert(e[0], e[1])
    hashtable.printElements()
    print('Searching for ', ('Colombia', '1243', 'Max'), ': ', hashtable.search(('Colombia', '1243', 'Max')))


main()

# sha, MD5