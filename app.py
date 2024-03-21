import pandas as pd
import matplotlib.pyplot as plt

# ANÁLISE EXPLORATÓRI DE DADOS DE SAÚDE

df = pd.read_csv('insurance.csv')

## GRÁFICO DE FUMANTES
smoke_counts = df['smoker'].value_counts()
colors=['steelblue', 'lightcoral']

fig, ax = plt.subplots(figsize=(8, 6))

ax.bar(

        smoke_counts.index # valor do eixo x
    ,   smoke_counts.values # valor do eixo y
    ,   color = colors
)

ax.set_xlabel('Smoker', fontsize=8)
ax.set_ylabel('Count', fontsize=8)

ax.set_title('Distribuição de Fumantes', fontsize=14)

# removendo contorno de gráfico
# plt.gca().spines['top'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()


fig, ax = plt.subplots(figsize=(8,6))

ax.scatter(df['age'], df['charges'], c="red")

ax.set_title('Gráfico de Dispersão: Idade vs Cobrança', fontsize=16)
ax.set_xlabel("Idade", fontsize=12)
ax.set_ylabel('Cobranças', fontsize=12)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()



fig, axes = plt.subplots(
    1, #linhas
    2, # colunas
    figsize=(12,6)
)

axes[0].scatter(df['bmi'], df['charges'], c="red")
axes[0].set_xlabel('BMI')
axes[0].set_ylabel('Charges')
axes[0].set_title("Charges vs BMI")

axes[1].scatter(df['age'], df['charges'], c="blue")
axes[1].set_xlabel('Age')
axes[1].set_ylabel('Charges')
axes[1].set_title("Charges vs Age")


mean_charges_sex = df.groupby('sex')['charges'].mean()
mean_charges_region = df.groupby('region')['charges'].mean()
mean_charges_children = df.groupby('children')['charges'].mean()
mean_charges_smoker = df.groupby('smoker')['charges'].mean()

colors = ['#2b8cbe', '#fe9929', '#31a354', '#a1d99b']

fig, axes = plt.subplots(2, 2, figsize=(12,8))

mean_charges_sex.plot(kind='bar', ax=axes[0, 0], color=colors)
axes[0, 0].set_xlabel('Sexo')
axes[0, 0].set_ylabel('Cobrança Média')
axes[0, 0].set_title('Cobrança Média por Sexo')
axes[0, 0].spines['top'].set_visible(False)
axes[0, 0].spines['right'].set_visible(False)

mean_charges_region.plot(kind='bar', ax=axes[0, 1], color=colors)
axes[0, 1].set_xlabel('Region')
axes[0, 1].set_ylabel('Cobrança Média')
axes[0, 1].set_title('Cobrança Média por Região')
axes[0, 1].spines['top'].set_visible(False)
axes[0, 1].spines['right'].set_visible(False)



mean_charges_children.plot(kind='bar', ax=axes[1, 0], color=colors)
axes[1, 0].set_xlabel('Número de Filhos')
axes[1, 0].set_ylabel('Cobrança Média')
axes[1, 0].set_title('Cobrança Média por Número de Filhos')
axes[1, 0].spines['top'].set_visible(False)
axes[1, 0].spines['right'].set_visible(False)


mean_charges_smoker.plot(kind='bar', ax=axes[1, 1], color=colors)
axes[1, 1].set_xlabel('Somker')
axes[1, 1].set_ylabel('Cobrança Média')
axes[1, 1].set_title('Cobrança Média por Somker')
axes[1, 1].spines['top'].set_visible(False)
axes[1, 1].spines['right'].set_visible(False)

plt.tight_layout()


plt.show()




plt.text(
    5, 2, "Texto de Exemplo", size=16
)

plt.xlim(0,7)
plt.ylim(0,4)

plt.show()


region_types = df['region'].value_counts()
region_names = ['southwest', 'souteast', 'northwest', 'northeast']
colors = ['steelblue', 'lightcoral', 'mediumseagreen', 'orange']

fig, ax = plt.subplots(figsize=(8,6))

ax.bar(
    region_names, 
    region_types.values,
    color=colors)

ax.set_title('Região', fontsize=16)
ax.set_xlabel("Contagem", fontsize=12)
ax.set_ylabel('Contagem de Regiões', fontsize=12)

for i,v in enumerate(region_types.values):
    # usamos a coordenada (Ii,Vi) para posicionar o valor da contagem no eixo X e com a altura eixo Y
    ax.text(i, v, str(v), ha='center', va='bottom')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
#ax.set_yticklabels([])
ax.set_yticks([])

plt.show()



mean_sex_charges = df.groupby('sex')['charges'].mean()
colors = ['steelblue', 'lightcoral']

_ = fig, ax = plt.subplots(figsize  = (8,6))

_ = ax.bar(
    mean_sex_charges.index,
    mean_sex_charges.values,
    color = colors
)

_ = ax.set_xlabel('sex')
_ = ax.set_ylabel('Charges')
_ = ax.set_title("Média de cobrança por Sexo")

_ = ax.spines['top'].set_visible(False)
_ = ax.spines['right'].set_visible(False)
_ = ax.spines['left'].set_visible(False)
#_ = ax.set_yticklabels([])
_ = ax.set_yticks([])

# Adicionar manualmente os textos nos rótulos
_ = ax.text(  0
        , mean_sex_charges.values[0]
        , f'{mean_sex_charges.values[0]:.2f}'
        , ha='center'
        , va='bottom'
        , fontsize = 12)

_ = ax.text(  1
        , mean_sex_charges.values[1]
        , f'{mean_sex_charges.values[1]:.2f}'
        , ha='center'
        , va='bottom'
        , fontsize = 12)

# diferença salarial entre homens e mulheres
_ = ax.set_xlim(-0.5, 1.5)
_ = ax.set_ylim(0, 17000)

## diferença percentual entre os dois eixos
diff_salarial = (mean_sex_charges['male'] - mean_sex_charges['female']) / mean_sex_charges['female'] * 100

### plotando a diferença salarial

_ = ax.text(
        1.58,
        mean_sex_charges[1] + 1500,
        f'Diferença Salarial de: {diff_salarial:.2f}%!',
        bbox={'facecolor': 'lightsteelblue',
          'alpha': 1,
          'pad': 0.7,
          'edgecolor':'none',
          'boxstyle':'round'},
        color='black',
        fontsize=11
)

_ = plt.show()