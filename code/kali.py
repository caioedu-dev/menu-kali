import random
class MenuKali:
    def __init__(self):
        self.largura = 40
    def menu(self):
        
        print('=' * self.largura)
        print('MENU KALI'.center(self.largura))
        print('=' * self.largura)
        print()
        print('[ 1 ] Gerar Senha Segura')
        print('[ 2 ] Analisar Força da Senha')
        print('[ 3 ] Ver Informações Da Máquina')
        print('[ 4 ] Organizador De Arquivos')
        print('[ 5 ] Verificação De Segurança')
        print('[ 6 ] Histórico De Ações')
        print('[ 7 ] Sair')
class GeradorSenha:
   def __init__(self):
       self.__senha= []
       self.__caracteres = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789"
    "!@#$%&*"
)
   def pedir_tamanho(self):
       self.tamanho=int(input('Digite o tamanho da senha: '))
   def gerar(self):
       while len(self.__senha) < self.tamanho:
          self.__senha.append(random.choice(self.__caracteres))
   def mostra_senha(self):
       print("".join(self.__senha))
app = MenuKali()
gerador = GeradorSenha()
while True:
    app.menu()

    opcao = input('Qual a sua opção: ')

    if opcao == '1':
       gerador.pedir_tamanho()
       gerador.gerar()
       gerador.mostra_senha()

       