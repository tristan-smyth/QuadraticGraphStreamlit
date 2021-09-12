import streamlit as st
import base64
import time
import os
from io import StringIO, BytesIO
import base64
import streamlit as st
import plotly.express as px

class MultiApp:

    # from myLibary import MultiApp
    # app = MultiApp()
    #
    # -- add a app --
    # app.add_app("Text",file.app)
    # ------
    # ------
    # app.run()
    #
    # in file name main function app
    # def app():
    #   code

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        app = st.sidebar.selectbox('Navagation', self.apps, format_func=lambda app: app['title'])
        app['function']()


def raw_text_downloader(raw_text, text="Click Me"):
    timestr = time.strftime("%d/%m/%Y %H.%M.%S")
    b64 = base64.b64encode(raw_text.encode()).decode()
    new_filename = "quadratic_data_{}.txt".format(timestr)
    href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">{text}</a>'
    st.markdown("{}".format(href), unsafe_allow_html=True)


def plot_downloader(plot, text="Click Me"):
    timestr = time.strftime("%d/%m/%Y %H.%M.%S")
    mybuff = StringIO()
    plot.write_html(mybuff, include_plotlyjs='cdn')
    mybuff = BytesIO(mybuff.getvalue().encode())
    b64 = base64.b64encode(mybuff.read()).decode()
    href = f'<a href="data:text/html;charset=utf-8;base64, {b64}" download="{"quadratic_plot_"+timestr+".html"}">{text}</a>'
    st.markdown(href, unsafe_allow_html=True)


