import pandas as pd

# Caminho do arquivo original
caminho_arquivo = "dados.csv"

# Ler o arquivo CSV, tratando espaços extras
df = pd.read_csv(caminho_arquivo, sep=";", encoding="utf-8", skip_blank_lines=True)

# Remover espaços dos nomes das colunas
df.columns = df.columns.str.strip()

# Remover espaços extras dentro da coluna "Tipo" para evitar problemas
df["Tipo"] = df["Tipo"].str.strip()

# Filtrar apenas as linhas onde "Tipo" seja "Consumo"
df_filtrado = df[df["Tipo"] == "Consumo"]

# Caminho do arquivo filtrado
caminho_saida = "dados_filtrados.csv"

# Salvar o CSV filtrado
df_filtrado.to_csv(caminho_saida, index=False, sep=";", encoding="utf-8")

print(f"✅ Arquivo filtrado salvo em: {caminho_saida}")

