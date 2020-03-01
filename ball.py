from datetime import datetime


class Ball:
    def __innit__(self, kind, radius, weight, material):
        self.kind = kind
        self.radius = radius
        self.weight = weight
        self.material = material

    def show(self):
        if self.kind:
           str_kind = "basket"
        else:
           str_kind = "foot"
        return str_kind + str(self.radius) + str(self.weight) + str.material

