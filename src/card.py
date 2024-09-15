'''Карты Зелень'''

class Card:

    def __init__(self, corn = 0, eggplant = 0, broccoli = 0, tomato = 0, carrot = 0):
        if corn + eggplant + broccoli + tomato + carrot != 3:
            raise ValueError
        self.Corn = corn
        self.Eggplant = eggplant
        self.Broccoli = broccoli
        self.Tomato = tomato
        self.Carrot = carrot

    def __repr__(self):
        st = ''
        if self.Corn != 0:
            st += f'Corn - {self.Corn}; '
        if self.Eggplant != 0:
            st += f'Eggplant - {self.Eggplant}; '
        if self.Broccoli != 0:
            st += f'Broccoli - {self.Broccoli}; '
        if self.Tomato != 0:
            st += f'Tomato - {self.Tomato}; '
        if self.Carrot != 0:
            st += f'Carrot - {self.Carrot}; '
        return st[:-2]

    def __eq__(self, other):
        return self.Carrot == other.Carrot and self.Corn == other.Corn \
            and self.Tomato == other.Tomato and self.Broccoli == other.Broccoli and self.Eggplant == other.Eggplant

    def save(self):
        return repr(self)

    @staticmethod
    def load(text: str):
        """From 'Tomato - 3' to Card(tomato=3)"""
        if text.find("Corn - ") != -1:
            corn = int(text[text.find("Corn - ") + 6: text.find("Corn - ") + 8])
        else:
            corn = 0
        if text.find("Eggplant - ") != -1:
            eggplant = int(text[text.find("Eggplant - ") + 10: text.find("Eggplant - ") + 12])
        else:
            eggplant = 0
        if text.find("Brocoli - ") != -1:
            brocoli = int(text[text.find("Brocoli - ") + 9: text.find("Brocoli - ") + 11])
        else:
            brocoli = 0
        if text.find("Tomato - ") != -1:
            tomato = int(text[text.find("Tomato - ") + 8: text.find("Tomato - ") + 10])
        else:
            tomato = 0
        if text.find("Carrot - ") != -1:
            carrot = int(text[text.find("Carrot - ") + 8: text.find("Carrot - ") + 10])
        else:
            carrot = 0
        return Card(corn, eggplant, brocoli, tomato, carrot)

