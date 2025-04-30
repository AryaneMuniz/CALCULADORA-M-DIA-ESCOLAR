import streamlit as st
import pandas as pd

if "dados" not in st.session_state:
    st.session_state["dados"] = []

st.title("Calculadora de Média Escolar")

nome = st.text_input("Nome do aluno")
serie = st.selectbox("Série do aluno", ["1º ano", "2º ano", "3º ano", "4º ano", "5º ano", 
                                        "6º ano", "7º ano", "8º ano", "9º ano", 
                                        "1º ano EM", "2º ano EM", "3º ano EM"])

# Agora com text_input para diferenciar nota zero de "não preenchida"
avaliacoes = []
for i in range(1, 5):
    aval = st.text_input(f"{i}ª Avaliação")
    avaliacoes.append(aval)

if st.button("Calcular"):
    notas_formatadas = []
    notas_validas = []

    for aval in avaliacoes:
        try:
            nota = float(aval)
            if 0.0 <= nota <= 10.0:
                notas_formatadas.append(nota)
                notas_validas.append(nota)
            else:
                st.warning("As notas devem estar entre 0 e 10.")
                break
        except:
            notas_formatadas.append("Não Avaliado")

    if notas_validas:
        media = sum(notas_validas) / len(notas_validas)
        situacao = "Aprovado(a)" if media >= 7 else "Reprovado(a)"

        st.success(f"Média do aluno {nome} ({serie}): {media:.2f} - {situacao}")

        st.session_state["dados"].append({
            "Nome": nome,
            "Série": serie,
            "Primeira Avaliação": notas_formatadas[0],
            "Segunda Avaliação": notas_formatadas[1],
            "Terceira Avaliação": notas_formatadas[2],
            "Quarta Avaliação": notas_formatadas[3],
            "Média": round(media, 2),
            "Situação": situacao
        })
    else:
        st.warning("Preencha pelo menos uma nota válida para calcular a média.")

# Mostrar histórico e opção de exclusão
if st.session_state["dados"]:
    df = pd.DataFrame(st.session_state["dados"])
    st.write("Histórico de alunos:")
    st.dataframe(df)

    excluir_nome = st.selectbox("Selecione um aluno para excluir:", df["Nome"].tolist(), key="excluir_nome")
    if st.button("Excluir aluno"):
        st.session_state["dados"] = [dado for dado in st.session_state["dados"] if dado["Nome"] != excluir_nome]
        st.success(f"Aluno {excluir_nome} excluído com sucesso!")

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Baixar como CSV", csv, "notas_alunos.csv", "text/csv")



