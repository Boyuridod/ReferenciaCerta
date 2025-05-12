# # Botão para troca de modo
# botaoModo = CTkButton(telaPrincipal, image = CTkImage(Image.open("./Images/forma-de-meia-lua.png"), size=(26, 26)),
#                       text = None, width = 10, height = 10, corner_radius = 10, command=trocaTema)
# botaoModo.grid(row = 0, column = 2, padx = 10, pady = 10, sticky = "e")

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