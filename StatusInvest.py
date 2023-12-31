import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import requests
import plotly.express as px
import plotly.graph_objects as go
import matplotlib
matplotlib.rcParams['figure.figsize'] = (16,8)

def consulta_bc(codigo_bcb):
  url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json'.format(codigo_bcb)
  #df = pd.read_json(url)
  response = requests.get(url)
  dados_json = response.json()

  df = pd.DataFrame(dados_json)
  df['data'] = pd.to_datetime(df['data'], dayfirst=True)
  df.set_index('data', inplace=True)
  df = df.reset_index()
  return df

selic_meta = consulta_bc(432)
selic_meta['termina_com_01'] = selic_meta['data'].dt.strftime('%d').eq('01').astype(bool)
selic_meta = selic_meta[selic_meta['termina_com_01']==True]
# Obtenha os 24 últimos valores
selic_meta = selic_meta.tail(30)
selic_meta['data'] = selic_meta['data'].dt.strftime('%Y%m')
# Converte a coluna 'taxa' para o tipo numérico
selic_meta['valor'] = pd.to_numeric(selic_meta['valor'])

# Cria um gráfico de linha interativo
fig = px.line(selic_meta, x='data', y='valor', markers=True, text='valor')
# Define o valor mínimo do eixo y como 0
fig.update_yaxes(range=[0, selic_meta['valor'].max() + 1])

# Adiciona rótulos aos pontos e alinha acima dos marcadores
fig.update_traces(textposition='top left',stackgroup='v')


# Salva o gráfico em um arquivo HTML
fig.write_html('grafico2.html')
