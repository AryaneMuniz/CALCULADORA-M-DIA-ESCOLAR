import streamlit as st
import pandas as pd

# Criação de uma variável para armazenar os dados no estado da sessão
if "dados" not in st.session_state:
    st.session_state["dados"] = []

# Título do app
st.title("Calculadora de Média Escolar")

# Inputs para nome e notas
nome = st.text_input("Nome do aluno")
nota1 = st.number_input("Nota 1", min_value=0.0, max_value=10.0, step=0.1)
nota2 = st.number_input("Nota 2", min_value=0.0, max_value=10.0, step=0.1)
nota3 = st.number_input("Nota 3", min_value=0.0, max_value=10.0, step=0.1)

# Botão para calcular a média
if st.button("Calcular"):
    media = (nota1 + nota2 + nota3) / 3
    situacao = "Aprovado(a)" if media >= 7 else "Reprovado(a)"
    
    # Exibe a média e situação do aluno
    st.success(f"Média do aluno {nome}: {media:.2f} - {situacao}")
    
    # Adiciona os dados no histórico
    st.session_state["dados"].append({
        "Nome": nome,
        "Nota 1": nota1,
        "Nota 2": nota2,
        "Nota 3": nota3,
        "Média": round(media, 2),
        "Situação": situacao
    })

# Verificando se há dados no histórico
if st.session_state["dados"]:
    df = pd.DataFrame(st.session_state["dados"])
    st.write("Histórico de alunos:")

    # Exibe a tabela com os dados
    st.dataframe(df)

    # Opção de excluir linha do histórico
    excluir_nome = st.selectbox("Selecione um aluno para excluir:", df["Nome"].tolist(), key="excluir_nome")
    if st.button("Excluir aluno"):
        # Remove a linha correspondente ao aluno selecionado
        st.session_state["dados"] = [dado for dado in st.session_state["dados"] if dado["Nome"] != excluir_nome]
        st.success(f"Aluno {excluir_nome} excluído com sucesso!")

    # Botão para baixar o histórico como CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Baixar como CSV", csv, "notas_alunos.csv", "text/csv")


