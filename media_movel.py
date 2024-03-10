from deque import *

def calcular_media(lista, k):
    medias = Deque()
    for i in range(len(lista)):
        if i < k - 1:
            medias.add_last(None)  
        else:
            soma = sum(lista[i-(k-1):i+1])
            if i >= k - 1:
                media = soma / k
                medias.add_last(media)
    return medias

def ler_dados_arquivo(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        dados = []
        for linha in arquivo:
            if linha.strip():
                valores = [int(valor) for valor in linha.strip("[]\n").split(",")]
                dados.append(valores)
    return dados

def ler_dados_manualmente():
    dados = []
    num_listas = int(input("Digite o número de listas de volumes de tráfego: "))
    for i in range(num_listas):
        entrada = input(f"Digite a lista de volumes de tráfego {i+1}, separada por vírgulas: ")
        valores = [int(valor.strip()) for valor in entrada.split(",")]
        dados.append(valores)
    return dados

def escolher_valor_k():
    k = input("Digite o valor de K (pressione Enter para manter o valor padrão 7): ")
    if k == '':
        k = 7
    else:
        k = int(k)
    return k

opcao = int(input("Escolha a opção:\n 1 - Ler dados do arquivo\n 2 - Inserir dados manualmente\nOpção: "))

if opcao == 1:
    dados_trafego = ler_dados_arquivo("dados_trafego.txt")
elif opcao == 2:
    dados_trafego = ler_dados_manualmente()
else:
    print("Opção inválida. Saindo do programa.")
    exit()

k = escolher_valor_k()

if dados_trafego:
    with open("medias_moveis.txt", "w") as arquivo:
        for lista in dados_trafego:
            medias_moveis = calcular_media(lista, k)
            print("Médias móveis:", end=" ")
            while not medias_moveis.is_empty():
                media = medias_moveis.delete_first()
                if media is not None:
                    print(f"{media:.1f}", end=", ")
                    arquivo.write(f"{media:.1f}")
                else:
                    print("None", end=", ")
                    arquivo.write("None")
                if not medias_moveis.is_empty():
                    arquivo.write(", ")
            arquivo.write("\n")
            print() 

