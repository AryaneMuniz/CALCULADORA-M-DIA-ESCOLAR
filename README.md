Calculadora de Média Escolar
Este projeto é uma calculadora de médias escolares simples criada com Streamlit e Pandas. A aplicação permite que professores calculem rapidamente a média de notas dos alunos e verifiquem se eles foram aprovados ou reprovados com base em uma média mínima.

Além disso, o app oferece uma tabela para visualizar o histórico de alunos e a opção de exportar os resultados para um arquivo CSV.

Funcionalidades
Entrada de notas: O professor pode inserir o nome do aluno e as três notas.

Cálculo de média: O app calcula a média das três notas inseridas.

Situação do aluno: O sistema classifica o aluno como aprovado ou reprovado com base na média.

Histórico de alunos: Todos os alunos calculados são registrados e exibidos em uma tabela.

Download dos dados: O histórico de notas pode ser exportado para um arquivo CSV.

Tecnologias Utilizadas
Streamlit: Framework para criar aplicações web interativas e de fácil uso.

Pandas: Biblioteca para manipulação e análise de dados, usada para gerar a tabela de histórico de alunos.

Instalação e Execução
Passo 1: Clonar o repositório
Primeiro, clone este repositório para sua máquina local:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/projeto-calculadora-media-escolar.git
Passo 2: Instalar as dependências
Dentro da pasta do projeto, crie um ambiente virtual e instale as dependências necessárias:

Criar um ambiente virtual (opcional, mas recomendado):

bash
Copiar
Editar
python -m venv venv
Ativar o ambiente virtual:

No Windows:

bash
Copiar
Editar
venv\Scripts\activate

No macOS/Linux:

bash
Copiar
Editar
source venv/bin/activate
Instalar as dependências do projeto:

bash
Copiar
Editar
pip install -r requirements.txt
Passo 3: Rodar o app
Execute o aplicativo Streamlit com o comando:

bash
Copiar
Editar
streamlit run app.py
Isso abrirá o app no seu navegador.

Como Usar
Ao abrir o aplicativo, você verá campos para inserir o nome do aluno e suas três notas.

Clique no botão "Calcular" para ver a média do aluno e sua situação (aprovado ou reprovado).

O histórico de alunos será exibido na tabela abaixo.

Você pode baixar os dados em formato CSV clicando no botão "Baixar como CSV".

Exemplo de Uso
Entrada de Notas
Nome do aluno: João

Nota 1: 8.5

Nota 2: 7.2

Nota 3: 6.9

Resultado:
Média: 7.53

Situação: Aprovado
