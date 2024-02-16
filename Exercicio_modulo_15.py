import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import base64
import matplotlib.pyplot as plt

def main():
    st.title("Exercício Módulo 15")

    # Introdução
    st.header("Introdução")
    st.write("Este é um exercício que reproduzirá 20 códigos da documentação do Streamlit.")

    # Exemplo 1: Hello World
    st.header("Exemplo 1: Hello World")
    st.write("Este é um exemplo simples de uma aplicação Streamlit que exibe 'Hello, World!'")
    st.code("import streamlit as st\n\nst.write('Hello, World!')", language="python")

    # Exemplo 2: Dataframes
    st.header("Exemplo 2: Dataframes")
    st.write("Este exemplo demonstra como exibir um dataframe no Streamlit.")
    df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    })
    st.write(df)

    # Exemplo 3: Gráfico de Linhas
    st.header("Exemplo 3: Gráfico de Linhas")
    st.write("Este exemplo mostra como criar e exibir um gráfico de linhas usando Altair.")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

    # Exemplo 4: Widgets Interativos
    st.header("Exemplo 4: Widgets Interativos")
    st.write("Este exemplo demonstra como adicionar widgets interativos.")
    x = st.slider('Selecione um valor')
    st.write(f'O valor selecionado é {x}.')

    # Exemplo 1: Texto e Markdown
    st.header("Exemplo 5: Texto e Markdown")
    st.write("Este exemplo demonstra como exibir texto e Markdown.")
    st.write("Aqui está um texto simples em Streamlit.")
    st.markdown("### Este é um título em Markdown")

    # Exemplo 6: Botões
    st.header("Exemplo 6: Botões")
    st.write("Este exemplo mostra como adicionar botões.")
    if st.button("Clique aqui"):
        st.write("Botão clicado!")

    # Exemplo 7: Seleção de Opções
    st.header("Exemplo 7: Seleção de Opções")
    st.write("Este exemplo demonstra como adicionar uma seleção de opções.")
    option = st.selectbox("Escolha uma opção", ["Opção 1", "Opção 2", "Opção 3"])
    st.write("Você selecionou:", option)

    # Exemplo 8: Entrada de Texto
    st.header("Exemplo 8: Entrada de Texto")
    st.write("Este exemplo mostra como adicionar uma caixa de entrada de texto.")
    text_input = st.text_input("Digite algo", "Digite aqui...")
    st.write("Você digitou:", text_input)

    # Exemplo 9: Multi-Seleção
    st.header("Exemplo 9: Multi-Seleção")
    st.write("Este exemplo demonstra como adicionar uma multi-seleção.")
    options = st.multiselect("Selecione várias opções", ["Opção 1", "Opção 2", "Opção 3"])
    st.write("Você selecionou:", options)

    # Exemplo 10: Gráfico de Barras
    st.header("Exemplo 10: Gráfico de Barras")
    st.write("Este exemplo mostra como criar e exibir um gráfico de barras.")
    data = pd.DataFrame(np.random.randint(0, 100, (10, 2)), columns=['A', 'B'])
    st.bar_chart(data)

    # Exemplo 11: Exibindo Arquivos PDF
    st.header("Exemplo 11: Exibindo Arquivos PDF")
    st.write("Este exemplo demonstra como exibir arquivos PDF.")
    pdf_file_path = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
    st.write(f"Visualize o PDF [aqui]({pdf_file_path}).")

    # Exemplo 12: Adicionando Títulos de Seção
    st.header("Exemplo 12: Adicionando Títulos de Seção")
    st.write("Este exemplo demonstra como adicionar títulos de seção.")
    with st.expander("Veja mais"):
        st.write("Conteúdo adicional aqui.")

    # Exemplo 13: Slider de Data
    st.header("Exemplo 13: Slider de Data")
    st.write("Este exemplo mostra como adicionar um slider de data.")
    date_input = st.date_input("Escolha uma data")
    st.write("Data selecionada:", date_input)

    # Exemplo 14: Carregamento de Arquivos
    st.header("Exemplo 14: Carregamento de Arquivos")
    st.write("Este exemplo demonstra como permitir que os usuários carreguem arquivos.")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["csv", "txt"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write(data)

    # Exemplo 15: API de Componentes do Streamlit
    st.header("Exemplo 15: API de Componentes do Streamlit")
    st.write("Este exemplo demonstra como usar os componentes de formulário do Streamlit.")
    name = st.text_input("Digite seu nome")
    st.write("Olá,", name)

    # Exemplo 16: Gráfico de Dispersão
    st.header("Exemplo 16: Gráfico de Dispersão")
    st.write("Este exemplo mostra como criar e exibir um gráfico de dispersão.")
    df = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon']
    )
    st.map(df)

    # Exemplo 17: Escolha de Cor
    st.header("Exemplo 17: Escolha de Cor")
    st.write("Este exemplo demonstra como adicionar um seletor de cor.")
    color = st.color_picker("Escolha uma cor", "#00f")
    st.write("Você escolheu a cor:", color)

    # Exemplo 18: Barra de Progresso
    st.header("Exemplo 18: Barra de Progresso")
    st.write("Este exemplo mostra como adicionar uma barra de progresso.")
    progress_bar = st.progress(0)
    for i in range(100):
        progress_bar.progress(i + 1)

    # Exemplo 19: Botão de Compartilhamento
    st.header("Exemplo 19: Botão de Compartilhamento")
    st.write("Este exemplo demonstra como adicionar um botão de compartilhamento.")
    if st.button("Compartilhar"):
        st.write("Compartilhado com sucesso!")

    # Exemplo 20: Gráfico de Linhas com Matplotlib
    st.header("Exemplo 20: Gráfico de Linhas com Matplotlib")
    st.write("Este exemplo mostra como criar e exibir um gráfico de linhas usando Matplotlib.")
    x = np.linspace(0, 20, 100)
    y = np.sin(x)
    plt.plot(x, y)
    st.pyplot(plt)

if __name__ == "__main__":
    main()