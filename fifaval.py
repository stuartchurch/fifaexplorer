import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


#url = "https://github.com/stuartchurch/fifaexplorer/blob/main/All_Player_List.csv"
#@st.cache       
df = st.cache(pd.read_csv)("All_Player_List.csv")
#df = pd.read_csv("All_Player_List.csv")
df['delta'] = df['Potential Score'] - df['Overall Score']

st.title("Exploring the Market Value of FIFA 20 Players")

marketvalue = st.sidebar.slider("Market value",0,150000000, (0,150000000))
#marketvalue = st.sidebar.slider("Market value (GBP)",df['Market Value'].min(),df['Market Value'].max(), (df['Market Value'].min(),df['Market Value'].max()))
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
