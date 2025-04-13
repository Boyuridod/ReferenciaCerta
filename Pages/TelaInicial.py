#pip install pyinstaller
#pyinstaller --onefile --noconsole --icon="D:\Desenvolvimento Projetos\Projetos em Python\GeradorDeReferenciaABNT\Images\LogoModerna.jpg" --name=GeradorDeReferenciaABNT TelaInicial.py

# TODO Criar um setup de instalação

from customtkinter import * #pip install customtkinter
from PIL import Image
from GerarReferencia import gerarReferencia
import pyperclip #pip install pyperclip
import webbrowser

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

# Predefinições
telaPrincipal = CTk()
telaLargura = 700
telaAltura = 500
telaPrincipal.geometry(f"{telaLargura}x{telaAltura}")
telaPrincipal.title("Gerador de Referência ABNT")
telaPrincipal.grid_rowconfigure(0, weight = 0) # Impede a expansão da linha 0
telaPrincipal.grid_columnconfigure(1, weight = 1) # Permitir a expansão da coluna 1
# telaPrincipal.iconphoto(True, CTkImage(Image.open("./Images/forma-de-meia-lua.png"), size=(26, 26)))
set_appearance_mode("System")  # Modes: system (default), light, dark
set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# TODO Colocar uma maneira de gerar referencias impressas e referencias on-line
# Existe uma diferença em cada uma delas
# Vide: https://normas-abnt.espm.br/index.php?title=Um_autor

# Título
labelTitulo = CTkLabel(telaPrincipal, text = "Gerador de Referência ABNT")
labelTitulo.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 3)

# TODO Implementar a troca de modo escuro e claro salvando tudo em um json

# Botão para troca de modo
botaoModo = CTkButton(telaPrincipal, image = CTkImage(Image.open("./Images/forma-de-meia-lua.png"), size=(26, 26)),
                      text = None, width = 10, height = 10, corner_radius = 10)
botaoModo.grid(row = 0, column = 2, padx = 10, pady = 10, sticky = "e")

# Componentes do Título do Artigo
labelTituloDoArtigo = CTkLabel(telaPrincipal, text = "Título do artigo:")
labelTituloDoArtigo.grid(row = 1, column = 0, padx = 10, pady = 10)
inputTituloDoArtigo = CTkEntry(telaPrincipal, placeholder_text = "Digite aqui")
inputTituloDoArtigo.grid(row = 1, column = 1, columnspan = 2, padx = 10, pady = 10, sticky="nsew")

# Componentes do Nome do Site
labelNomeDoSite = CTkLabel(telaPrincipal, text="Nome do site:")
labelNomeDoSite.grid(row = 2, column = 0, padx = 10, pady = 10)
inputNomeDoSite = CTkEntry(telaPrincipal, placeholder_text = "Digite aqui")
inputNomeDoSite.grid(row = 2, column = 1, columnspan = 2, padx = 10, pady = 10, sticky="nsew")

# Componentes do Ano de Publicação
labelAnoPublicacao = CTkLabel(telaPrincipal, text="Ano da publicação:")
labelAnoPublicacao.grid(row = 3, column = 0, padx = 10, pady = 10)
inputAnoPublicacao = CTkEntry(telaPrincipal, placeholder_text = "Digite aqui")
inputAnoPublicacao.grid(row = 3, column = 1, columnspan = 2, padx = 10, pady = 10, sticky="nsew")

# Componentes do Link
labelLink = CTkLabel(telaPrincipal, text="Link do artigo:")
labelLink.grid(row = 4, column = 0, padx = 10, pady = 10)
inputLink = CTkEntry(telaPrincipal, placeholder_text = "https://exemplo.com.br")
inputLink.grid(row = 4, column = 1, columnspan = 2, padx = 10, pady = 10, sticky="nsew")

# Componentes do Autor
autores = 0
labelAutor1 = CTkLabel(telaPrincipal, text="Nome do autor(a):")
labelAutor1.grid(row = 5, column = 0, padx = 10, pady = 10)
inputAutor1 = CTkEntry(telaPrincipal, placeholder_text = "SOBRENOME, Nome")
inputAutor1.grid(row = 5, column = 1, columnspan = 2, padx = 10, pady = 10, sticky="nsew")

# TODO Colocar uma forma de ter mais de um autor
# Posso fazer tipo um botão que adiciona e subtrai pra dizer a quantidade

# Componente do Botão
botaoGerar = CTkButton(telaPrincipal, text="Gerar referência", command=botaoGerarOnClick)
botaoGerar.grid(row = 6, column = 0, columnspan = 3, padx = 10, pady = 10, sticky="n")

# Área da resposta
textReferencia = CTkTextbox(telaPrincipal, corner_radius=10)
textReferencia.grid(row = 7, column = 0, columnspan = 3, padx = 10, pady = 10, sticky = "nsew")
textReferencia.configure(state = "disabled")
telaPrincipal.grid_rowconfigure(7, weight = 1)

# Botão do Desenvolvedor
botaoYuri = CTkButton(telaPrincipal, text = "@yuridsduarte", fg_color = "transparent", hover = False, width = 0, command = instagramYuri)
botaoYuri.grid(row = 8, column = 2, padx = 10, sticky = "e")

#Chamar a Tela
telaPrincipal.mainloop()