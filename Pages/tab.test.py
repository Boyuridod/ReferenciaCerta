# TODO Otimizar os imports, ou seja, importar somente o que for necessário de verdade
from customtkinter import *
from PIL import Image
from GerarReferencia import gerarReferencia
import pyperclip
import webbrowser
import os
import sqlite3

# Listas separadas para autores de cada aba (agora guardam (label, entry))
autores_digital = []
autores_impresso = []

# Função que carrega os autores
def labelAutores(pagina, lista_autores):
    linha = len(lista_autores) + 4
    labelAutor = CTkLabel(tabviewAbas.tab(pagina), text=f"Nome do autor(a) {linha - 3}:")
    labelAutor.grid(row=linha, column=0, padx=10, pady=10)
    inputAutor = CTkEntry(tabviewAbas.tab(pagina), placeholder_text="SOBRENOME, Nome")
    inputAutor.grid(row=linha, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")

    lista_autores.append((labelAutor, inputAutor))

    getAutor(inputAutor, pagina, lista_autores)

# Verifica se autor foi preenchido para adicionar novos até 5
def getAutor(inputAutor, pagina, lista_autores):
    def verificar():
        if inputAutor.get().strip() != "":
            if inputAutor == lista_autores[-1][1] and len(lista_autores) < 5:
                labelAutores(pagina, lista_autores)
        else:
            telaPrincipal.after(300, verificar)

    verificar()

# Remove autores extras e limpa o primeiro
def limparAutores():
    for i, (label, entry) in enumerate(autores_digital):
        if i == 0:
            entry.delete(0, "end")
        else:
            label.destroy()
            entry.destroy()
    del autores_digital[1:]

    for i, (label, entry) in enumerate(autores_impresso):
        if i == 0:
            entry.delete(0, "end")
        else:
            label.destroy()
            entry.destroy()
    del autores_impresso[1:]

# Função de limpar as entradas
def limpar():
    limparAutores()
    inputTituloDoArtigo.delete(0, "end")
    inputNomeDoSite.delete(0, "end")
    inputAnoPublicacao.delete(0, "end")
    inputLink.delete(0, "end")

# Função do botão "Gerar referência"
def botaoGerarOnClick():
    autor = "VAZIO"
    tituloDoArtigo = inputTituloDoArtigo.get()
    nomeDoSite = inputNomeDoSite.get()
    ano = inputAnoPublicacao.get()
    link = inputLink.get()

    referencia = gerarReferencia(autor, tituloDoArtigo, nomeDoSite, ano, link)

    textReferencia.configure(state="normal")
    textReferencia.insert("end", referencia + "\n")
    textReferencia.configure(state="disabled")

    try:
        pyperclip.copy(referencia)
        copiado = "Copiado para a Área de Transferência!"
    except:
        copiado = "Não foi possível copiar para sua área de transferência. Tente copiar manualmente."

    limpar()

def instagramYuri():
    webbrowser.open("https://www.instagram.com/yuridsduarte/")

modo = "dark"

# Predefinições
telaPrincipal = CTk()
telaLargura = 700
telaAltura = 500
telaPrincipal.geometry(f"{telaLargura}x{telaAltura}")
telaPrincipal.title("Gerador de Referência ABNT")
telaPrincipal.grid_rowconfigure(0, weight=0)
telaPrincipal.grid_rowconfigure(1, weight=0)
telaPrincipal.grid_columnconfigure(0, weight=1)
telaPrincipal.grid_columnconfigure(1, weight=1)
telaPrincipal.grid_columnconfigure(2, weight=1)
set_appearance_mode(modo)
set_default_color_theme("blue")

labelTitulo = CTkLabel(telaPrincipal, text="Gerador de Referência ABNT")
labelTitulo.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

tabviewAbas = CTkTabview(telaPrincipal)
tabviewAbas.grid(row=1, column=0, padx=10, pady=10, columnspan=3, sticky="nsew")

tabviewAbas.add("Impresso")
tabviewAbas.add("Digital")

tabviewAbas.tab("Impresso").grid_columnconfigure(1, weight=1)

labelNomeDoLivro = CTkLabel(tabviewAbas.tab("Impresso"), text="Nome do livro:")
labelNomeDoLivro.grid(row=0, column=0, padx=10, pady=10)
inputNomeDoLivro = CTkEntry(tabviewAbas.tab("Impresso"), placeholder_text="Digite aqui")
inputNomeDoLivro.grid(row=0, column=1, padx=10, pady=10, columnspan=2, sticky="nsew")

labelEdicaoDoLivro = CTkLabel(tabviewAbas.tab("Impresso"), text="Edição do lívro:")
labelEdicaoDoLivro.grid(row=1, column=0, padx=10, pady=10)
inputEdicaoDoLivro = CTkEntry(tabviewAbas.tab("Impresso"), placeholder_text="Digite aqui")
inputEdicaoDoLivro.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")

labelEditora = CTkLabel(tabviewAbas.tab("Impresso"), text="Editora:")
labelEditora.grid(row=2, column=0, padx=10, pady=10)
inputEditora = CTkEntry(tabviewAbas.tab("Impresso"), placeholder_text="Digite aqui")
inputEditora.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")

labelAnoPublicacaoImpresso = CTkLabel(tabviewAbas.tab("Impresso"), text="Ano de publicação:")
labelAnoPublicacaoImpresso.grid(row=3, column=0, padx=10, pady=10)
inputAnoPublicacaoImpresso = CTkEntry(tabviewAbas.tab("Impresso"), placeholder_text="Digite aqui")
inputAnoPublicacaoImpresso.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")

labelPaginas = CTkLabel(tabviewAbas.tab("Impresso"), text="Páginas:")
labelPaginas.grid(row=4, column=0, padx=10, pady=10)
inputPaginas = CTkEntry(tabviewAbas.tab("Impresso"), placeholder_text="xx-xx")
inputPaginas.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")

labelAutores("Impresso", autores_impresso)

tabviewAbas.tab("Digital").grid_columnconfigure(1, weight=1)

labelTituloDoArtigo = CTkLabel(tabviewAbas.tab("Digital"), text="Título do artigo:")
labelTituloDoArtigo.grid(row=0, column=0, padx=10, pady=10)
inputTituloDoArtigo = CTkEntry(tabviewAbas.tab("Digital"), placeholder_text="Digite aqui")
inputTituloDoArtigo.grid(row=0, column=1, padx=10, pady=10, columnspan=2, sticky="nsew")

labelNomeDoSite = CTkLabel(tabviewAbas.tab("Digital"), text="Nome do site:")
labelNomeDoSite.grid(row=1, column=0, padx=10, pady=10)
inputNomeDoSite = CTkEntry(tabviewAbas.tab("Digital"), placeholder_text="Digite aqui")
inputNomeDoSite.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")

labelAnoPublicacao = CTkLabel(tabviewAbas.tab("Digital"), text="Ano da publicação:")
labelAnoPublicacao.grid(row=2, column=0, padx=10, pady=10)
inputAnoPublicacao = CTkEntry(tabviewAbas.tab("Digital"), placeholder_text="Digite aqui")
inputAnoPublicacao.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")

labelLink = CTkLabel(tabviewAbas.tab("Digital"), text="Link do artigo:")
labelLink.grid(row=3, column=0, padx=10, pady=10)
inputLink = CTkEntry(tabviewAbas.tab("Digital"), placeholder_text="https://exemplo.com.br")
inputLink.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")

labelAutores("Digital", autores_digital)

botaoGerar = CTkButton(telaPrincipal, text="Gerar referência", command=botaoGerarOnClick)
botaoGerar.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="n")

telaPrincipal.grid_rowconfigure(4, weight=1)
textReferencia = CTkTextbox(telaPrincipal, corner_radius=10)
textReferencia.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
textReferencia.configure(state="disabled")

botaoYuri = CTkButton(telaPrincipal, text="@yuridsduarte", fg_color="transparent", hover=False, width=0, command=instagramYuri)
botaoYuri.grid(row=5, column=2, padx=10, sticky="e")

# Chamar a Tela
telaPrincipal.mainloop()
