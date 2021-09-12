import streamlit as st
from apps import home,quadraticGraph
from myLibary import MultiApp

app = MultiApp()
app.add_app("Home", home.app)
app.add_app("Quadratic Graph",quadraticGraph.app)

app.run()