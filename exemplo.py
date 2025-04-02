import pandas as pd

# Leitura do arquivo com os dados
df = pd.read_csv("arquivo.txt", delimiter=";", encoding="utf-8")  # Muda o delimitador se necessário
print(df.head())  # Mostra as primeiras linhas

# Filtragem de Dados
idade_ana = df.loc[df["Nome"] == "Ana", "Idade"].values[0]
print(idade_ana)  # Saída: 30

# Criar um outro arquivo e armazenar os dados filtrados do arquivo para o outro
'''
# Suponha que já temos um DataFrame carregado
df = pd.read_csv("dados.txt", delimiter=";", encoding="utf-8")

# Filtrar os dados desejados (exemplo: apenas da Ana)
df_filtrado = df[df["Nome"] == "Ana"]

# Salvar em um novo arquivo CSV
df_filtrado.to_csv("dados_filtrados.csv", index=False, sep=";", encoding="utf-8")

print("Arquivo 'dados_filtrados.csv' criado com sucesso!")'''