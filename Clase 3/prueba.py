import pandas as pd
import plotly.express as px
data = pd.read_excel('RecursoDatos.xlsx')
banco_popular = data[data['BANCO'] == "BANCO POPULAR"]

## px."tipo Grafico "(data set, x='variable x', y='variable y')
fig = px.bar(banco_popular, x='fecha_reporte', y='CLIENTES')
fig.show()