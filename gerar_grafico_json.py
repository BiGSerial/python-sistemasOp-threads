from app.utils import carregar_tempos_json
from app.graficos import gerar_boxplot

if __name__ == "__main__":
    # Listas pequenas
    tempos_seq_peq, tempos_par_peq = carregar_tempos_json(
        "resultados/tempos_pequenas.json"
    )
    gerar_boxplot(
        tempos_seq_peq,
        tempos_par_peq,
        "Boxplot - Listas Pequenas",
        "boxplot_pequenas.png",
    )

    # Listas grandes
    tempos_seq_grd, tempos_par_grd = carregar_tempos_json(
        "resultados/tempos_grandes.json"
    )
    gerar_boxplot(
        tempos_seq_grd,
        tempos_par_grd,
        "Boxplot - Listas Grandes",
        "boxplot_grandes.png",
    )
