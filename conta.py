#-*- coding: latin1 -*-
from errors import ValorInvalidoError
from errors import SaldoInsuficienteError
class Conta:

    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0.0
        self.extrato=[]

    def __str__(self):
        return " Conta " + str(self.numero) + "\n" + " Saldo R$" + str(self.saldo)

    def op_saldo(self) :
        return self.saldo

    def op_saque(self, valor) :
        if (valor > self.saldo) :
            raise SaldoInsuficienteError()
        elif (valor <= 0):
            raise ValorInvalidoError()
        else :
            self.saldo = self.saldo - valor
            self.extrato.append("R$: "+str(valor)+" (Saque)");

    def op_deposito(self, valor) :
        if (valor <= 0):
            raise ValorInvalidoError()
        else :
            self.saldo = self.saldo + valor
            self.extrato.append("R$: "+str(valor)+" (Depósito)");
            

    def get_extrato(self):

        texto="Extrato – Conta: "+str(self.numero)+"\n----------------\n"
        for x in range(len(self.extrato)):
            texto+=self.extrato[x]+"\n"
        texto+="----------------\n"
        texto+="Saldo Atual: R$ "+str(self.saldo)
        return texto


