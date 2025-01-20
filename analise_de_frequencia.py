import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Carregar os dados da planilha
file_path = "C:\\Users\\Alecs\\Desktop\\Casos_Juridicos.xlsx"
df = pd.read_excel(file_path)

# Agrupar os dados para obter os resultados por tipo de tributo
tributos_resultados = df.groupby("Tipo de Tributo")["Sentença/Decisão/Acórdão"].value_counts().unstack(fill_value=0)

# Renomear as colunas para facilitar a leitura
tributos_resultados = tributos_resultados.rename(columns={
    "Procedente": "Vencidos",
    "Improcedente": "Negados",
    "Sem decisão": "Sem Resultado"
})

# Garantir que todas as categorias existam
for col in ["Vencidos", "Negados", "Sem Resultado"]:
    if col not in tributos_resultados.columns:
        tributos_resultados[col] = 0

# Dados para o gráfico
tributos = list(tributos_resultados.index)  # Tipos de tributo
casos = ["Vencidos", "Negados", "Sem Resultado"]
valores = [tributos_resultados[caso].values for caso in casos]

# Configuração da posição das barras
x = np.arange(len(tributos))  # A posição das barras
largura = 0.25  # Largura das barras

# Criando o gráfico
fig, ax = plt.subplots(figsize=(12, 6))

# Criando barras para cada categoria de caso
barras_vencidos = ax.bar(x - largura, valores[0], largura, label='Vencidos', color='green')
barras_negados = ax.bar(x, valores[1], largura, label='Negados', color='red')
barras_sem_resultado = ax.bar(x + largura, valores[2], largura, label='Sem Resultado', color='gray')

# Adicionando labels, título e customizando o gráfico
ax.set_xlabel('Tipos de Tributo', fontsize=14)
ax.set_ylabel('Quantidade de Processos', fontsize=14)
ax.set_title('Resultados dos Processos por Tipo de Tributo', fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(tributos, rotation=45)
ax.legend()

# Exibindo os valores acima das barras
def adicionar_labels(barras):
    for barra in barras:
        altura = barra.get_height()
        ax.annotate(f'{int(altura)}',
                    xy=(barra.get_x() + barra.get_width() / 2, altura),
                    xytext=(0, 3),  # Desloca a anotação para cima
                    textcoords="offset points",
                    ha='center', va='bottom')

# Adicionando as labels para as barras
adicionar_labels(barras_vencidos)
adicionar_labels(barras_negados)
adicionar_labels(barras_sem_resultado)

# Exibindo o gráfico
plt.tight_layout()
plt.show()
