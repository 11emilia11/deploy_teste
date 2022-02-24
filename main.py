import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px


def line_plot():
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                    size='petal_length', hover_data=['petal_width'])
    st.plotly_chart(fig)

def gauge_plot():

    fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = 450,
    title = {'text': "Speed"},
    domain = {'x': [0, 1], 'y': [0, 1]}
    ))

    st.plotly_chart(fig)
    

def area_plot(continent):
    df = px.data.gapminder()
    df = df[df['continent'] == continent]
    fig = px.area(df, x="year", y="pop", color="continent",
            line_group="country")
    st.plotly_chart(fig)


def bar_plot(country):
    
    data_canada = px.data.gapminder()
    fig = px.bar(data_canada[data_canada['country'] == country], x='year', y='pop')
    st.plotly_chart(fig)


def filter_country():
    global country
    data_canada = px.data.gapminder()
    countries = list(data_canada['country'].unique())

    country = st.selectbox('', countries,index=0, key = 18)
    
    return country


def filter_continent():
    global continent
    data_canada = px.data.gapminder()
    continents = list(data_canada['continent'].unique())

    continent = st.selectbox('', continents,index=0, key = 18)
    
    return continent

def page1():
    line_plot()

    gauge_plot()

def page2():
    country = filter_country()

    bar_plot(country)

def page3():

    continent = filter_continent()

    area_plot(continent)


def select_page():
    page = st.selectbox('Página', ['Página 1', 'Página 2', 'Página 3'], index=0)
    if page == 'Página 1':
        page1()
    
    elif page == 'Página 2':
        page2()
    
    elif page == 'Página 3':
        page3()



def main():

    select_page()



main()

