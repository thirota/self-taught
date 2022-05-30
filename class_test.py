
class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        self.mold = days * temp


o = Orange(10, "dark")
print(o.weight)
print(o.color)
print(o.mold)

o.rot(5, 28)
print(o.mold)

