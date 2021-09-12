import streamlit as st
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from myLibary import raw_text_downloader,plot_downloader
import plotly.graph_objects as go

def app():
    # --- Options ----------------------------------------------------------------------------------------
    st.set_option('deprecation.showPyplotGlobalUse', False)
    pd.set_option('display.max_rows', 1000)
    st.title("Quadratic App")

    # --- Side Bar -----------------------------------------------------------------------------------------------------

    exp1 = st.sidebar.expander("X Y Values")
    exp2 = st.sidebar.expander("Graph Colors")

    colorLine = exp2.color_picker('Line Color', '#13F1A7')
    lineWidth = exp2.slider("Line Width", min_value=1, max_value=10, value=1)
    colorSpike = exp2.color_picker('Spike Color', '#F3470F')
    spikeWidth = exp2.slider("Spike Width", min_value=1, max_value=10, value=1)
    # colorAxisText = exp2.color_picker('Axis Text Color', '#FFFFFF')
    # colorText = exp2.color_picker('Text Color', '#000000')
    # colorBg = exp2.color_picker("Background Color","#000000")


    # --- Functions ----------------------------------------------------------------------------------------------------

    def drawGraphPlotly(a, b, c, xmin, xmax, points, container=st): #--- Test

        x = np.linspace(xmin, xmax, points)
        y = (a * (x ** 2)) + (b * x) + c

        df = pd.DataFrame({"x": x, "y": y})
        exp1.table(df)

        fig = go.Figure(data=go.Line(x=x, y=y,line_color=colorLine,line_width=lineWidth))
        fig.layout.title = "ax² + bx + c"
        fig.update_xaxes(zeroline=True, zerolinewidth=3, zerolinecolor='Black')
        fig.update_yaxes(zeroline=True, zerolinewidth=3, zerolinecolor='Black')

        fig.layout.yaxis.showspikes = True
        fig.layout.xaxis.showspikes = True

        fig.layout.yaxis.spikecolor = colorSpike
        fig.layout.xaxis.spikecolor = colorSpike

        fig.layout.yaxis.spikethickness = spikeWidth
        fig.layout.xaxis.spikethickness = spikeWidth

        container.plotly_chart(fig)


        y_intercept = (numBoxA * (0 ** 2)) + (numBoxB * 0) + numBoxC
        st.text(f"Y Intercept = {y_intercept}")
        raw_text_downloader("{}".format(df),text="Download Data")
        plot_downloader(fig,text="Download Plot")




    # --- Columns ------------------------------------------------------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:
        numBoxA = st.number_input(value=0.0, label="A")

        numBoxB = st.number_input(value=0.0, label="B")
        numBoxC = st.number_input(value=0.0, label="C")

    with col2:
        xMin = st.number_input(label="X Min", value=-10)

        xMax = st.number_input(label="X Max", value=10)

        points = st.number_input(label="Points", value=100)

    # --- Body ---------------------------------------------------------------------------------------------------------

    drawGraphPlotly(numBoxA, numBoxB, numBoxC, xMin, xMax, points)



app()