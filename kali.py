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
            return
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
             print("❌ Senha fraca! Ela deve conter:")
             print("- Pelo menos uma letra maiúscula")
             print("- Pelo menos uma letra minúscula")
             print("- Pelo menos um número")
             print("- Pelo menos um símbolo")
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
       s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
       s.connect(("8.8.8.8", 80))
       print(s.getsockname()[0])
       s.close()
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
        print('Você será redirecinado para um serviço especializado que realizar a um teste mais completo')
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
import sys
import io
import contextlib
import builtins
import tkinter as tk
from tkinter import messagebox, simpledialog


def capturar(funcao, entrada=None):
    buffer = io.StringIO()
    input_original = builtins.input
    if entrada is not None:
        builtins.input = lambda *args: entrada
    try:
        with contextlib.redirect_stdout(buffer):
            funcao()
    finally:
        builtins.input = input_original
    return buffer.getvalue()


class InterfaceKali:
    BG = "#0d1117"
    PAINEL = "#161b22"
    BOTAO = "#21262d"
    BOTAO_HOVER = "#30363d"
    VERDE = "#3fb950"
    TEXTO = "#e6edf3"

    def __init__(self, root):
        self.root = root
        root.title("Menu Kali")
        root.geometry("860x540")
        root.minsize(720, 460)
        root.configure(bg=self.BG)

        tk.Label(root, text="MENU KALI", font=("Consolas", 22, "bold"),
                 bg=self.BG, fg=self.VERDE).pack(pady=(14, 6))

        corpo = tk.Frame(root, bg=self.BG)
        corpo.pack(fill="both", expand=True, padx=14, pady=(0, 14))

        # ----- coluna dos botões -----
        lateral = tk.Frame(corpo, bg=self.PAINEL)
        lateral.pack(side="left", fill="y", padx=(0, 12))

        botoes = [
            ("🔑  Gerar Senha Segura", self.opcao_1),
            ("🛡️  Analisar Força da Senha", self.opcao_2),
            ("💻  Informações da Máquina", self.opcao_3),
            ("🔍  Arquivos Suspeitos", self.opcao_4),
            ("📜  Histórico de Ações", self.opcao_5),
            ("🚪  Sair", self.opcao_6),
        ]
        for texto, comando in botoes:
            b = tk.Button(lateral, text=texto, command=comando, anchor="w",
                          font=("Segoe UI", 11), bg=self.BOTAO, fg=self.TEXTO,
                          activebackground=self.BOTAO_HOVER, activeforeground=self.TEXTO,
                          relief="flat", bd=0, padx=16, pady=10, width=26, cursor="hand2")
            b.pack(fill="x", padx=10, pady=5)
            b.bind("<Enter>", lambda e, w=b: w.config(bg=self.BOTAO_HOVER))
            b.bind("<Leave>", lambda e, w=b: w.config(bg=self.BOTAO))

        direita = tk.Frame(corpo, bg=self.PAINEL)
        direita.pack(side="left", fill="both", expand=True)

        self.saida = tk.Text(direita, font=("Consolas", 11), bg=self.PAINEL,
                             fg=self.TEXTO, relief="flat", wrap="word",
                             padx=14, pady=14, state="disabled")
        barra = tk.Scrollbar(direita, command=self.saida.yview)
        self.saida.config(yscrollcommand=barra.set)
        barra.pack(side="right", fill="y")
        self.saida.pack(side="left", fill="both", expand=True)

        self.escrever("Bem-vindo ao Menu Kali!\n\nEscolha uma opção ao lado.")

    def escrever(self, texto):
        self.saida.config(state="normal")
        self.saida.delete("1.0", "end")
        self.saida.insert("end", texto)
        self.saida.config(state="disabled")

    def registrar(self, op):
        global opcao                
        opcao = op
        historico.adicionar()


    def opcao_1(self):
        tam = simpledialog.askinteger(
            "Gerar Senha", "Tamanho da sua senha (12 a 32):",
            parent=self.root, minvalue=12, maxvalue=32)
        if tam is None:
            return
        gerador.tamanho = tam
        gerador.gerar()
        resultado = capturar(gerador.mostra_senha).strip()
        self.root.clipboard_clear()
        self.root.clipboard_append(resultado)
        self.escrever("Senha gerada:\n\n" + resultado +
                      "\n\n(copiada para a área de transferência)")
        self.registrar('1')

    def opcao_2(self):
        s = simpledialog.askstring("Analisar Senha", "Digite a senha aqui:",
                                   parent=self.root, show="*")
        if s is None:
            return
        senha.senha = s
        self.escrever(capturar(senha.analisador_senha))
        self.registrar('2')

    def opcao_3(self):
        try:
            texto = capturar(maquina.veja_maquina)
        except Exception as erro:
            texto = f"Não foi possível obter as informações:\n{erro}"
        self.escrever(texto)
        self.registrar('3')

    def opcao_4(self):
        aviso = ("O Menu Kali possui uma ferramenta de análise online para "
                 "verificar possíveis problemas de segurança.\n\n"
                 "Você será redirecionado para um serviço especializado.\n\n"
                 "Não envie arquivos confidenciais.\n\nDeseja continuar?")
        if messagebox.askyesno("Analisador de arquivos", aviso):
            capturar(seguranca.verificao_de_seguranca, entrada='s')
            self.escrever("Abrindo o serviço de análise no seu navegador...")
        else:
            self.escrever("OK! Você não será redirecionado. Volte ao menu!")
        self.registrar('4')

    def opcao_5(self):
        texto = capturar(historico.mostrar).strip()
        self.escrever(texto if texto else "Nenhuma ação registrada ainda.")

    def opcao_6(self):
        self.registrar('6')
        messagebox.showinfo("Menu Kali", "Obrigado por usar o Menu Kali, volte sempre.")
        self.root.destroy()


def iniciar_interface():
    root = tk.Tk()
    InterfaceKali(root)
    root.mainloop()
if "--terminal" not in sys.argv:
    iniciar_interface()
else:
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
