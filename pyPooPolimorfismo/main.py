# Polimorfismo
class Passaro:
    def voar(self): pass


class Pardal(Passaro):
    def voar(self):
        print("Pardal voa")
        super().voar()


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

class Aviao(Passaro):
    def voar(self):
        print("Aviao está decolando")


# FIXME: não usar em sistemas real, exemplo ruim
def plano_de_voo(obj):
    obj.voar()


plano_de_voo(Pardal())
plano_de_voo(Avestruz())

if __name__ == '__main__':
    print(len("python"))
    print(len([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    plano_de_voo(Pardal())
    plano_de_voo(Avestruz())
    plano_de_voo(Aviao())

