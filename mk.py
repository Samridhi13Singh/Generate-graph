import streamlit as st
import matplotlib.pyplot as plt

st.title("Mark Visualisation Graph")
st.subheader("Enter your subject marks: ")

subject = ['English','Science','Math','Social','AI']

marks = []


for i in subject:
    str_val='Enter the marks of'+i
    mark = st.number_input(str_val,min_value=0,max_value=100,value=0)
    marks.append(mark)

if st.button('Genrate a Graph'):
    if any(marks):
        fig,ax=plt.subplots()
        ax.plot(subject,marks,marker='o',color='blue',linestyle='-',linewidth=3)
        ax.set_title("Marks of the Student")
        ax.set_ylim(0,120)
        ax.set_xlabel('<------Subject------->')
        ax.set_ylabel('<-------Marks-------->')
        st.pyplot(fig)

    else:
        st.warning("Please enter atleast one subject marks")