import customtkinter as ctk

ctk.set_appearance_mode("System")  # Inicialmente baseado no sistema
ctk.set_default_color_theme("blue")

modo_atual = "light"  # Começa no modo claro (pode mudar se quiser)

# Função para alternar entre claro e escuro
def alternar_tema():
    global modo_atual
    if modo_atual == "light":
        ctk.set_appearance_mode("dark")
        modo_atual = "dark"
    else:
        ctk.set_appearance_mode("light")
        modo_atual = "light"

# Função para mostrar a tela de sucesso
def mostrar_sucesso():
    tela_sucesso = ctk.CTkToplevel()
    tela_sucesso.title("Sucesso")
    tela_sucesso.geometry("300x150")

    label = ctk.CTkLabel(tela_sucesso, text="Logado com sucesso!", font=("Arial", 16))
    label.pack(pady=20)

    def fechar_sucesso():
        tela_sucesso.destroy()

    botao_ok = ctk.CTkButton(tela_sucesso, text="OK", command=fechar_sucesso)
    botao_ok.pack(pady=10)

# Função do botão de login
def fazer_login():
    email = entry_email.get()
    senha = entry_senha.get()
    if email and senha:
        mostrar_sucesso()

# Criação da janela principal
app = ctk.CTk()
app.title("Tela de Login")
app.geometry("400x300")

# Campos de entrada
label_email = ctk.CTkLabel(app, text="Email:")
label_email.pack(pady=(20, 5))
entry_email = ctk.CTkEntry(app, width=250)
entry_email.pack()

label_senha = ctk.CTkLabel(app, text="Senha:")
label_senha.pack(pady=(15, 5))
entry_senha = ctk.CTkEntry(app, width=250, show="*")
entry_senha.pack()

# Botão de login
botao_login = ctk.CTkButton(app, text="Login", command=fazer_login)
botao_login.pack(pady=15)

# Botão para alternar o tema
botao_tema = ctk.CTkButton(app, text="Alternar Tema", command=alternar_tema)
botao_tema.pack(pady=5)

app.mainloop()
