import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


gas_df = pd.read_csv('gasolina.csv')

with sns.axes_style('darkgrid'):
  fig, ax = plt.subplots(figsize=(16,5))
  graffic = sns.lineplot(data=gas_df, x='dia' , y='venda' , palette='pastel')
  graffic.set_title('Preço da Gasolina por dia', size=16, fontweight='bold')
  graffic.set(xlabel='dia', ylabel='venda (R$)')
  plt.savefig('gasolina.png')