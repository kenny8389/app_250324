import streamlit as st
import numpy as np
import pandas as pd

st.title("ABC")
st.write("ABC")
st.header("ABC")
st.text("ABC")

st.write("# ABC")
st.write("## ABC")

a = np.array([[10,20,30],[100,200,300]])
st.write(a)
st.table(a)

b = pd.DataFrame([[10,20,30],[100,200,300]])
st.write(b)
st.table(b)


name = "kenny"
st.write(name,b[0])
st.info(name)

#核取方塊
st.write("### 核取方塊-------------------------")
re1 = st.checkbox("美食")
if re1 : 
    st.info("美食")
else :
    st.info("不愛美食")
re2 = st.checkbox("運動")
if re2 : 
    st.info("愛運動")
else :
    st.info("不愛運動")

#核取方塊2
st.write("### 核取方塊2-------------------------")
res = st.columns(3)
with res[0]:
    c1 = st.checkbox("A")
    if c1:
        st.info("a")
with res[1]:
    c2 = st.checkbox("B")
    if c2:
        st.info("b")
with res[2]:
    c3 = st.checkbox("C")
    if c3:
        st.info("c")    
#選項按鈕
st.write("### 選項按鈕-------------------------")
re3 = st.radio("性別:",("男","女","第三性"), index=1)
st.write(re3)
re4 = st.radio("性別:",("男","女","第三性"), index=1,key=58)
st.write(re4)

#選項按鈕2
st.write("### 選項按鈕2-------------------------")
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("請輸入任意整數")
with col2:
    num2 = st.number_input("請輸入任意整數",key=54547)
re4 = st.radio("計算:",("加","減","除","乘"),key="b")
if re4 == "加":
    st.write("{}+{}={}".format(num1,num2,num1+num2))
elif re4 == "減":
    st.write("{}-{}={}".format(num1,num2,num1-num2))
elif re4 == "乘":
    st.write("{}*{}={}".format(num1,num2,num1*num2))
elif re4 == "除":
    st.write("{}/{}={}".format(num1,num2,num1/num2))            
#滑桿
st.write("### 滑桿--------------------------")
re5 = st.slider("數量:" , 1.0 , 20.0, step=1.0)
st.info(re5)
#下拉選單
st.write("### 下拉選單--------------------------")
re6 = st.selectbox("分類器",("knn","svc","tree"))
st.write(re6)
       


