class PokerPlayer():
    def __init__(self, first_name, last_name, age, town, tournaments, victories, level):
        self.ime = first_name
        self.priimek = last_name
        self.starost = age
        self.kraj = town
        self.turnirji = tournaments
        self.zmage = victories
        self.nivo = level

print("Dobrodošli! Vpišite vaše podatke in se prijavite na turnir v Pokru.")

ime = input("Vpiši tvoje ime: ")
priimek = input("Vpiši tvoj priimek: ")
starost = input("Koliko si star? ")
kraj = input("Vpiši kraj bivanja: ")
turnirji = input("Koliko turnirjev si se že udeležil? ")
zmage = input("Koliko turnirjev si že zmagal? ")
nivo = input("Vpiši nivo igranja (začetnik / profesionalec): ")

nov_igralec = PokerPlayer(first_name=ime, last_name=priimek, age=starost, town=kraj, tournaments=int(turnirji), victories=int(zmage), level=nivo)

with open("poker_prijave.txt", "w") as turnir_file:
    turnir_file.write(str(nov_igralec.__dict__))

print("Player successfully entered!")
print("Player's data: {0}".format(nov_igralec.__dict__))