from animal import Animal
from interface_animal import InterfaceAnimal
from dono import Dono

class Cachorro(Animal, InterfaceAnimal):
    def __init__(self, nome, idade, cor, qtd_brinquedos, dono=Dono()):
        super().__init__(nome, idade, cor)
        self.__qtd_brinquedos = qtd_brinquedos
        self.__dono = dono

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Cor: {self.cor}, Quantidade de brinquedos: {self.qtd_brinquedos}, Dono: {self.dono.nome}"    

    @property
    def qtd_brinquedos(self):
        return self.__qtd_brinquedos    
    
    @qtd_brinquedos.setter
    def qtd_bolinhas(self, qtd_brinquedos):
        self.__qtd_brinquedos = qtd_brinquedos   

    @property
    def dono(self):
        return self.__dono

    @dono.setter
    def dono(self, dono):
        self.__dono = dono     


    def fazer_barulho(self):
        return "Au Au" 
    
    def brincar(self):
        self.felicidade += 2
        return "Brincando com os brinquedos"