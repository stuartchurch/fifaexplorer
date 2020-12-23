import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

#@st.cache
df = pd.read_csv('All_Player_List.csv')
df['delta'] = df['Potential Score'] - df['Overall Score']

st.title("Exploring the Market Value of FIFA 20 Players")

marketvalue = st.sidebar.slider("Market value (£)",df['Market Value'].min(),df['Market Value'].max(), (df['Market Value'].min(),df['Market Value'].max()))
overall = st.sidebar.slider("Overall Score",0,100, (0,100))
delta = st.sidebar.slider("Potential Increase",0,20,(0,20))
mental = st.sidebar.slider("Mental strength",0,100, (0,100))
ballskills = st.sidebar.slider("Ball skills",0,100, (0,100))

df = df[(df['Overall Score'] >= overall[0])
        & (df['Overall Score'] <= overall[1])
        & (df['delta'] >= delta[0])
        & (df['delta'] <= delta[1])
        & (df['Market Value'] >= marketvalue[0])
        & (df['Market Value'] <= marketvalue[1])
        & (df['Mental'] >= mental[0])
        & (df['Mental'] <= mental[1])
        & (df['Ball Skills'] >= ballskills[0])
        & (df['Ball Skills'] <= ballskills[1])]

st.header("First 50 results")

st.dataframe(df.head(50))

st.header("Choose chart options:")

X = st.selectbox('X-axis',['Overall Score', 'Market Value', 'Potential Score','Mental','Ball Skills','Age'])
Y = st.selectbox('Y-axis',['Market Value', 'Overall Score', 'Potential Score', 'Mental','Ball Skills','Age'])

fig, ax = plt.subplots()
plt.scatter(df[X],df[Y])
plt.xlabel(X)
plt.ylabel(Y)
plt.show()
st.pyplot(fig)


#ordered_df = df.sort_values(by='Age')
#my_range=range(1,len(df.index)+1)

import seaborn as sns
#fig2 = plt.figure(figsize=(20, 50))
#plt.hlines(y=my_range, xmin=ordered_df['Overall Score'], xmax=ordered_df['Potential Score'], color='gray', alpha=0.4)
#plt.scatter(ordered_df['Overall Score'], my_range, color='black', s=20, alpha=1, label='Overall Score')
#plt.scatter(ordered_df['Potential Score'], my_range, color='red', s=20, alpha=1 , label='Potential Score')
#plt.legend()
#st.pyplot(fig2)




#MarketValue = st.sidebar.slider("Market Value",0,120000000,(df['Market Value'].min(),df['Market Value'].max()))
#OverallScore = st.sidebar.slider("Overall Score",0,100,(df['Overall Score'].min(),df['Overall Score'].max()))
#PotentialScore = st.sidebar.slider("Potential Score",0,100,(df['Potential Score'].min(),df['Potential Score'].max()))
#BallSkills = st.sidebar.slider("Ball Skills",0,100,(df['Ball Skills'].min(),df['Ball Skills'].max()))
#Mental = st.sidebar.slider("Mental ability",0,100,(df['Mental'].min(),df['Mental'].max()))
#Potential = st.sidebar.slider("Potential increase",0,20, (df['delta'].min(),df['delta'].max()))

# To run:   streamlit run ~/Library/Application\ Support/JetBrains/PyCharmCE2020.2/scratches/fifaval.py
#  http://localhost:8501/
