class Silnia:
    stala = 5

    def mnozenie(self, a, b):
        a += self.stala
        return a * b

    def dzielenie(self, a, b):
        """
        hhgd
        :param a:
        :type a:
        :param b:
        :type b:
        :return:
        :rtype:
        """
        b -= b - self.stala
        return a // b


class Matma:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def licz(self):
        """
        xcxc
        :return: cxzc
        :rtype: zxczxc
        """
        return self._a + self._b
