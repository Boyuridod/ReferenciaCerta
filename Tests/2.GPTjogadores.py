import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Janela principal
app = ctk.CTk()
app.title("Nome do jogador")
app.geometry("400x400")

jogadores = []
max_jogadores = 4
frame_jogadores = ctk.CTkFrame(app)
frame_jogadores.pack(pady=10)

# Função para atualizar o título e os labels
def atualizar_jogadores():
    for widget in frame_jogadores.winfo_children():
        widget.destroy()

    qtd = len(jogadores)
    if qtd > 1:
        app.title("Nomes dos jogadores")
    else:
        app.title("Nome do jogador")

    for i in range(qtd):
        label = ctk.CTkLabel(frame_jogadores, text=f"Jogador {i+1}")
        label.pack(pady=2)

# Adicionar jogador
def adicionar_jogador():
    if len(jogadores) < max_jogadores:
        jogadores.append(f"Jogador {len(jogadores)+1}")
        atualizar_jogadores()

# Remover jogador
def remover_jogador():
    if len(jogadores) > 1:
        jogadores.pop()
        atualizar_jogadores()

# Ao clicar em "Jogar"
def jogar():
    popup = ctk.CTkToplevel()
    popup.title("Pronto!")
    popup.geometry("250x120")

    msg = ctk.CTkLabel(popup, text="Bom jogo!", font=("Arial", 18))
    msg.pack(pady=20)

    ok_button = ctk.CTkButton(popup, text="OK", command=popup.destroy)
    ok_button.pack()

# Botões + e -
botoes_frame = ctk.CTkFrame(app)
botoes_frame.pack(pady=10)

btn_add = ctk.CTkButton(botoes_frame, text="+ Jogador", command=adicionar_jogador)
btn_add.grid(row=0, column=0, padx=10)

btn_remove = ctk.CTkButton(botoes_frame, text="- Jogador", command=remover_jogador)
btn_remove.grid(row=0, column=1, padx=10)

# Botão jogar
btn_jogar = ctk.CTkButton(app, text="Jogar", command=jogar)
btn_jogar.pack(pady=20)

# Começa com 1 jogador
jogadores.append("Jogador 1")
atualizar_jogadores()

app.mainloop()
