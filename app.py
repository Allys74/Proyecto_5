# Importamos librerias
import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')       # Leemos los datos

# Primer Título
st.header('Visualizar los Datos')

# Inclusion de modelos
include_all = st.checkbox('Incluir modelos con menos de 1000 anuncios')

if include_all:     # muestra todos
    st.dataframe(car_data)
else:       # muestra los de más de mil ads
    groupby_model = car_data.groupby(
        'model')['model'].count()      # agrupo por modelo
    # enlisto los modelos
    thousand_ads = groupby_model[groupby_model > 1000].index
    # presento los modelos
    models = car_data[car_data['model'].isin(thousand_ads)].sort_values('model')
    st.write(models)

# Segundo Título
#st.header('Tipo de vehículo por modelo')

# Botón de crear Gráfico
show_button = st.button('Construir histograma')  # crear un botón

# Checkbox para el tipo de gráfico a mostrar
build_histogram = st.checkbox('Construir un Histograma')
build_scatter = st.checkbox('Construir un Diagrama de Disperción')

# elegir el tipo de gráfico
if build_histogram:     # crear un histograma
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")

if build_scatter:       # crear un diagrama de disperción
    st.write('Construir un diagrama de disperción para la columna odómetro')
    fig = px.scatter(car_data, x="odometer")

if show_button:         # al hacer clic en el botón
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

st.write('Esta aplicación está en construcción, todavía no es funcional')
