import streamlit as st
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

st.title('my-first-app')

st.info('Hi')

df = pd.read_csv('penguins.csv')
df
