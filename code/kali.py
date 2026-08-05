import random
import platform
import socket
import os
import shutil
import tempfile
import webbrowser
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
        print('[ 4 ] Analisador De Arquivos Suspeitos')
        print('[ 5 ] Histórico De Ações')
        print('[ 6 ] Sair')
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
       print()
       print('========= INFORMAÇÕES DO SISTEMA =========')
       print()
       print('Sistema Operacional:')
       print(platform.system())
       print()
       print('Versão:')
       print(platform.freedesktop_os_release()["PRETTY_NAME"])
       print()
       print('Processador:')
       print(platform.processor())
       print()
       print('IP local:')
       print(socket.gethostbyname(socket.gethostbyname()))
       print()
       print('CPU:')
       with open("/proc/cpuinfo", "r") as arquivo:
        for linha in arquivo:
            if "model name" in linha:
               print(linha.split(":")[1].strip())
               break
       print()
       print('Espaço livre:')
       total, usado, livre = shutil.disk_usage("/")

       print(f"Total: {total // (1024**3)} GB")
       print(f"Usado: {usado // (1024**3)} GB")
       print(f"Livre: {livre // (1024**3)} GB")
       print()
       print('===========================================')
class Seguranca:
    def verificao_de_seguranca(self):
        print()
        print('Analisador de arquivos:')
        print()
        print('O Menu Kali possui uma ferramenta de análise online para verificar possíveis problemas de segurança.')
        print('Você será redirecinado para um serviço especializado que realizar a um teste mais completo.')
        print()
        print('Não envie arquivos confidenciais.')
        print()
        self.oopcao=input('Deseja continuar? [S/N]')
        print()
        if self.oopcao == 's'.lower():
            webbrowser.open("https://virusscan.jotti.org/pt-br")
        else:
            print('OK! vc não será redirecionado. Volte ao menu!')
class Historico:

    def __init__(self):
        self.registros = []

    def adicionar(self,):

        if opcao == '1':
            self.registros.append('Gerou senha.')

        elif opcao == '2':
            self.registros.append('Testou força da senha.')

        elif opcao == '3':
            self.registros.append('Viu informações da máquina.')

        elif opcao == '4':
            self.registros.append('Analisou arquivo em site.')

        elif opcao == '6':
            self.registros.append('Saiu do menu.')

    def mostrar(self):
        for registro in self.registros:
            print(registro)
app = MenuKali()
gerador = GeradorSenha()
senha = AnalisadordeSenha()
maquina= Maquina()
seguranca= Seguranca()
historico= Historico()
while True:
    app.menu()
    print()
    opcao = input('Qual a sua opção: ')
    if opcao not in ("1", "2", "3", "4", "5", "6"):
        print("\n Opção inválida! Escolha uma opção entre 1 e 6.")
        input("\nPressione ENTER para continuar...")
        continue
    if opcao == '1':
       gerador.pedir_tamanho()
       gerador.gerar()
       gerador.mostra_senha()
       historico.adicionar()
       input("\nPressione ENTER para voltar ao menu...")
       print()
    elif opcao == '2':
        senha.pedir_senha()
        senha.analisador_senha()
        historico.adicionar()
        input("\nPressione ENTER para voltar ao menu...")
        print()
    elif opcao == '3':
        maquina.veja_maquina()
        historico.adicionar()
        input("\nPressione ENTER para voltar ao menu...")
        print()
    elif opcao == '4':
       seguranca.verificao_de_seguranca()
       historico.adicionar()
       input("\nPressione ENTER para voltar ao menu...")
       print()
    elif opcao == '5':
        print()
        historico.mostrar()
        input("\nPressione ENTER para voltar ao menu...")
        print()
    elif opcao == '6':
        print('Obrigado por usar o Menu Kali, volte sempre.')
        historico.adicionar()
        break
