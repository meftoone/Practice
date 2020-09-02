import random

class Düşman():
    def __init__(self):
        self.saglik=random.randint(30,70)
        self.güc=random.randint(20,50)
        self.kalkan=random.randint(0,10)
    def vur(self,player):
        damage=self.güc - player.kalkan
        player.saglik-=damage


class Player():
    def __init__(self):
        self.saglik=500
        self.kalkan=123123
        self.güc=55


    def vur(self,Düşman):
        damage=self.güc - Düşman.kalkan
        Düşman.saglik-=damage
        if düşman.saglik <=0:
            düşman.saglik=False
            düşmanlar.remove(düşman)

düşmanlar = list()
for i in range(3):
    düşmanlar.append(Düşman())

player=Player()
print("0. player ->saglik:{} -- güc:{}--kalkan:{}".format(player.saglik, player.güc, player.kalkan),end="\n \n")
while True:

    if not düşmanlar:
        print("teprikler")
        quit()
    for i in düşmanlar:
        print("{} Düşman ->saglik:{} -- güc:{}--kalkan:{}".format(düşmanlar.index(i),i.saglik,i.güc,i.kalkan))

    try:
        secim=int(input("düşmanseçim:"))
        düşman = düşmanlar[secim]
        player.vur(düşman)
    except:
        print("irrevelant choice")
        pass