class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
    '''
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network.")
        else:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people or person2_name not in self.people:
            print(f"Friendship not created. One or both people don't exist: {person1_name}, {person2_name}")
        else:
            person1 = self.people[person1_name]
            person2 = self.people[person2_name]
            person1.add_friend(person2)
            person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]
            print(f"{name} is friends with: {', '.join(friend_names)}")


# Test your code here
network = SocialNetwork()

# Add people
network.add_person("Alex")
network.add_person("Jordan")
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

# Create friendships
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Jordan", "Johnny")  # Should print error
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

# Print the network
network.print_network()

# Deisgn Memo
# A graph is the ideal data structure for modeling a social network because it naturally represents relationships between entities.
# Each person can be treated as a node, and each friendship as an edge connecting two nodes. 
# This structure allows for efficient traversal, querying, and expansion — all critical for simulating real-world social dynamics.
# Unlike a list, which only stores linear data, a graph supports complex, non-linear relationships. 
# A tree structure, while hierarchical, fails to capture mutual connections and cyclical relationships common in social networks. 
# For example, in a tree, a person could only have one “parent” node, which doesn’t reflect the bidirectional nature of friendships.
# During implementation, I noticed that adding friends was straightforward using adjacency lists, but required careful checks to avoid duplicates or missing nodes. 
# The add_friendship method had to validate both participants before creating a connection, which added robustness to the network. 
# Printing the network was efficient, but formatting friend lists for readability required extra attention.
# One trade-off is that while adjacency lists are memory-efficient and fast for sparse networks, they can become less performant if the network grows dense or requires frequent lookups. 
# However, for this assignment’s scale, the structure was both intuitive and effective.
# Overall, this project reinforced how graph theory applies to real-world systems and highlighted the importance of validating inputs and designing for scalability.
