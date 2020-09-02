from os import system as komut


class Client():
    def __init__(self,ID,PAROLA,ISIM):
        self.isim=ISIM
        self.id=ID
        self.parola=PAROLA
        self.bakiye=0

class Bank():
    def __init__(self):
        self.clients=list()
    def beClient(self,ID,PAROLA,ISIM):
        self.clients.append(Client(ID,PAROLA,ISIM))
        print("welcome to our bank")


def main():
    banka=Bank()
    while True:
        print("""
        [1]Currently  Client
        [2]Wanna be a Client    
        """)

        secim = input("seçiminiz")

        if secim == "1":
            ids=[i.id for i in banka.clients]
            ID = input("IDs :")
            if ID in ids:
                for client in banka.clients:
                    if ID == client.id:
                        print("welcome {}".format(client.isim))
                        password = input("enter a password")
                        if password == client.parola:
                            print("""
                            [1] Ammount
                            [2] deposit own acc
                            [3] deposit another acc
                            [4] withdraw 
                            [Q] quit
                            """)
                            choice2= input("your choice ?:")
                            if choice2 =="1":
                                print("your wallet is {}",client.bakiye)
                            elif choice2 =="2":
                                amount = int(input("Amount:"))
                                approve = input("do you approve a amount {}")
                                if approve == "Y" or approve =="y":
                                    client.bakiye += amount
                                    print("process complete")
                                elif approve == "N" or approve == "n":
                                    print("process canceled")
                                else:
                                    print("wroing choice only y or n")
                            elif choice2 == "3":
                                searchingID = input("other Client ID:")
                                if searchingID in ids:
                                    for otherClient in banka.clients:

                                        if searchingID == otherClient.id:
                                            amount=int(input("amount"))
                                            approve = input("do you approve a amount {} send to {}".format(amount,client.isim))
                                            if approve == "Y" or approve == "y":
                                                otherClient.bakiye += amount
                                                client.bakiye-=amount
                                                print("process complete")
                                            elif approve == "N" or approve == "n":
                                                print("process canceled")
                                                pass
                                            else:
                                                print("wroing choice only y or n")
                                print("theri is no client like that")
                            elif choice2 == "4":
                                withdrawmoney = int(input("amount you need to withdraw"))
                                if withdrawmoney <= client.bakiye:
                                    client.bakiye-=withdrawmoney
                                    print("process completed take your money dont forget!!")
                                else:
                                    print("your bank acc not enough to with draw money")
                            elif choice2 == "q" or choice2=="Q":
                                break
        elif secim == "2":
            ID=input("id")
            ISIM=input("name")
            PAROLA=input("parola")
            banka.beClient(ID,PAROLA,ISIM)

if __name__ == '__main__':
    main()
