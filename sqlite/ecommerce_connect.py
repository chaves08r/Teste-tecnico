import sqlite3
import csv
import argparse
import os

parser = argparse.ArgumentParser(description='Importar um arquivo CSV para uma tabela SQLite.')
parser.add_argument('csv', help='Caminho do arquivo CSV')
parser.add_argument('tabela', help='Nome da tabela no banco SQLite')
parser.add_argument('--db', default='ecommerce.db', help='Nome do arquivo de banco de dados SQLite (padrão: ecommerce.db)')

args = parser.parse_args()

# banco de dados
csv_arquivo = args.csv
db_arquivo = args.db
tabela = args.tabela

def inferir_tipo(valor):
    try:
        int(valor)
        return 'INTEGER'
    except ValueError:
        try:
            float(valor)
            return 'REAL'
        except ValueError:
            return 'TEXT'
        
with open(csv_arquivo, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    headers = next(reader)
    first_row = next(reader)
    tipos = [inferir_tipo(valor) for valor in first_row]

print(tipos)
# Criacao de tabela dinamicamente
colunas_def = ', '.join(f'"{nome}" {tipo}' for nome, tipo in zip(headers, tipos))

print(colunas_def)

# conectando o banco e criaando a tabela
conn = sqlite3.connect(db_arquivo)
cursor = conn.cursor()

cursor.execute(f'DROP TABLE IF EXISTS {tabela}') 
cursor.execute(f'CREATE TABLE {tabela} ({colunas_def})')

# Inserindo os dados
with open(csv_arquivo, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    colunas = ', '.join(f'"{col}"' for col in reader.fieldnames)
    placeholders = ', '.join('?' for _ in reader.fieldnames)

    for row in reader:
        valores = [row[col] for col in reader.fieldnames]
        cursor.execute(f'INSERT INTO {tabela} ({colunas}) VALUES ({placeholders})', valores)

# Salvar e fechar
conn.commit()
conn.close()

print(f"CSV importado com sucesso para a tabela '{tabela}' no banco '{db_arquivo}'.")