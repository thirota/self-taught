
# Rect class
class Rect:
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((w,l))

    def print_size(self):
        print("{} by {}".format(self.width, self.len))

    def __repr__(self):
        return "I am Rect object"

    def __add__(self, other):
        #return self.width + other.width
        return self.len + other.len


r1 = Rect(10,24)
r2 = Rect(20,40)
r3 = Rect(100,200)

print(Rect.recs)



print(r1)
debug_str = r1.__repr__()
print(debug_str.split())
#print(r1.__add__())   # no attribute error
print(r1 + r2)


print(r1 is r2)
r4 = r2
print(r4 is r2)

