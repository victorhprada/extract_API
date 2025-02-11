import streamlit as st
import pandas as pd
import psycopg2
import time
import os
from datetime import datetime
from dotenv import load_dotenv

# 1) Título principal
st.title('Dashboard de Dados do Bitcoin')

# 2) Seção de carregamento de dados
st.header('Contexto de Data Engineering')

# 3) Texto simples
st.write("""
         Este é um dashboard simula alguns elementos que você usaria em um projeto de Data Engineering:
         - Coleta/Extração de dados
         - Transformação de dados
         - Visualização de dados
         - Publicação de dados
         - Monitoramento de dados
         """)

# 4) Texto em formato de markdown
st.markdown("""
            ## Tópicos abordados:
            - **Criação de widgets** para coleta de parâmetros
            - **Exibição de DataFrames** (parte de "Transform")
            - **Gráficos** para monitorar performance e throughput
            - **Métricas** representando KPIs de pipeline ETL
            """)

st.header('2. Parâmetros para pipelines')

# 5) Parâmetro textual
nome_pipeline = st.text_input('Nome da pipeline de dados', value='pipeline_bitcoin')

# 6) Parâmetro numérico
batch_size = st.number_input('Batch size (linha por ingestão)', min_value=100, max_value=100000, value=10000, step=100)

# 7) Seletor contínuo
latencia_max = st.slider('Latência máxima Aceitável (segundos)', min_value=1, max_value=30, value=5)

# 8) Escolha de um pipeline
tipo_pipeline = st.selectbox('Tipo de pipeline:', ['Batch', 'Streaming', 'Lambda', 'Kappa'])

# 9) Escolha múltipla de camadas de processamento
camadas_processamento = st.multiselect("Quais camadas envolvidas no pipeline?",
    ["Raw", "Staging", "Trusted", "Analytics", "Sandbox", "Dimensão", "Fato"],
    default=["Raw", "Staging"]
)

# 10) Check para simular ativação de logs
ativar_logs = st.checkbox('Ativar logs de execução')

st.header('3. Exibição de dados (Transform)')

# 11) Criar um dataset ficticio sobre 'execuções' de pipelines
dados_execusoes = {
    "data_execucao": pd.date_range(end=datetime.now(), periods=5, freq="H"),
    "status": ["Sucesso", "Sucesso", "Falha", "Sucesso", "Sucesso"],
    "linhas_processadas": [1000, 1200, 900, 1500, 1300],
    "tempo_execucao_seg": [4.2, 5.1, 7.8, 3.9, 4.5]
}
df_execucoes = pd.DataFrame(dados_execusoes)

# 12) Tabela interativa
st.subheader('Execuções recentes de pipelines')
st.dataframe(df_execucoes)

# 13) Tabela estática
st.subheader('Tabela estática - ultimas execuções')
st.table(df_execucoes)

# 14) Gráfico de barras
st.subheader('Indicadores de desempenho (KPI)')
col1, col2, col3 = st.columns(3)
col1.metric('Total de linhas processadas', df_execucoes['linhas_processadas'].sum())
col2.metric('Execuções com sucesso', str(df_execucoes['status'].value_counts()['Sucesso']), 0)
col3.metric('Execuções com falha', str(df_execucoes['status'].value_counts()['Falha']), 0)

st.header('4. Visualização de dados (Analytics)')

# 15) Gráfico de linha com métricas
st.subheader('Linhas processadas por execução (line chart)')
df_execucoes_ordenado = df_execucoes.sort_values(by='data_execucao')
st.line_chart(df_execucoes_ordenado, x='data_execucao', y='linhas_processadas')

# 16) Gráfico de barras com métricas
st.subheader('Execuções por status (bar chart)')
st.bar_chart(df_execucoes_ordenado, x='data_execucao', y='linhas_processadas', color='status')

st.header('5. Outros recursos úteis')

# 17) Seletor de data
data_planejada = st.date_input('Data planejada para execução', value=datetime.now())

# 18) Barra de progresso
st.write('Carregando dados de log...')
progress_bar = st.progress(0)

for i in range(101):
    time.sleep(0.1)
    progress_bar.progress(i)

# 19) Mensagens de sucesso/erro
if ativar_logs:
    st.success('Logs ativados com sucesso!')
else:
    st.warning('Logs desativados com sucesso!')

# 20) Botão para simular disparo de pipeline
if st.button('Disparar pipeline'):
    st.info(f'Pipeline {nome_pipeline} disparada em modo {tipo_pipeline}')
    st.write(f'Batch size configurado para {batch_size} linhas. Latência máxima aceitável de {latencia_max} segundos.')
    st.write(f'Camadas selecionadas: {', '.join(camadas_processamento)}')

st.markdown("___")
st.caption("Quick Starter de Streamlit aplicado à Engenharia de Dados. © 2025")





