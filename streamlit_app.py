import streamlit as st
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

st.title('my-first-app')

st.info('Hi')

with st.expander('data'):
  st.write('raw data')
  df = pd.read_csv('penguins.csv')
  df

  X = df.drop('species',axis=1)
  y = df.species

with st.expander('data_visualization'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')
