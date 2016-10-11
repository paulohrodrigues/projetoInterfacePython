#coding:latin1
from Tkinter import *
from errors import ValorInvalidoError
from errors import SaldoInsuficienteError
from conta import Conta

class Menu(object): 
    def __init__(self):
        self.contas = {}
        janela =Tk()

        btCadastro=Button(janela,text="Cadastro",width=20, command=self.cadastro)
        btCadastro.place(x=70,y=20)

        btSaldo=Button(janela,text="Saldo",width=20, command=self.saldo)
        btSaldo.place(x=70,y=50)

        btSaque=Button(janela,text="Saque",width=20, command=self.saque)
        btSaque.place(x=70,y=80)

        btDeposito=Button(janela,text="Deposito",width=20, command=self.deposito)
        btDeposito.place(x=70,y=110)

        btDeposito=Button(janela,text="Extrato",width=20, command=self.extrato)
        btDeposito.place(x=70,y=140)

        janela.geometry("300x200+200+200")
        janela.mainloop()
    def saqueController(self,entrada1,entrada2,mensagem):

        numero = entrada1
        if self.contas.has_key(numero):
            conta=self.contas[numero]
        else:
            mensagem["text"]="Conta invalida"
        try:
            valor = float(entrada2)
            conta.op_saque(valor)
            mensagem["text"]="Saque realizado com sucesso!"
        except ValorInvalidoError as vie:
            mensagem["text"]=vie
        except SaldoInsuficienteError as sie:
            mensagem["text"]=sie
    def depositoController(self,entrada1,entrada2,mensagem):

		if self.contas.has_key(entrada1) :
			conta=self.contas[entrada1]
			try:
				valor = float(entrada2)
				conta.op_deposito(valor)
				mensagem["text"]="Deposito realizado com sucesso!"
			except ValorInvalidoError as vie:
				mensagem["text"]=vie
		else:
			mensagem["text"]="Conta Invalida!"
    def cadastraContoller(self,entrada,label):
        ent=entrada

        if self.contas.has_key(ent) :
            label["text"]="Já existe uma conta cadastrada com este número!"
        else:
            conta = Conta(ent)
            self.contas[ent] = conta
            label["text"]="Conta cadastrada com sucesso!"
    def extratoController(self,entrada,label):
        ent=entrada
        if self.contas.has_key(ent) :
            label["text"]=self.contas[ent].get_extrato()
        else:
            label["text"]="Conta Invalida!"
    def saldoController(self,entrada,label):
        numero = entrada
        if self.contas.has_key(numero) :
            label["text"]=self.contas[numero]
        else:
            label["text"]="Conta não existente"
    def cadastro(self):
            janela =Tk()

            label=Label(janela,text="Digite o número da conta:")
            label.place(x=70,y=10)

            labelMensagem=Label(janela,text="")
            labelMensagem.place(x=30,y=100)         

            entrada=Entry(janela,width=25)
            entrada.place(x=70,y=40)

            btCadastro=Button(janela,text="Cadastrar",width=20, command=lambda:self.cadastraContoller(entrada.get(),labelMensagem))
            btCadastro.place(x=70,y=70)



            janela.geometry("300x200+400+200")
            janela.mainloop()
    def saque(self):

        janela =Tk()

        label=Label(janela,text="Digite o número da conta:")
        label.place(x=70,y=10)

        entrada=Entry(janela,width=25)
        entrada.place(x=70,y=30)

        label=Label(janela,text="Digite o valor desejado: R$:")
        label.place(x=70,y=70)

        entrada2=Entry(janela,width=25)
        entrada2.place(x=70,y=90)

        labelMensagem=Label(janela,text="")
        labelMensagem.place(x=30,y=120)

        btCadastro=Button(janela,text="Sacar",width=20, command=lambda:self.saqueController(entrada.get(),entrada2.get(),labelMensagem))
        btCadastro.place(x=70,y=160)

        janela.geometry("300x300+400+200")
        janela.mainloop()
    def saldo(self):
            janela =Tk()

            label=Label(janela,text="Digite o número da conta:")
            label.place(x=70,y=10)

            labelMensagem=Label(janela,text="")
            labelMensagem.place(x=70,y=100)         

            entrada=Entry(janela,width=25)
            entrada.place(x=70,y=40)

            btCadastro=Button(janela,text="Consultar",width=20, command=lambda:self.saldoController(entrada.get(),labelMensagem))
            btCadastro.place(x=70,y=70)

            janela.geometry("300x200+400+200")
            janela.mainloop()
    def deposito(self):
        janela =Tk()

        label=Label(janela,text="Digite o número da conta:")
        label.place(x=70,y=10)

        entrada=Entry(janela,width=25)
        entrada.place(x=70,y=30)

        label=Label(janela,text="Digite o valor desejado: R$:")
        label.place(x=70,y=70)

        entrada2=Entry(janela,width=25)
        entrada2.place(x=70,y=90)

        labelMensagem=Label(janela,text="")
        labelMensagem.place(x=30,y=120)

        btCadastro=Button(janela,text="Depositar",width=20, command=lambda:self.depositoController(entrada.get(),entrada2.get(),labelMensagem))
        btCadastro.place(x=70,y=160)

        janela.geometry("300x300+400+200")
        janela.mainloop()
    def extrato(self):
            janela =Tk()

            label=Label(janela,text="Digite o número da conta:")
            label.place(x=70,y=10)

            labelMensagem=Label(janela,text="")
            labelMensagem.place(x=70,y=100)         

            entrada=Entry(janela,width=25)
            entrada.place(x=70,y=40)

            btCadastro=Button(janela,text="Consultar",width=20, command=lambda:self.extratoController(entrada.get(),labelMensagem))
            btCadastro.place(x=70,y=70)



            janela.geometry("300x500+400+200")
            janela.mainloop()
Menu()