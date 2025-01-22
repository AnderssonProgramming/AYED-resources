#from sys import stdin

class DisjointSets:

    def __init__(self, A):
        self.sets = {x: x for x in A}

    def getSets(self):
        return list(set(self.sets.values()))

    def findSet(self, x):
        return self.sets.get(x, None)

    def makeSet(self, x):
        if x not in self.sets:
            self.sets[x] = x

    def union(self, x, y):
        s1 = self.findSet(x)
        s2 = self.findSet(y)

        if s1 != s2:
            for k, v in self.sets.items():
                if v == s2:
                    self.sets[k] = s1

    def connectedComponents(self):
        sets = {}
        for k, v in self.sets.items():
            sets.setdefault(v, []).append(k)
        return list(sets.values())

class SocialNetwork(DisjointSets):

    def addFriendship(self, x, y):
        self.union(x, y)

    def areFriends(self, x, y):
        return self.findSet(x) == self.findSet(y)

def main():
    dj = SocialNetwork(["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Hannah", "Ian"])
    print('Initial State', dj.getSets())
    dj.makeSet("John")
    print('Adding new member', "John", dj.getSets())
    dj.makeSet("Alice")
    print('Adding Existing member', "Alice", dj.getSets())

    print('Find Set', "Alice", dj.findSet("Alice"))
    print('Find Set', "Tom", dj.findSet("Tom"))

    dj.addFriendship("Alice", "Bob")
    print('Friendship added between Alice and Bob', dj.getSets())
    dj.addFriendship("Alice", "Charlie")
    dj.addFriendship("Bob", "David")
    print('Friendships added', dj.getSets())

    # Check if two users are friends
    print('Are Alice and Bob friends?', dj.areFriends("Alice", "Bob"))
    print('Are Alice and Frank friends?', dj.areFriends("Alice", "Frank"))

    #This returns a boolean depending if those people are friends

main()
