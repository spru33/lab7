import random

zoo = {
    "Savanna": ["Lion", "Giraffe", "Zebra"],
    "Jungle": ["Monkey", "Tiger", "Parrot"],
    "Aquarium": ["Shark", "Dolphin", "Turtle"],
    "Arctic": ["Polar Bear", "Penguin", "Seal"]
}

visitor_counts = {}

for exhibit in zoo:
    visitor_counts[exhibit] = random.randint(10, 100)

print("zoo exhibit report")
for exhibit in zoo:
    print("Exhibit:", exhibit)
    print("Animals:", zoo[exhibit])
    print("Visitors:", visitor_counts[exhibit])

total_visitors = 0
for exhibit in visitor_counts:
    total_visitors += visitor_counts[exhibit]
print("Total visitors:", total_visitors)

most_visited = ""
highest_count = 0
for exhibit in visitor_counts:
    if visitor_counts[exhibit] > highest_count:
        highest_count = visitor_counts[exhibit]
        most_visited = exhibit

print("Most visited exhibit:", most_visited)
print("Number of visitors:", highest_count)