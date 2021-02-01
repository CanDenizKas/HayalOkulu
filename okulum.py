
class Okul():
 

    def __init__(self, personel=3, bina=1, sporsalonu=0, bahce=True):
        self.bahce = bahce
        self.bina = bina
        self.sporsalonu = sporsalonu
        self.personel = personel
      
 tip = "Devlet Kurumu"

okullar1 = Okul(50, 3, 4, True)
okulllar2 = Okul(20, 2, 2, False)
okullar3 = Okul(personel=10, sporsalonu=1)
print(okullar1.__class__.tip)
print(okullar3.personel)

