import time
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import threading
#import dummy
#import pyodbc
import plotly.graph_objects as go
import socket
import pycomm3


# Page setting
st.set_page_config(page_title='Factory of the future',layout="wide",page_icon = 'Logo.png',initial_sidebar_state = 'auto')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
#Dashboard
#Main
def main():
        
    # Row 1
    first_title = '<p style="font-family:sans-serif; color:Gray; background-color: #000000; font-size: 42px;">Factory Of The Future</p>'
    a1, a2, = st.columns((2,8))
    a1.image(Image.open('LinamarLogo.png'))
    a2.markdown(first_title, unsafe_allow_html=True)

    #Row 2
    video_file = open('myvideo.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
#Turning
def turning():
    
    # Data collection from C# Fanuc Focas program by using socket
    HOST = 'localhost'
    PORT = 5000
    cycletime = 1.5 # Minutes
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = s.recv(1024)
    string_data = data.decode()
    values = string_data.split(",")

    # Using a list to store values with dynamically generated variable names
    for i in range(len(values)):
        var_name = f"var{i+1}"
        exec(f"{var_name} = '{values[i]}'")
    
    # Row 1
    first_title = '<p style="font-family:sans-serif; color:Gray; background-color: #000000; font-size: 42px;">Turning Tool Change Schedule</p>'
    a1, a2, = st.columns((2,8))
    a1.image(Image.open('LinamarLogo.png'))
    a2.markdown(first_title, unsafe_allow_html=True)
    
    # Row 2
    # Gauge Tool 1
    if ((int(values[0])*cycletime)<50):
        colorcode1 = "red"
    elif ((int(values[0])*cycletime)<150):
        colorcode1 = "yellow"
    elif ((int(values[0])*cycletime)<600):
        colorcode1 = "green"

    fig1 = go.Figure(go.Indicator(
    domain = {'x': [0.3, 1], 'y': [0.5, 1]},
    value = (int(values[0])*cycletime),
    number={'suffix': " Min", 'font_color':colorcode1, 'font_size':20},
    mode = "gauge+number",
    title = {'text': "Tool 1", 'font_size':35},
    gauge = {'axis': {'range': [None, 300], 'tickwidth': 1, 'tickcolor': "white"},
             'bar': {'color': "darkblue"},
             'steps' : [
                 {'range': [0, 50], 'color': "red"},
                 {'range': [50, 150], 'color': "yellow"},
                 {'range': [150, 300], 'color': "lightgreen"}]}))
    
    # Gauge Tool 2
    if ((int(values[1])*cycletime)<50):
        colorcode2 = "red"
    elif ((int(values[1])*cycletime)<150):
        colorcode2 = "yellow"
    elif ((int(values[1])*cycletime)<600):
        colorcode2 = "green"

    fig2 = go.Figure(go.Indicator(
    domain = {'x': [0.3, 1], 'y': [0.5, 1]},
    value = (int(values[1])*cycletime),
    number={'suffix': " Min", 'font_color':colorcode2, 'font_size':20},
    mode = "gauge+number",
    title = {'text': "Tool 2", 'font_size':35},
    gauge = {'axis': {'range': [None, 300], 'tickwidth': 1, 'tickcolor': "white"},
             'bar': {'color': "darkblue"},
             'steps' : [
                 {'range': [0, 50], 'color': "red"},
                 {'range': [50, 150], 'color': "yellow"},
                 {'range': [150, 300], 'color': "lightgreen"}]}))
    
    # Gauge Tool 3
    if ((int(values[2])*cycletime)<50):
        colorcode3 = "red"
    elif ((int(values[2])*cycletime)<150):
        colorcode3 = "yellow"
    elif ((int(values[2])*cycletime)<600):
        colorcode3 = "green"

    fig3 = go.Figure(go.Indicator(
    domain = {'x': [0.3, 1], 'y': [0.5, 1]},
    value = (int(values[2])*cycletime),
    number={'suffix': " Min", 'font_color':colorcode3, 'font_size':20},
    mode = "gauge+number",
    title = {'text': "Tool 3", 'font_size':35},
    gauge = {'axis': {'range': [None, 300], 'tickwidth': 1, 'tickcolor': "white"},
             'bar': {'color': "darkblue"},
             'steps' : [
                 {'range': [0, 50], 'color': "red"},
                 {'range': [50, 150], 'color': "yellow"},
                 {'range': [150, 300], 'color': "lightgreen"}]}))
    
    # Gauge Tool 4
    if ((int(values[3])*cycletime)<50):
        colorcode4 = "red"
    elif ((int(values[3])*cycletime)<150):
        colorcode4 = "yellow"
    elif ((int(values[3])*cycletime)<600):
        colorcode4 = "green"

    fig4 = go.Figure(go.Indicator(
    domain = {'x': [0.3, 1], 'y': [.5, 1]},
    value = (int(values[3])*cycletime),
    number={'suffix': " Min", 'font_color':colorcode4, 'font_size':20},
    mode = "gauge+number",
    title = {'text': "Tool 4", 'font_size':35},
    gauge = {'axis': {'range': [None, 300], 'tickwidth': 1, 'tickcolor': "white"},
             'bar': {'color': "darkblue"},
             'steps' : [
                 {'range': [0, 50], 'color': "red"},
                 {'range': [50, 150], 'color': "yellow"},
                 {'range': [150, 300], 'color': "lightgreen"}]}))
    
    # Gauge Tool 5
    if ((int(values[4])*cycletime)<50):
        colorcode5 = "red"
    elif ((int(values[4])*cycletime)<150):
        colorcode5 = "yellow"
    elif ((int(values[4])*cycletime)<600):
        colorcode5 = "green"
        
    fig5 = go.Figure(go.Indicator(
    domain = {'x': [0.3, 1], 'y': [0.5, 1]},
    value = (int(values[4])*cycletime),
    number={'suffix': " Min", 'font_color':colorcode5, 'font_size':20},
    mode = "gauge+number",
    title = {'text': "Tool 5", 'font_size':35},
    gauge = {'axis': {'range': [None, 300], 'tickwidth': 1, 'tickcolor': "white"},
             'bar': {'color': "darkblue"},
             'steps' : [
                 {'range': [0, 50], 'color': "red"},
                 {'range': [50, 150], 'color': "yellow"},
                 {'range': [150, 300], 'color': "lightgreen"}]}))
    
    # Gauge Tool 6
    if ((int(values[5])*cycletime)<50):
        colorcode6 = "red"
    elif ((int(values[5])*cycletime)<150):
        colorcode6 = "yellow"
    elif ((int(values[5])*cycletime)<600):
        colorcode6 = "green"
        
    fig6 = go.Figure(go.Indicator(
    domain = {'x': [0.3, 1], 'y': [0.5, 1]},
    value = (int(values[5])*cycletime),
    number={'suffix': " Min", 'font_color':colorcode6, 'font_size':20},
    mode = "gauge+number",
    title = {'text': "Tool 6" ,'font_size':35},
    gauge = {'axis': {'range': [None, 300], 'tickwidth': 1, 'tickcolor': "white"},
             'bar': {'color': "darkblue"},
             'steps' : [
                 {'range': [0, 50], 'color': "red"},
                 {'range': [50, 150], 'color': "yellow"},
                 {'range': [150, 300], 'color': "lightgreen"}]}))
    
    # Gauge Tool 7
    if ((int(values[6])*cycletime)<50):
        colorcode7 = "red"
    elif ((int(values[6])*cycletime)<150):
        colorcode7 = "yellow"
    elif ((int(values[6])*cycletime)<600):
        colorcode7 = "green"
        
    fig7 = go.Figure(go.Indicator(
    domain = {'x': [0.3, 1], 'y': [0.5, 1]},
    value = (int(values[6])*cycletime),
    number={'suffix': " Min", 'font_color':colorcode7, 'font_size':20},
    mode = "gauge+number",
    title = {'text': "Tool 7", 'font_size':35},
    gauge = {'axis': {'range': [None, 300], 'tickwidth': 1, 'tickcolor': "white"},
             'bar': {'color': "darkblue"},
             'steps' : [
                 {'range': [0, 50], 'color': "red"},
                 {'range': [50, 150], 'color': "yellow"},
                 {'range': [150, 300], 'color': "lightgreen"}]}))
    
    # Gauge Tool 8
    if ((int(values[7])*cycletime)<50):
        colorcode8 = "red"
    elif ((int(values[7])*cycletime)<150):
        colorcode8 = "yellow"
    elif ((int(values[7])*cycletime)<600):
        colorcode8 = "green"
        
    fig8 = go.Figure(go.Indicator(
    domain = {'x': [0.3, 1], 'y': [.5, 1]},
    value = (int(values[7])*cycletime),
    number={'suffix': " Min", 'font_color':colorcode8, 'font_size':20},
    mode = "gauge+number",
    title = {'text': "Tool 8", 'font_size':35},
    gauge = {'axis': {'range': [None, 300], 'tickwidth': 1, 'tickcolor': "white"},
             'bar': {'color': "darkblue"},
             'steps' : [
                 {'range': [0, 50], 'color': "red"},
                 {'range': [50, 150], 'color': "yellow"},
                 {'range': [150, 300], 'color': "lightgreen"}]}))
    
    
    c1,c2, c3, c4, c5, c6, c7, c8 = st.columns(8)
    with c1:
        st.plotly_chart(fig1, use_container_width=True)
    with c2:
        st.plotly_chart(fig2, use_container_width=True)
    with c3:
        st.plotly_chart(fig3, use_container_width=True)
    with c4:
        st.plotly_chart(fig4, use_container_width=True)
    with c5:
        st.plotly_chart(fig5, use_container_width=True)
    with c6:
        st.plotly_chart(fig6, use_container_width=True)
    with c7:
        st.plotly_chart(fig7, use_container_width=True)
    with c8:
        st.plotly_chart(fig8, use_container_width=True)

#Broach
def broach():
    # Row 1
    first_title = '<p style="font-family:sans-serif; color:Gray; background-color: #000000; font-size: 42px;">Broach Tool Change Schedule</p>'
    a1, a2, = st.columns((2,8))
    a1.image(Image.open('LinamarLogo.png'))
    a2.markdown(first_title, unsafe_allow_html=True)

    #Row 2
       
    second_title = '<p style="font-family:sans-serif; color:Gray; background-color: #ffffff; border-radius: 10px; font-size: 22px;"> July 14,2023 Change Tool 2 </p>'
    st.markdown(second_title, unsafe_allow_html=True)

#HeatTreat
def heattreat():
    # Row 1
    first_title = '<p style="font-family:sans-serif; color:Gray; background-color: #000000; font-size: 42px;">Heat Treat Coil Change Schedule</p>'
    a1, a2, = st.columns((2,8))
    a1.image(Image.open('LinamarLogo.png'))
    a2.markdown(first_title, unsafe_allow_html=True)

    #Row 2
    second_title = '<p style="font-family:sans-serif; color:Gray; background-color: #ffffff; border-radius: 10px; font-size: 22px;"> July 14,2023 Change Coil </p>'
    st.markdown(second_title, unsafe_allow_html=True)
    
#Binpick Cell
def binpick():
    
    #Data
    # define variables
    path = '10.174.90.100/5'
    fof_tag = 'Bin_Low'

    with pycomm3.LogixDriver(path) as PLC:

        # If connected to PLC then run loop
            if PLC.connected:
                fof_data = PLC.read(fof_tag)
    
    # Row 1
    first_title = '<p style="font-family:sans-serif; color:Gray; background-color: #000000; font-size: 42px;">Heat Treat Coil Change Schedule</p>'
    a1, a2, = st.columns((2,8))
    a1.image(Image.open('LinamarLogo.png'))
    a2.markdown(first_title, unsafe_allow_html=True)

    #Row 2
    if fof_data.value:
        second_title = '<p style="font-family:sans-serif; color:Gray; background-color: #ffffff; border-radius: 10px; font-size: 22px;"> low </p>'
        st.markdown(second_title, unsafe_allow_html=True)
    else:
        second_title = '<p style="font-family:sans-serif; color:Gray; background-color: #ffffff; border-radius: 10px; font-size: 22px;"> High </p>'
        st.markdown(second_title, unsafe_allow_html=True)
        
#Page Selection Names
page_names_to_funcs = {
    "Main Page": main,
    "Turning": turning,
    "Broaching": broach,
    "Heat Treat": heattreat,
    "Bin Pick Cell": binpick,
}

#Page Selection Function
selected_page = st.sidebar.selectbox("Select a Process to see schedule", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
