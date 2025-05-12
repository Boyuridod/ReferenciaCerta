#pip install pyinstaller
#pyinstaller --onefile --noconsole --icon="D:\Desenvolvimento Projetos\Projetos em Python\GeradorDeReferenciaABNT\Images\LogoModerna.jpg" --name=GeradorDeReferenciaABNT TelaInicial.py

# Criar um setup de instalação
# https://youtu.be/5U-nBAfbSek

# TODO Otimizar os imports, ou seja, importar somente o que for necessário de verdade
from customtkinter import * #pip install customtkinter
from PIL import Image
from GerarReferencia import gerarReferencia
import pyperclip #pip install pyperclip
import webbrowser
import os
import sqlite3

# Função de limpar as entradas
def limpar():
    inputAutor1.delete(0, "end")
    inputTituloDoArtigo.delete(0, "end")
    inputNomeDoSite.delete(0, "end")
    inputAnoPublicacao.delete(0, "end")
    inputLink.delete(0, "end")  

# Função do botão "Gerar referência"
def botaoGerarOnClick():
    # Pega as entradas do usuário
    autor = inputAutor1.get()
    tituloDoArtigo = inputTituloDoArtigo.get()
    nomeDoSite = inputNomeDoSite.get()
    ano = inputAnoPublicacao.get()
    link = inputLink.get()
    # print(autor, tituloDoArtigo, nomeDoSite, ano, link)

    # Manda para a função que gera a referência
    referencia = gerarReferencia(autor, tituloDoArtigo, nomeDoSite, ano, link)

    # Habilita a edição, coloca a referência e desabilita edição
    textReferencia.configure(state = "normal")
    textReferencia.insert("end", referencia + "\n")
    textReferencia.configure(state = "disabled")

    # TODO Implementar try except
    # Tenta copiar para a área de transferência, se falhar da um alerta
    try:
        pyperclip.copy(referencia)

        copiado = "Copiado para a Área de Transferência!"

    except:
        copiado = "Não foi possível copiar para sua área de transferência. Tente copiar manualmente."

    # # Componente do aviso da cópia para a área de trasferência
    # labelTransferencia = CTkLabel(telaPrincipal, text=copiado)
    # labelTransferencia.grid(padx= 10, pady= 10)

    # Limpa todas as entradas para uma nova referencia
    limpar()

# Função que abre meu instagram
def instagramYuri():
    webbrowser.open("https://www.instagram.com/yuridsduarte/")

# TODO Colocar um link para meu linkedin

# TODO Python tem integração com SQL Local, posso fazer assim, chama sqlite
# https://youtu.be/Mdg1D-Kdmrw
# SQLITE https://youtu.be/jYUDi83tJXc?list=PLwsAoT89dh3pnuT7dGaG4vdxCpo5tJI8S
# # Função que aplica o novo tema
# def trocaTema():
#     print("Troca Tema")

# Carregando Configurações
modo = "dark"

#TODO Deixar a tela dinâmica
# Predefinições
telaPrincipal = CTk()
telaLargura = 700
telaAltura = 500
telaPrincipal.geometry(f"{telaLargura}x{telaAltura}")
telaPrincipal.title("Gerador de Referência ABNT")
telaPrincipal.grid_rowconfigure(0, weight = 0) # Impede a expansão da linha 0
telaPrincipal.grid_rowconfigure(1, weight = 0) # Impede a expansão da linha 0
telaPrincipal.grid_columnconfigure(0, weight = 1) # Permite a expansão da coluna 0
telaPrincipal.grid_columnconfigure(1, weight = 1) # Permite a expansão da coluna 1
telaPrincipal.grid_columnconfigure(2, weight = 1) # Permite a expansão da coluna 2
# telaPrincipal.iconphoto(True, CTkImage(Image.open("./Images/forma-de-meia-lua.png"), size=(26, 26)))
set_appearance_mode(modo)  # Modes: system (default), light, dark
set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# TODO Colocar uma maneira de gerar referencias impressas e referencias on-line
# Existe uma diferença em cada uma delas
# Vide: https://normas-abnt.espm.br/index.php?title=Um_autor

# Título
labelTitulo = CTkLabel(telaPrincipal, text = "Gerador de Referência ABNT")
labelTitulo.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 3)

# # Botão para troca de modo
# botaoModo = CTkButton(telaPrincipal, image = CTkImage(Image.open("./Images/forma-de-meia-lua.png"), size=(26, 26)),
#                       text = None, width = 10, height = 10, corner_radius = 10, command=trocaTema)
# botaoModo.grid(row = 0, column = 2, padx = 10, pady = 10, sticky = "e")

# Criação do TabView das Abas

tabviewAbas = CTkTabview(telaPrincipal)
tabviewAbas.grid(row = 1, column = 0, padx = 10, pady = 10, columnspan = 3, sticky="nsew")

tabviewAbas.add("Impresso")
tabviewAbas.add("Digital")

# Na aba do Referêncial Impresso

tabviewAbas.tab("Impresso").grid_columnconfigure(1, weight=1)

# TODO Aba do Referêncial Impresso

# Na aba do Referêncial Digital

tabviewAbas.tab("Digital").grid_columnconfigure(1, weight=1)

# # Componentes do Título do Artigo
labelTituloDoArtigo = CTkLabel(tabviewAbas.tab("Digital"), text = "Título do artigo:")
labelTituloDoArtigo.grid(row = 0, column = 0, padx = 10, pady = 10)
inputTituloDoArtigo = CTkEntry(tabviewAbas.tab("Digital"), placeholder_text = "Digite aqui")
inputTituloDoArtigo.grid(row = 0, column = 1, padx = 10, pady = 10, columnspan = 2, sticky = "nsew")

# # Componentes do Nome do Site
labelNomeDoSite = CTkLabel(tabviewAbas.tab("Digital"), text="Nome do site:")
labelNomeDoSite.grid(row = 1, column = 0, padx = 10, pady = 10)
inputNomeDoSite = CTkEntry(tabviewAbas.tab("Digital"), placeholder_text = "Digite aqui")
inputNomeDoSite.grid(row = 1, column = 1, columnspan = 2, padx = 10, pady = 10, sticky="nsew")

# # Componentes do Ano de Publicação
labelAnoPublicacao = CTkLabel(tabviewAbas.tab("Digital"), text="Ano da publicação:")
labelAnoPublicacao.grid(row = 2, column = 0, padx = 10, pady = 10)
inputAnoPublicacao = CTkEntry(tabviewAbas.tab("Digital"), placeholder_text = "Digite aqui")
inputAnoPublicacao.grid(row = 2, column = 1, columnspan = 2, padx = 10, pady = 10, sticky="nsew")

# # Componentes do Link
labelLink = CTkLabel(tabviewAbas.tab("Digital"), text="Link do artigo:")
labelLink.grid(row = 3, column = 0, padx = 10, pady = 10)
inputLink = CTkEntry(tabviewAbas.tab("Digital"), placeholder_text = "https://exemplo.com.br")
inputLink.grid(row = 3, column = 1, columnspan = 2, padx = 10, pady = 10, sticky="nsew")

# # Componentes do Autor
autores = 0
labelAutor1 = CTkLabel(tabviewAbas.tab("Digital"), text="Nome do autor(a):")
labelAutor1.grid(row = 4, column = 0, padx = 10, pady = 10)
inputAutor1 = CTkEntry(tabviewAbas.tab("Digital"), placeholder_text = "SOBRENOME, Nome")
inputAutor1.grid(row = 4, column = 1, columnspan = 2, padx = 10, pady = 10, sticky="nsew")

# Fim tabView das Abas

# TODO Colocar uma forma de ter mais de um autor
# Posso fazer tipo um botão que adiciona e subtrai pra dizer a quantidade



# Componente do Botão
botaoGerar = CTkButton(telaPrincipal, text="Gerar referência", command=botaoGerarOnClick)
botaoGerar.grid(row = 6, column = 0, columnspan = 3, padx = 10, pady = 10, sticky="n")

# Área da resposta
telaPrincipal.grid_rowconfigure(7, weight = 1)
textReferencia = CTkTextbox(telaPrincipal, corner_radius=10)
textReferencia.grid(row = 7, column = 0, columnspan = 3, padx = 10, pady = 10, sticky = "nsew")
textReferencia.configure(state = "disabled")

# Botão do Desenvolvedor
botaoYuri = CTkButton(telaPrincipal, text = "@yuridsduarte", fg_color = "transparent", hover = False, width = 0, command = instagramYuri)
botaoYuri.grid(row = 8, column = 2, padx = 10, sticky = "e")

#Chamar a Tela
telaPrincipal.mainloop()