class Vector:
    def __init__(self, dim:int):
        #this array will contain the coordinates of the vector
        self.dim = dim
        self.coordinates = []

        for i in range(dim):
            self.coordinates.append(0)

    def __len__(self):
        return self.dim

    def __str__(self):
        result = "("

        for i in range(len(self.coordinates)):
            result += str(self.coordinates[i])

            if (i != len(self.coordinates) - 1):
                result += ","
        
        result += ")"

        return result

    def __getitem__(self, i):
        return self.coordinates[i]

    def __setitem__(self, i, newValue):
        self.coordinates[i] = newValue

    def __add__(self, other):
        if(type(other) != Vector):
            return "Sum two vectors bro"

        if(self.dim != other.dim):
            return "Sum two vectors of the same dimension bro"

        result = Vector(self.dim)

        for i in range(len(self.coordinates)):
            result.coordinates[i] = self.coordinates[i] + other.coordinates[i]

        return result

    def __eq__(self, other):
        if(type(other) != Vector):
            return "Compare two vectors bro"

        if(self.dim != other.dim):
            return "Compare two vectors of the same dimension bro"

        result = True

        for i in range(len(self.coordinates)):
            if (self.coordinates[i] != other.coordinates[i]):
                result = False

        return result 
    
    def dot(self, other):
        if(type(other) != Vector):
            return "Operate two vectors bro"

        if(self.dim != other.dim):
            return "Operate two vectors of the same dimension bro"

        result = 0

        for i in range(self.dim):
            result += self.coordinates[i] * other.coordinates[i]

        return result

    #What is cosine distance
    """def cosine_angle(self):
        if(type(other) != Vector):
            return "Operate two vectors bro"

        if(self.dim != other.dim):
            return "Operate two vectors of the same dimension bro"

        result = 0

        for i in range(self.dim):
            result += self.coordinates[i] * other.coordinates[i]

        return result"""
        
vector1= Vector(2)
vector2 = Vector(2)
vector1[0] = 2
vector2[0] = 3
print(vector1.dot(vector2))