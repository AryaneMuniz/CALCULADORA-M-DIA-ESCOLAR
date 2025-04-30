import streamlit as st
import pandas as pd

# Inicializa o histórico
if "dados" not in st.session_state:
    st.session_state["dados"] = []

st.title("Calculadora de Média Escolar")

# Formulário de entrada
nome = st.text_input("Nome do aluno")
serie = st.selectbox("Série do aluno", ["1º ano", "2º ano", "3º ano", "4º ano", "5º ano", 
                                        "6º ano", "7º ano", "8º ano", "9º ano", 
                                        "1º ano EM", "2º ano EM", "3º ano EM"])
avaliacao1 = st.number_input("Primeira Avaliação", min_value=0.0, max_value=10.0, step=0.1, format="%.1f")
avaliacao2 = st.number_input("Segunda Avaliação", min_value=0.0, max_value=10.0, step=0.1, format="%.1f")
avaliacao3 = st.number_input("Terceira Avaliação", min_value=0.0, max_value=10.0, step=0.1, format="%.1f")
avaliacao4 = st.number_input("Quarta Avaliação", min_value=0.0, max_value=10.0, step=0.1, format="%.1f")

# Botão para calcular a média
if st.button("Calcular"):
    notas = [avaliacao1, avaliacao2, avaliacao3, avaliacao4]
    notas_preenchidas = [nota for nota in notas if nota > 0.0]

    if notas_preenchidas:
        media = sum(notas_preenchidas) / len(notas_preenchidas)
        situacao = "Aprovado(a)" if media >= 7 else "Reprovado(a)"

        st.success(f"Média do aluno {nome} ({serie}): {media:.2f} - {situacao}")

        st.session_state["dados"].append({
            "Nome": nome,
            "Série": serie,
            "Primeira Avaliação": avaliacao1,
            "Segunda Avaliação": avaliacao2,
            "Terceira Avaliação": avaliacao3,
            "Quarta Avaliação": avaliacao4,
            "Média": round(media, 2),
            "Situação": situacao
        })
    else:
        st.warning("Por favor, preencha ao menos uma das avaliações para calcular a média.")

# Exibição do histórico
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



