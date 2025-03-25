def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, "r") as f:
        return [int(linha.strip()) for linha in f if linha.strip()]
