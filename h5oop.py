class hesap():
    def __init__(self,say1,say2):
        self.say1=say1
        self.say2=say2
    def carp(self):
        sonuc= self.say1 * self.say2
        return sonuc
    def bol(self):
        sonuc= self.say1 / self.say2
        return sonuc
    def topla(self):
        sonuc=self.say1 + self.say2
        return sonuc
    def cikar(self):
        sonuc=self.say1 - self.say2
        return sonuc
    def yazdir(self):
        toplam=self.topla()
        carpma=self.carp()
        bolme=self.bol()
        cikarma=self.cikar()
        print("sayıların toplamı:",toplam)
        print("sayıların carpımı",carpma)
        print("sayıların bölümü",bolme)
        print("sayıların farkı",cikarma)


