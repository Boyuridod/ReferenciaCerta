from customtkinter import *

app = CTk()
app.geometry("600x400")
set_appearance_mode("dark")

# Lista para armazenar os inputs de autores
entrada_autores = []

# Frame/tab onde os inputs serão adicionados
aba_digital = CTkFrame(app)
aba_digital.pack(fill="both", expand=True, padx=20, pady=20)

# Função para adicionar um novo autor
def adicionar_autor():
    linha = len(entrada_autores) + 4  # começa da linha 4

    label = CTkLabel(aba_digital, text=f"Nome do autor(a) {linha - 3}:")
    label.grid(row=linha, column=0, padx=10, pady=5, sticky="w")

    entry = CTkEntry(aba_digital, placeholder_text="SOBRENOME, Nome")
    entry.grid(row=linha, column=1, columnspan=2, padx=10, pady=5, sticky="nsew")

    entrada_autores.append(entry)

    # Agendar verificação deste novo campo
    checar_entrada(entry)

# Função que verifica se a entrada está preenchida e adiciona outra
def checar_entrada(entry):
    def verificar():
        if entry.get().strip() != "":
            # Verifica se já é o último campo
            if entry == entrada_autores[-1] and len(entrada_autores) < 10:
                adicionar_autor()
        else:
            # Continua verificando até preencher
            app.after(300, verificar)

    verificar()

# Adiciona o primeiro autor ao iniciar
adicionar_autor()

app.mainloop()
