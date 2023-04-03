## membuat program bank

class Bank:

    def __init__(self, nama):
        self.nama = nama
        self.saldo = 1000000

    def cekSaldo(self):
        print("saldo nasabah adalah Rp" + str(self.saldo))
    
    def kurangSaldo(self, tunai):
        self.saldo -= tunai
    
    def tambahSaldo(self, tunai):
        self.saldo += tunai

    def transferSaldo(self, tunai):
        if (self.saldo >= tunai):
            self.kurangSaldo(tunai)
        else :
            print("maaf saldo " + self.nama + " tidak mencukupi")

    def setorSaldo(self, tunai):
        self.tambahSaldo(tunai)
        print("saldo " + self.nama + " telah bertambah")
        self.cekSaldo()

# membuat objek baru bernama robin
orang1 = Bank("robin")

# mengecek nama dan saldo rekening robin
print("nama nasabah adalah " + orang1.nama)
Bank.cekSaldo(orang1)

# si robin mau transfer 700rb ke orang lain
Bank.transferSaldo(orang1, 700000)
Bank.cekSaldo(orang1)

# si robin mau setor tunai 100rb
Bank.setorSaldo(orang1, 100000)
Bank.cekSaldo(orang1)

# si "robin mau transfer 500rb ke orang lain
Bank.transferSaldo(orang1, 500000)
Bank.cekSaldo(orang1)
