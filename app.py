# Importamos librerias
import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')       # Leemos los datos

# Primer Título
st.header('Visualizar los Datos')

# Inclusion de modelos
include_all = st.checkbox('Incluir modelos con menos de 1000 anuncios')

if include_all:     # muestra la tabla normal
    st.dataframe(car_data)
else:       # muestra solo los de más de mil ads
    groupby_model = car_data.groupby(
        'model')['model'].count()      # agrupo por modelo
    thousand_ads = groupby_model[groupby_model > 1000].index
    # presento los modelos
    models = car_data[car_data['model'].isin(
        thousand_ads)].sort_values('model')
    st.write(models)
st.write('\nCreación de Gráficos para el conjunto de datos de anuncios de venta de coches')

# Checkbox para el tipo de gráfico a mostrar
build_scatter = st.checkbox('Construir un Diagrama de Disperción')
build_histogram = st.checkbox('Construir un Histograma')

# Botón de crear Gráfico
show_button = st.button('Construir histograma')  # crear un botón

if show_button:         # al hacer clic en el botón
    if build_histogram and build_scatter:
        st.write('Por favor, seleccione solo un tipo de gráfico a la vez')
    else:
        # el tipo de gráfico a escoger
        if build_histogram:     # crear un histograma
            build_scatter = False
            st.subheader('Histograma de Condición vs Año del Modelo')
            fig = px.histogram(car_data, x='model_year', color='condition')
            st.plotly_chart(fig, use_container_width=True)

        if build_scatter:       # crear un diagrama de disperción
            build_histogram = False
            st.subheader('Diagrama de Disperción para la columna odómetro')
            fig = px.scatter(car_data, x="odometer", y="price")
            st.plotly_chart(fig, use_container_width=True)

# Segundo Título
st.header('Tipo de vehículo por modelo')

# Separo las marcas
manufacturer = ['acura', 'bmw', 'buick', 'cadillac', 'chevrolet', 'chrysler',
                'dodge', 'ford', 'gmc', 'honda', 'hyundai', 'jeep', 'kia',
                'mercedes-benz benze', 'nissan', 'ram', 'subaru', 'toyota', 'volkswagen']
new_colum = []
for modelo in car_data['model']:       # clasifico los modelos
    for marca in manufacturer:
        if marca in modelo.lower():
            if marca == 'mercedes-benz benze':
                new_colum.append('mercedes-benz')
            else:
                new_colum.append(marca)

car_data['manufacturer'] = new_colum    # Creo nueva columna

# Creo el histograma
vehicle_types = px.histogram(car_data.sort_values(
    by='model', ascending=True), x='manufacturer', color='type')
# preseno el histograma
st.plotly_chart(vehicle_types, use_container_width=True)

# Tercer Título
st.header('Comparar Distribución de Precio entre Modelos')

# Creo los cuadros de opciones a seleccionar
option_1 = st.selectbox("Seleccione la primera marca", (manufacturer))
option_2 = st.selectbox("Seleccione la segunda marca", (manufacturer))

# luego condiciono la busqueda con las opciones
options = car_data[(car_data['manufacturer'] == option_1) |
                   (car_data['manufacturer'] == option_2)]
price_models = px.histogram(
    options, x='price', color='manufacturer')    # Creo el histograma

# condicionamos que no sean las dos opciones iguales
if option_1 == option_2:
    st.write('Para hacer la comparación, seleccione marcas diferentes')
else:
    # presento el histograma
    st.plotly_chart(price_models, use_container_width=True)
