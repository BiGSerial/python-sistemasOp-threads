import matplotlib.pyplot as plt
import os


def gerar_boxplot(
    tempos_seq, tempos_par, titulo, nome_arquivo="boxplot.png", nomes_bases=None
):
    fig, ax = plt.subplots(figsize=(12, 6))
    dados = tempos_seq + tempos_par

    # Se nomes reais forem fornecidos, use eles com prefixos
    if nomes_bases:
        labels = [f"s-{nome}" for nome in nomes_bases] + [
            f"p-{nome}" for nome in nomes_bases
        ]
    else:
        # fallback: nomes genéricos
        labels = [f"S{i+1}" for i in range(len(tempos_seq))] + [
            f"P{i+1}" for i in range(len(tempos_par))
        ]

    # Criação do boxplot com cores
    box = ax.boxplot(dados, patch_artist=True)
    for i, patch in enumerate(box["boxes"]):
        patch.set_facecolor("lightblue" if i < len(tempos_seq) else "lightgreen")

    # Títulos e labels
    ax.set_title(titulo)
    ax.set_xlabel("Arquivos")
    ax.set_ylabel("Tempo (ms)")
    ax.set_xticklabels(labels, rotation=45)
    plt.grid(True)
    plt.tight_layout()

    # Salvar figura
    os.makedirs("resultados", exist_ok=True)
    caminho = os.path.join("resultados", nome_arquivo)
    plt.savefig(caminho)
    print(f"📊 Gráfico salvo em: {caminho}")
    plt.close()
