from datetime import date

# Função que retorna o mês já formatado
def getMes(n):

    # Vetor de meses
    mes = ["Jan.", "Fev.", "Mar.", "Abr.", "Mai.", "Jun.", "Jul.", "Ago.", "Set.", "Out.", "Nov.", "Dez."]

    return mes[n]

# Recebendo as informações da entrada
def gerarReferenciaDigital(autores, tituloDoArtigo, nomeDoSite, ano, link):
    # Gerando a data
    data = str(date.today().day) + " " + getMes(date.today().month - 1) + " " + str(date.today().year)

    # Criando a referência perfeita
    referencia = f"{autores}. {tituloDoArtigo}. {nomeDoSite}, {ano}. Disponível em: {link}. Acesso em: {data}."

    # Retorno da referência
    return referencia

def gerarReferenciaImpressa(autores, nomeDoLivro, edicaoDoLivro, editora, anoPublicacao, paginas):

    # Criando a referência perfeita
    referencia = f"{autores}. {nomeDoLivro}. {edicaoDoLivro}. ed. {editora}, {anoPublicacao}p.{paginas}"

    # Retorno da referência
    return referencia