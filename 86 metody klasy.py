class Cake:
    def __init__(self, name:str, kind:str, taste:str, additives:list, filling:str):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:    {}".format(self.kind))
        print("Taste:   {}".format(self.taste))

        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling: {}".format(self.filling))
        print('-'*20)

    def set_filling(self, filling:str):
        self.filling = filling

    def add_additives(self, additives:list):
        self.additives.extend(additives)

bakery_offer = [
    Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream'),
    Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], ''),
    Cake('Super Sweet Maringue','meringue', 'very sweet', [], '')
]


bakery_offer[1].set_filling('vanilla cream')
bakery_offer[2].add_additives(['cocoa powder', 'coconuts'])


print("Today in our offer:")
for c in bakery_offer:
    c.show_info()
