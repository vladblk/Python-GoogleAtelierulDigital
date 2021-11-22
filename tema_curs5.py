# Să se scrie o clasă Fractie(numarator, numitor) care sa implementeze următoarele metode:
# __init__ : instanțiem numărător și numitor
#  __str__  : afisam "numărător/numitor"
# __add__ : returnam o noua fractie care reprezinta adunarea
# __sub__: returnam o nouă fracție care reprezinta scădearea
# inverse: returnează o nouă fracție (inversa fracției)

class Fractie:
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f'{self.numarator}/{self.numitor}'

    def __add__(self, other):
        if self.numitor == other.numitor:
            return f'{self.numarator + other.numarator}/{self.numitor}'

        suma_numarator = (self.numarator * other.numitor + other.numarator * self.numitor)
        suma_numitor = self.numitor * other.numitor

        return f'{suma_numarator}/{suma_numitor}'

    def __sub__(self, other):
        if self.numitor == other.numitor:
            return f'{self.numarator - other.numarator}/{self.numitor}'

        dif_numarator = (self.numarator * other.numitor - other.numarator * self.numitor)
        dif_numitor = self.numitor * other.numitor

        return f'{dif_numarator}/{dif_numitor}'

    def inversa_fractie(self):
        return f'{self.numitor}/{self.numarator}'


a = Fractie(14, 10)
b = Fractie(24, 3)

print(a)
print(b)
print(a + b)
print(a - b)
print(a.inversa_fractie())
print(b.inversa_fractie())
