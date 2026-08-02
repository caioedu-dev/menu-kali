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
    "!@#$&#$#$!@@#$#@@*"
)
   def pedir_tamanho(self):
       while True:
           self.tamanho = int(input('tamanho da sua senha: '))
           if self.tamanho < 12:
               print('A senha deve ter 12 ou mais caracteres')
           elif self.tamanho > 32:
               print('A senha deve ter 32 caracteres no maximo.')
           elif self.tamanho >= 12:
               break
   def gerar(self):
       self.__senha.clear()
       while len(self.__senha) < self.tamanho:
          self.__senha.append(random.choice(self.__caracteres))

   def mostra_senha(self):
       print("".join(self.__senha))
class AnalisadordeSenha:
    def pedir_senha(self):
        self.senha = input('Digite a senha aqui: ')
    def analisador_senha(self):
        if len(self.senha) < 12:
            print('Senha fraca! Por segurança, utilize no mínimo 12 caracteres.')
        tem_maiuscula = False
        tem_minuscula = False
        tem_numero = False
        tem_simbolo = False

        for caractere in self.senha:

             if caractere.isupper():
                 tem_maiuscula = True

             elif caractere.islower():
                 tem_minuscula = True

             elif caractere.isdigit():
                tem_numero = True

             elif caractere in "!@#$%&*":
                tem_simbolo = True

        if tem_maiuscula and tem_minuscula and tem_numero and   tem_simbolo:
            print("Senha forte!")
        else:
             print("Senha fraca! Por segurança, utilize no mínimo 12 caracteres.")
class Maquina:
   def veja_maquina(self):
       

        
    





















app = MenuKali()
gerador = GeradorSenha()
senha = AnalisadordeSenha()
while True:
    app.menu()
    print()
    opcao = input('Qual a sua opção: ')

    if opcao == '1':
       gerador.pedir_tamanho()
       gerador.gerar()
       gerador.mostra_senha()
       input("\nPressione ENTER para voltar ao menu...")
    elif opcao == '2':
        senha.pedir_senha()
        senha.analisador_senha()
        input("\nPressione ENTER para voltar ao menu...")


       