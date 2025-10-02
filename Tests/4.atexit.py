import atexit

def limpar():
    print("🔚 Finalizando... limpando recursos!")

atexit.register(limpar)

print("Rodando o programa...")

input()