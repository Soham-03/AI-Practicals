class Person:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []

    def add_child(self, child):
        if child not in self.children:
            self.children.append(child)
            child.parents.append(self)

    def get_children(self):
        return [child.name for child in self.children]

    def get_parents(self):
        return [parent.name for parent in self.parents]

    def get_siblings(self):
        siblings = set()
        for parent in self.parents:
            for sibling in parent.children:
                if sibling != self:
                    siblings.add(sibling.name)
        return list(siblings)

# Example Usage
alice = Person("Alice")
bob = Person("Bob")
carol = Person("Carol")

# Adding children
alice.add_child(bob)
alice.add_child(carol)

# Test outputs
print(f"Alice's children: {alice.get_children()}")
print(f"Bob's parents: {bob.get_parents()}")
print(f"Carol's siblings: {carol.get_siblings()}")
