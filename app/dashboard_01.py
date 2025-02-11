import streamlit as st
import pandas as pd
import psycopg2
import time
import os
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine


# Carregar variáveis de ambiente
load_dotenv()

# Lê as credenciais do banco de dados do arquivo .env
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')

def write_postgres_data():
    "Lê os dados do banco PostgreSQL e retorna um DataFrame"

    try:
        # Criar string de conexão SQLAlchemy
        DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
        engine = create_engine(DATABASE_URL)
        
        query = "SELECT * FROM bitcoin ORDER BY timestamp DESC"
        df = pd.read_sql_query(query, engine)
        return df
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return pd.DataFrame()
    
def main():
    st.set_page_config(
        page_title="Bitcoin Dashboard",
        page_icon=":chart_with_upwards_trend:",
        layout="wide"
    )
    st.title("Bitcoin Dashboard")
    st.write("Este dashboard exibe os dados do preço do Bitcoin coletados periodicamente em um banco PostgreSQL.")
    
    df = write_postgres_data()
    
    if not df.empty:
        st.subheader("Dados recentes do Bitcoin")
        st.dataframe(df)
        
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values(by='timestamp')
        
        st.subheader("Preço do Bitcoin ao longo do tempo")
        st.line_chart(df, x='timestamp', y='valor', use_container_width=True)

        st.subheader("Estatísticas gerais")
        col1, col2, col3 = st.columns(3)
        col1.metric("Preço Atual", f"${df['valor'].iloc[-1]:,.2f}")
        col2.metric("Preço Máximo", f"${df['valor'].max():,.2f}")
        col3.metric("Preço Mínimo", f"${df['valor'].min():,.2f}")
    else:
        st.warning("Nenhum dado encontrado no banco de dados PostgreSQL.")

if __name__ == "__main__":
    main()

        
    


