'''Write __str__() method to print the vector as follows: 
7i + 8j +10k  '''

class Vector:
    def __init__(self, components):
        self.components = components  

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        return sum(a * b for a, b in zip(self.components, other.components))

    def __str__(self):
        labels = ['i', 'j', 'k']  # Labels for the first 3 dimensions
        terms = [f"{self.components[i]}{labels[i]}" if i < 3 else f"{self.components[i]}e{i+1}" 
                 for i in range(len(self.components))]
        return " + ".join(terms)


# Example Usage
v1 = Vector([1, 2, 3])
v2 = Vector([6, 6, 7])

print("Addition:", v1 + v2)   # Output: 7i + 8j + 10k
print("Dot Product:", v1 * v2)  # Output: 41
