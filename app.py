import streamlit as st
import pandas as pd
import uuid

st.set_page_config(page_title="Calculadora de Média Escolar", layout="centered")

# Inicializa o estado da sessão
if "dados" not in st.session_state:
    st.session_state["dados"] = []

st.title("📚 Calculadora de Média Escolar")

# Layout com colunas para nome e série
col1, col2 = st.columns(2)
with col1:
    nome = st.text_input("Nome do aluno")
with col2:
    serie = st.selectbox(
        "Série do aluno", 
        ["1º ano", "2º ano", "3º ano", "4º ano", "5º ano", 
         "6º ano", "7º ano", "8º ano", "9º ano", 
         "1º ano EM", "2º ano EM", "3º ano EM"]
    )

st.markdown("### Notas das Avaliações")
avaliacoes = []
for i in range(1, 5):
    nota = st.number_input(f"{i}ª Avaliação", min_value=0.0, max_value=10.0, step=0.1, key=f"nota_{i}")
    avaliacoes.append(nota)

if st.button("📊 Calcular"):
    if not nome.strip():
        st.warning("Por favor, insira o nome do aluno.")
        st.stop()

    notas_validas = [nota for nota in avaliacoes if isinstance(nota, float)]
    
    if notas_validas:
        media = sum(notas_validas) / len(notas_validas)
        situacao = "Aprovado(a)" if media >= 7 else "Reprovado(a)"

        st.success(f"✅ Média do aluno **{nome}** ({serie}): **{media:.2f}** - **{situacao}**")

        st.session_state["dados"].append({
            "ID": str(uuid.uuid4()),
            "Nome": nome,
            "Série": serie,
            "Primeira Avaliação": avaliacoes[0],
            "Segunda Avaliação": avaliacoes[1],
            "Terceira Avaliação": avaliacoes[2],
            "Quarta Avaliação": avaliacoes[3],
            "Média": round(media, 2),
            "Situação": situacao
        })

        st.rerun()
    else:
        st.warning("Preencha pelo menos uma nota válida para calcular a média.")

# Exibir histórico com filtros e exclusão
if st.session_state["dados"]:
    st.markdown("---")
    st.subheader("📋 Histórico de Alunos")

    df = pd.DataFrame(st.session_state["dados"])

    filtro_nome = st.text_input("🔍 Buscar por nome")
    if filtro_nome:
        df = df[df["Nome"].str.contains(filtro_nome, case=False)]

    st.dataframe(df.drop(columns=["ID"]), use_container_width=True)

    if not df.empty:
        aluno_excluir = st.selectbox("Selecione um aluno para excluir:", 
                                     options=df["Nome"] + " - " + df["ID"].str[:8])
        if st.button("🗑️ Excluir aluno"):
            id_excluir = aluno_excluir.split(" - ")[-1]
            st.session_state["dados"] = [d for d in st.session_state["dados"] if not d["ID"].startswith(id_excluir)]
            st.success("Aluno excluído com sucesso!")
            st.experimental_rerun()

    # Botão para baixar CSV
   # Define a ordem das colunas manualmente
colunas_ordenadas = [
    "Nome", "Série", 
    "Primeira Avaliação", "Segunda Avaliação", 
    "Terceira Avaliação", "Quarta Avaliação", 
    "Média", "Situação"
]

df_formatado = df[colunas_ordenadas]

# Gera CSV limpo e formatado
csv = df_formatado.to_csv(index=False, sep=',', encoding='utf-8')

# Botão para download
st.download_button(
    label="⬇️ Baixar histórico como CSV",
    data=csv,
    file_name="notas_alunos.csv",
    mime="text/csv"
)
