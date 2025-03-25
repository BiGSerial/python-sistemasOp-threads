import json
import os


def salvar_tempos_json(tempos_seq, tempos_par, nome_arquivo):
    dados = {"sequencial": tempos_seq, "paralelo": tempos_par}
    os.makedirs("resultados", exist_ok=True)
    caminho = os.path.join("resultados", nome_arquivo)
    with open(caminho, "w") as f:
        json.dump(dados, f, indent=4)
    print(f"📁 Dados de tempo salvos em: {caminho}")


def carregar_tempos_json(nome_arquivo):
    with open(nome_arquivo, "r") as f:
        dados = json.load(f)
    return dados["sequencial"], dados["paralelo"]
