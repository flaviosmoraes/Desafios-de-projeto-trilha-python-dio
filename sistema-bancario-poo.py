from abc import ABC, ABCMeta, abstractmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    @property
    def endereco(self):
        return self._endereco

    @property
    def contas(self):
        return self._contas

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)
        

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(self, endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self._cpf

    @property
    def nome(self):
        return self._nome

    @property
    def data_nascimento(self):
        return self._data_nascimento
    
class Conta:
    def __init__(self, cliente, numero):
        self._saldo = 0.00
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

    def sacar(self, valor):
        if valor > self.saldo:
            print("\nSaldo insuficiente.")
        elif valor > 0:
            self._saldo -= valor
            print(f"\nDeposito no valor de R${valor:.2f} efetuado com sucesso.\nNovo saldo R$ {self.saldo:.2f} .")
            return True
        else:
            print("\nInsira um valor maior que R$ 0.00")
        return False


    def depositar(self, valor):
        if valor > 0.00:
            self._saldo += valor
            print(f"\nDeposito no valor de R${valor:.2f} efetuado com sucesso.\nNovo saldo R$ {self.saldo:.2f} .")
            return True
        else:
            print("\nInsira um valor maior que R$ 0.00")
            return False

class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, limite=500, limite_saques=3) -> None:
        super().__init__(self, saldo, numero, agencia, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    @property
    def limite(self):
        return self._limite

    @property
    def limite_saques(self):
        return self._limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])
        if valor > self.limite:
            print(f"\nO valor do saque ultrapassa o limite de R$ {self:_limite:.2f}")
        elif numero_saques < self.limite_saques:
            super().sacar(self, valor)
        else:
            print(f"\nValor limite de {self.limite_saques} saques atingido, volte amanhã para conseguir realizar novos saques.")
        return False
    
    def __str__(self) -> str:
        return f"""
            Titular: {self.cliente.nome}
            Número da conta: {self.numero}
            Agência: {self.agencia}
        """

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_trasacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_trasacao(self)


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_trasacao(self, trasacao):
        self._transacoes.append({
            "tipo": trasacao.__class__.__name__,
            "valor": trasacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s")
        })

