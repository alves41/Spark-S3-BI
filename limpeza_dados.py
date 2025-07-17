import pandas as pd
import csv

# Configurações iniciais
input_file = "relatorio.csv"  # Substitua pelo seu arquivo de entrada
output_file = "limpeza_dados.csv"  # Arquivo de saída limpo
delimiter = ";"  # Delimitador usado no CSV (ajuste conforme necessário)

# --- Passo 1: Ler o arquivo CSV ---
try:
    df = pd.read_csv(
        input_file,
        delimiter=delimiter,
        encoding="utf-8",
        on_bad_lines="skip",  # Pular linhas malformadas
        dtype=str,  # Tratar todos os dados como string inicialmente
    )
except UnicodeDecodeError:
    # Tentar latin-1 se UTF-8 falhar
    df = pd.read_csv(input_file, delimiter=delimiter, encoding="latin-1", dtype=str)

# --- Passo 2: Remover linhas incompletas (com valores nulos) ---
# Remove linhas onde TODAS as colunas são nulas
df.dropna(how="all", inplace=True)

# --- Passo 3: Remover a última linha se estiver truncada ---
# Verifica se a última linha tem valores nulos em colunas críticas
if df.iloc[-1].isnull().any():
    df = df.iloc[:-1]  # Remove a última linha

# --- Passo 4: Padronizar strings e remover espaços extras ---
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# --- Passo 5: Salvar o arquivo limpo (UTF-8, delimitador consistente) ---
df.to_csv(
    output_file,
    sep=delimiter,
    index=False,  # Não salvar o índice
    encoding="utf-8",
    quoting=csv.QUOTE_ALL,  # Aspas em todos os campos para segurança
)

print(f"Arquivo limpo salvo como {output_file}!")