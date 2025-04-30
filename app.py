import streamlit as st
import pandas as pd

# Inicializa o histórico de alunos
if "dados" not in st.session_state:
    st.session_state["dados"] = []

st.title("Calculadora de Média Escolar")

# Entradas do formulário
nome = st.text_input("Nome do aluno")
serie = st.selectbox("Série do aluno", ["1º ano", "2º ano", "3º ano", "4º ano", "5º ano", 
                                        "6º ano", "7º ano", "8º ano", "9º ano", 
                                        "1º ano EM", "2º ano EM", "3º ano EM"])
nota1 = st.number_input("Nota 1", min_value=0.0, max_value=10.0, step=0.1)
nota2 = st.number_input("Nota 2", min_value=0.0, max_value=10.0, step=0.1)
nota3 = st.number_input("Nota 3", min_value=0.0, max_value=10.0, step=0.1)

# Botão para calcular
if st.button("Calcular"):
    media = (nota1 + nota2 + nota3) / 3
    situacao = "Aprovado(a)" if media >= 7 else "Reprovado(a)"
    
    st.success(f"Média do aluno {nome} ({serie}): {media:.2f} - {situacao}")
    
    # Adiciona os dados no histórico
    st.session_state["dados"].append({
        "Nome": nome,
        "Série": serie,
        "Nota 1": nota1,
        "Nota 2": nota2,
        "Nota 3": nota3,
        "Média": round(media, 2),
        "Situação": situacao
    })

# Exibe o histórico, se houver dados
if st.session_state["dados"]:
    df = pd.DataFrame(st.session_state["dados"])
    st.write("Histórico de alunos:")
    st.dataframe(df)

    # Seleção para excluir aluno
    excluir_nome = st.selectbox("Selecione um aluno para excluir:", df["Nome"].tolist(), key="excluir_nome")
    if st.button("Excluir aluno"):
        st.session_state["dados"] = [dado for dado in st.session_state["dados"] if dado["Nome"] != excluir_nome]
        st.success(f"Aluno {excluir_nome} excluído com sucesso!")

    # Botão para download do CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Baixar como CSV", csv, "notas_alunos.csv", "text/csv")


