import customtkinter as ctk

# Configura o tema
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Janela principal
root = ctk.CTk()
root.geometry("400x400")
root.title("Exemplo de Scroll no CustomTkinter")

# Frame com scroll
scroll_frame = ctk.CTkScrollableFrame(root, width=380, height=350)
scroll_frame.pack(padx=10, pady=10, fill="both", expand=True)

# Adicionando vários widgets dentro do scroll
for i in range(30):
    label = ctk.CTkLabel(scroll_frame, text=f"Item {i+1}", font=("Arial", 16))
    label.pack(pady=5)

root.mainloop()
