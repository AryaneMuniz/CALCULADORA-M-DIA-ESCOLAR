import streamlit as st
import pandas as pd

if "dados" not in st.session_state:
    st.session_state["dados"] = []

st.title("Calculadora de Média Escolar")

nome = st.text_input("Nome do aluno")
nota1 = st.number_input("Nota 1", min_value=0.0, max_value=10.0, step=0.1)
nota2 = st.number_input("Nota 2", min_value=0.0, max_value=10.0, step=0.1)
nota3 = st.number_input("Nota 3", min_value=0.0, max_value=10.0, step=0.1)

if st.button("Calcular"):
    media = (nota1 + nota2 + nota3) / 3
    situacao = "Aprovado(a)" if media >= 7 else "Reprovado(a)"
    
    st.success(f"Média do aluno {nome}: {media:.2f} - {situacao}")
    
    st.session_state["dados"].append({
        "Nome": nome,
        "Nota 1": nota1,
        "Nota 2": nota2,
        "Nota 3": nota3,
        "Média": round(media, 2),
        "Situação": situacao
    })

if st.session_state["dados"]:
    df = pd.DataFrame(st.session_state["dados"])
    st.write("Histórico de alunos:")
    st.dataframe(df)

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Baixar como CSV", csv, "notas_alunos.csv", "text/csv")

