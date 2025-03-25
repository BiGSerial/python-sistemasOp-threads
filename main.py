from app.benchmarks import executar_testes_em_pasta
from app.graficos import gerar_boxplot
from app.utils import salvar_tempos_json

if __name__ == "__main__":
    # === Listas pequenas ===
    tempos_seq_peq, tempos_par_peq, nomes_peq = executar_testes_em_pasta(
        "listas_pequenas"
    )

    gerar_boxplot(
        tempos_seq_peq,
        tempos_par_peq,
        "Boxplot - Listas Pequenas",
        "boxplot_pequenas.png",
        nomes_bases=nomes_peq,
    )

    salvar_tempos_json(tempos_seq_peq, tempos_par_peq, "tempos_pequenas.json")

    # === Listas grandes ===
    tempos_seq_grd, tempos_par_grd, nomes_grd = executar_testes_em_pasta(
        "listas_grandes"
    )

    gerar_boxplot(
        tempos_seq_grd,
        tempos_par_grd,
        "Boxplot - Listas Grandes",
        "boxplot_grandes.png",
        nomes_bases=nomes_grd,
    )

    salvar_tempos_json(tempos_seq_grd, tempos_par_grd, "tempos_grandes.json")
