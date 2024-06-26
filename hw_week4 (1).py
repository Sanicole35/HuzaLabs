# -*- coding: utf-8 -*-
"""hw_week4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zl-sA1AQCgFI-iyFPWwV20RXiFHZuxYZ

**Extra-practice 8 - 1;**
"""



def mostCommonName_n2(names):
    if not names:
        return None
    max_count = 0
    most_common_names = set()
    for name in names:
        count = names.count(name)
        if count > max_count:
            most_common_names = {name}
            max_count = count
        elif count == max_count:
            most_common_names.add(name)
    return most_common_names if most_common_names else None

def mostCommonName_nlogn(names):
    if not names:
        return None
    name_counts = Counter(names)
    max_count = max(name_counts.values())
    most_common_names = {name for name, count in name_counts.items() if count == max_count}
    return most_common_names if most_common_names else None

def mostCommonName_n(names):
    if not names:
        return None
    name_counts = {}
    max_count = 0
    most_common_names = set()
    for name in names:
        name_counts[name] = name_counts.get(name, 0) + 1
        if name_counts[name] > max_count:
            most_common_names = {name}
            max_count = name_counts[name]
        elif name_counts[name] == max_count:
            most_common_names.add(name)
    return most_common_names if most_common_names else None

def main():
    names = input("Enter a list of names separated by spaces: ").split()

    print("Most common name(s) using O(n^2):", mostCommonName_n2(names))
    print("Most common name(s) using O(nlogn):", mostCommonName_nlogn(names))
    print("Most common name(s) using O(n):", mostCommonName_n(names))

if __name__ == "__main__":
    main()





"""**Extra-practice 8 - 5;**"""

def mostPopularFriend(d):
    friend_counts = {}

    # Iterate over each set of friends
    for friends in d.values():
        for friend in friends:
            friend_counts[friend] = friend_counts.get(friend, 0) + 1

    # Find the friend with the highest count
    most_popular_friend = max(friend_counts, key=friend_counts.get)

    return most_popular_friend

# Example usage:
d = dict()
d["fred"] = set(["wilma", "betty", "barney"])
d["wilma"] = set(["fred", "betty", "dino"])

print("Most popular friend:", mostPopularFriend(d))



"""**Extra-practice 8 - 6;**"""

def findTriplets(L):
    triplets = set()
    n = len(L)

    # Create a dictionary to store pairs of numbers and their sum
    pairs_sum = {}
    for i in range(n):
        for j in range(i+1, n):
            pair_sum = L[i] + L[j]
            pairs_sum[(L[i], L[j])] = pair_sum

    # Check for triplets
    for num in L:
        if -num in pairs_sum.values():
            for pair, pair_sum in pairs_sum.items():
                if pair_sum == -num:
                    triplet = tuple(sorted(list(pair) + [num]))
                    triplets.add(triplet)

    return triplets

# Example usage:
L = [-1, 0, -3, 2, 1]
print("Triplets with sum equal to 0:", findTriplets(L))

"""**Hw 8 - 2**"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getFriends(self):
        return self.friends

    def getFriendsNames(self):
        return sorted([friend.getName() for friend in self.friends])

    def addFriend(self, person):
        if person not in self.friends:
            self.friends.append(person)
            person.addFriend(self)

    def addFriends(self, people):
        for person in people:
            self.addFriend(person)

    @staticmethod
    def createPersonFromInput():
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        return Person(name, age)

    def addFriendFromInput(self):
        friend = Person.createPersonFromInput()
        self.addFriend(friend)

"""**Hw 8-3**"""

def getPairSum(L, target):
    seen = set()
    for num in L:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return None

# Test cases
print(getPairSum([1], 1))  # None
print(getPairSum([5, 2], 7))  # (5, 2) or (2, 5)
print(getPairSum([10, -1, 1, -8, 3, 1], 2))  # (3, -1) or (-1, 3) or (1, 1) or (10, -8) or (-8, 10)
print(getPairSum([10, -1, 1, -8, 3, 1], 10))  # None

"""**Hw 8-4**"""

def containsPythagoreanTriple(L):
    squares = set()
    for num in L:
        squares.add(num ** 2)
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if L[i] ** 2 + L[j] ** 2 in squares:
                return True
    return False

# Test cases
print(containsPythagoreanTriple([1, 3, 6, 2, 5, 1, 4]))  # True
print(containsPythagoreanTriple([1, 3, 6, 2, 1, 4]))     # False

"""**Hw 8-5**"""

def movieAwards(oscarResults):
    movie_awards = {}
    for category, movie in oscarResults:
        if movie in movie_awards:
            movie_awards[movie] += 1
        else:
            movie_awards[movie] = 1
        if len(movie_awards) == len(set(movie for _, movie in oscarResults)):
            return movie_awards

# Test case
oscar_results = {
    ("Best Picture", "Green Book"),
    ("Best Actor", "Bohemian Rhapsody"),
    ("Best Actress", "The Favourite"),
    ("Film Editing", "Bohemian Rhapsody"),
    ("Best Original Score", "Black Panther"),
    ("Costume Design", "Black Panther"),
    ("Sound Editing", "Bohemian Rhapsody"),
    ("Best Director", "Roma")
}

result = movieAwards(oscar_results)
if result:
    print(result)
else:
    print("No result yet. Continue processing...")

"""**Hw 8-6**"""

def friendsOfFriends(d):
    friends_of_friends = {}
    for person, friends in d.items():
        fofs = set()
        for friend in friends:
            fofs.update(d.get(friend, set()))  # Retrieve friend's friends or empty set if friend not in dictionary
        fofs -= {person}  # Remove the person itself
        fofs -= friends    # Remove direct friends
        friends_of_friends[person] = fofs
    return friends_of_friends

# Test case
d = {
    "jon": {"arya", "tyrion"},
    "tyrion": {"jon", "jaime", "pod"},
    "arya": {"jon"},
    "jaime": {"tyrion", "brienne"},
    "brienne": {"jaime", "pod"},
    "pod": {"tyrion", "brienne", "jaime"},
    "ramsay": set()
}

print(friendsOfFriends(d))

"""**Hw 8-7**"""

import matplotlib.pyplot as plt
import numpy as np
import random

# Bubble Sort algorithm
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            yield data.copy(), j, j+1  # Yield the current state of data and indices being compared
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                yield data.copy(), j, j+1  # Yield the updated state after swapping

# Function to generate a shuffled list of numbers from 0 to 20
def generate_data():
    data = list(range(21))
    random.shuffle(data)
    return data

# Initialize the figure
fig, ax = plt.subplots()
ax.set_title('Bubble Sort Visualization')

# Generate initial data and plot
data = generate_data()
bars = ax.bar(range(len(data)), data, align='edge')
ax.set_xticks(range(0, 21, 2))

# Update function for animation
def update(frame):
    current_data, i, j = frame
    for rect, val in zip(bars, current_data):
        rect.set_height(val)
        rect.set_color('skyblue')  # Reset color
    bars[i].set_color('orange')  # Highlight comparison
    bars[j].set_color('orange')  # Highlight comparison

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=bubble_sort(data), repeat=False)

plt.show()