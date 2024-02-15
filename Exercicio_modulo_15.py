import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def main():
    st.title("Exercício Módulo 15")

    # Introdução
    st.header("Introdução")
    st.write("Este é um exercício que reproduzirá 23 códigos da documentação do Streamlit.")

    # Exemplo 1: Hello World
    st.header("Exemplo 1: Hello World")
    st.write("Este é um exemplo simples de uma aplicação Streamlit que exibe 'Hello, World!'")
    code_hello_world = """
    import streamlit as st
    st.write('Hello, World!')
    """
    st.code(code_hello_world, language="python")

 