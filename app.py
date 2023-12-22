import pandas as pd
import requests
import plotly.express as px

url = 'https://servicodados.ibge.gov.br/api/v3/agregados/' \
      '7060/periodos/-24/' \
       'variaveis/2265?localidades=N1[all]'
# Faz a requisição GET
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida (código de status 200)
if response.status_code == 200:
  # Converte os dados JSON da resposta em um objeto Python
    dados_json = response.json()

    # Extrai a coluna "serie" dos dados JSON
    series_data = [item['resultados'][0]['series'][0]['serie'] for item in dados_json]

    dados_convertidos = []

    for periodo, taxa in series_data[0].items():
        dados_convertidos.append({'periodo': periodo, 'taxa': taxa})

    df = pd.DataFrame(dados_convertidos)

    # Converte a coluna 'taxa' para o tipo numérico
    df['taxa'] = pd.to_numeric(df['taxa'])

    # Cria um gráfico de linha interativo
    fig = px.line(df, x='periodo', y='taxa', title='Variação Índice IPCA:',markers=True, text='taxa')

    # Define o valor mínimo do eixo y como 0
    fig.update_yaxes(range=[0, df['taxa'].max() + 1])

    # Adiciona rótulos aos pontos e alinha acima dos marcadores
    fig.update_traces(textposition='top center')

    # Salva o gráfico em um arquivo HTML
    fig.write_html('grafico.html')


else:
    # Se a requisição falhou, imprime o código de status
    print("Falha na requisição. Código de status:", response.status_code)


