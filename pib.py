import pandas as pd
import plotly.express as px


url = "http://www.ipea.gov.br/cartadeconjuntura/wp-content/uploads/2023/12/231212_atividade_economica.xlsx"

# Carrega o arquivo Excel do URL diretamente para um DataFrame do Pandas
df = pd.read_excel(url,sheet_name='Tab 12')
# Selecione o subconjunto desejado
df = df.loc[6:104]

df = df[[df.columns[1], df.columns[10]]]
# Agora você pode usar o DataFrame df normalmente
df = df.fillna('-')
# Obtém o nome original da coluna pelo índice
indice_da_coluna = 1
indice_da_coluna2 = 0
nome_original = df.columns[indice_da_coluna]
nome_original2 = df.columns[indice_da_coluna2]
# Renomeia a coluna pelo índice
novo_nome = 'PIB a preços de mercado'
df = df.rename(columns={nome_original: novo_nome})
df = df.rename(columns={nome_original2: 'Periodo'})
df = df[df['PIB a preços de mercado'] != '-']
df['crescimento'] = df['PIB a preços de mercado'].pct_change() * 100
# Obtenha os 24 últimos valores
df = df.tail(18)
df['crescimento'] = df['crescimento'].round(2)
# Cria um gráfico de linha interativo
fig = px.bar(df, x='Periodo', y='crescimento', text='crescimento')
fig.update_yaxes(title_text=None)
# Ajusta a margem para alinhar à direita
fig.update_layout(margin=dict(l=0, r=0, b=0, t=5))

# Salva o gráfico em um arquivo HTML
fig.write_html('pib.html')
