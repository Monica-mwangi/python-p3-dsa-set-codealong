class MySet:
    def __init__(self, elements=None):
        if elements is None:
            self.elements = set()
        else:
            self.elements = set(elements)
        # Create a dictionary 
        self.dictionary = {elem: True for elem in self.elements}

    def add(self, element):
        self.elements.add(element)
        self.dictionary[element] = True  

    def remove(self, element):
        self.elements.remove(element)
        del self.dictionary[element]  

    def has(self, element):
        return element in self.dictionary  

    def delete(self, element):
        if self.has(element):  
            self.remove(element)

    def size(self):
        return len(self.elements)

    def __str__(self):
        return str(self.elements)

    def __eq__(self, other):
        return self.elements == other.elements
