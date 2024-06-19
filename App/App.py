#Biblioteca Utilizada
import customtkinter as ctk 
from tkinter import Frame, messagebox, ttk
import mysql.connector


#Definindo Tela de login
tela_login = ctk.CTk()
tela_login._set_appearance_mode("System")
tela_login.geometry("500x500")
tela_login.title("Janela de Login")
tela_login.maxsize(width=500, height=500)
tela_login.minsize(width=500, height=500)


#Inicio Funções

# Função para fazer login
def login(usuario, senha):
    try:
        # Conexão com o banco de dados
        conn = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="",
            database="admins"
        )

        cursor = conn.cursor()

        consulta = "SELECT * FROM admins WHERE Usuario = %s AND Senha = %s"
        dados = (usuario, senha)

        cursor.execute(consulta, dados)

        if cursor.fetchone():
            return True
        else:
            return False

    except mysql.connector.Error as erro:
        print("Erro ao conectar ao MySQL:", erro)
        return False

    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            
# Função para validar o login
def validar_login():
    usuario = input_usuario.get()
    senha = input_senha.get()

    if login(usuario, senha):
        messagebox.showinfo("Login", "Login bem-sucedido!")
        print("Login bem-sucedido!")
        return True
    else:
        messagebox.showerror("Login", "Login falhou. Verifique suas credenciais.")
        print("Verifique a conexão com o banco de dados e Suas Credenciais")
        return False
    
# Definindo tela de opções
hud_selecao = ctk.CTkToplevel(tela_login)
hud_selecao.title("Selecione o que Deseja")
hud_selecao.geometry("700x700")

# Configurando a grade
hud_selecao.grid_rowconfigure(0, weight=1)
hud_selecao.grid_rowconfigure(1, weight=1)
hud_selecao.grid_rowconfigure(2, weight=1)
hud_selecao.grid_rowconfigure(3, weight=1)
hud_selecao.grid_columnconfigure(0, weight=1)
hud_selecao.grid_columnconfigure(1, weight=1)

# Widgets Hud_seleção
botao_usuarios = ctk.CTkButton(hud_selecao, width=200, height=200, text="Usuários")
botao_usuarios.grid(row=0, column=0, padx=10, pady=10)

botao_adm = ctk.CTkButton(hud_selecao, width=200, height=200, text="Admin")
botao_adm.grid(row=0, column=1, padx=10, pady=10)

botao_produtos = ctk.CTkButton(hud_selecao, width=200, height=200, text="Produtos")
botao_produtos.grid(row=1, column=0, padx=10, pady=10)

botao_cadastro = ctk.CTkButton(hud_selecao, width=200, height=200, text="Cadastro")
botao_cadastro.grid(row=1, column=1, padx=10, pady=10)

# Tela Login
label_usuario = ctk.CTkLabel(tela_login, width=250, height=50, text="Usuário")
label_usuario.pack(pady=10)

input_usuario = ctk.CTkEntry(tela_login, width=250, height=50, fg_color="white")
input_usuario.pack(pady=10)

label_senha = ctk.CTkLabel(tela_login, width=250, height=50, text="Senha")
label_senha.pack(pady=10)

input_senha = ctk.CTkEntry(tela_login, width=250, height=50, fg_color="white")
input_senha.pack(pady=10)

button_entrar = ctk.CTkButton(tela_login, text="Entrar!", fg_color="black", command=validar_login)
button_entrar.place(x=175, y=330)

tela_login.mainloop()