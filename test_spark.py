# converte_csv.py

input_path = "relatorio.csv"
output_path = "csv_em_utf8.csv"

with open(input_path, "r", encoding="latin1") as origem:  # ou 'ISO-8859-1'
    conteudo = origem.read()

with open(output_path, "w", encoding="utf-8") as destino:
    destino.write(conteudo)

print("Arquivo convertido para UTF-8 com sucesso!")
