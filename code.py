class Silnia:
    stala = 5

    def mnozenie(self, a, b):
        a += self.stala
        return a * b

    def dzielenie(self, a, b):
        b -= b - self.stala
        return a // b


class Matma:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def licz(self):
        return self._a + self._b
