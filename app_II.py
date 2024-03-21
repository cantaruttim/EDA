# bibliotecas para tratamento
import pandas as pd
import numpy as np

# bibliotecas para visualização
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# configuração para não mostrar warnings
import warnings
warnings.filterwarnings('ignore')

# estilo do gráfico
plt.style.use("ggplot")

# exibição máximo do dataframe
pd.set_option("display.max_rows", 50)

# exibir todas as colunas de um dataframe
pd.set_option("display.max_columns", None)


# importando os dados
df = pd.read_csv('data.csv')

print(f"O dataframe possui {df.shape[0]} linhas e {df.shape[1]} colunas")

df.info()


fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# primeiro boxplot: Rent
bp1 = axs[0].boxplot(df['rent'], patch_artist=True)
axs[0].set_title("Boxplot da variável rent")
# cor do boxplot 1
bp1['boxes'][0].set_facecolor('lightblue')

#legenda bp1
max_rent = np.max(df['rent'])
axs[0].annotate(f'Valor Máximo = {max_rent}',
                xy=(1, max_rent),
                xytext=(1.05, max_rent),
                bbox=dict(facecolor='lightblue', edgecolor='blue'),
                fontsize=5)

# primeiro boxplot: Rent
bp2 = axs[1].boxplot(df['total'], patch_artist=True)
axs[1].set_title("Boxplot da variável total")
# cor do boxplot 1
bp1['boxes'][0].set_facecolor('lightgreen')

#legenda bp1
max_rent = np.max(df['total'])
axs[1].annotate(f'Valor Máximo = {max_rent}',
                xy=(1, max_rent),
                xytext=(1.05, max_rent),
                bbox=dict(facecolor='lightblue', edgecolor='blue'),
                fontsize=5)

plt.show()



mediana_rent = df.rent.median()

mediana_rent_format = (
    "R$ {:,.2f}".format(mediana_rent)
    .replace(",", "v")
    .replace(".", ",")
    .replace("v", ".")
)

data = [go.Histogram(x=df.rent, 
                     nbinsx=50, 
                     marker=dict(color='blue'))]

line = [go.Scatter(x=[mediana_rent, mediana_rent], 
                   y=[0, 2200], 
                   mode='lines',
                   line=dict(color='orange', dash='dash'), 
                   showlegend=True,
                   name=f"Mediana = {mediana_rent_format}")]

fig = go.Figure(data=data+line)

fig.update_layout(title_text='Histograma do Aluguel', 
                  xaxis_title='Aluguel',
                  yaxis_title='Contagem',
                  autosize=False, 
                  width=900, 
                  height=500)

fig.update_yaxes(range=[0, 2200])

fig.show()


cores_do_tipo = {
    'Studio e kitnet': '#440154',
    'Apartamento': '#482878',
    'Casa em condomínio': '#26828e',
    'Casa': '#31688e'
}

fig = px.histogram(df, x='type')
fig.update_layout(title="Distribuição dos Tipos de Imóveis",
                  xaxis_title="Tipo do Imóvel",
                  yaxis_title="Contagem")

fig.show()