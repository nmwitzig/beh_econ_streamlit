import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Simple 2 Player Fehr Schmidt Utility Function")


gen_code = """
import streamlit as st
import numpy as np
MAX_SELF = 1000

self_money = np.linspace(0,MAX_SELF+1,1000)

def fehr_schmidt_plot(self_money,OTHER, alpha, beta):
    U = np.where(self_money < OTHER, self_money - (alpha * (OTHER - self_money)), self_money - (beta * (self_money - OTHER)))
    return U
    
def plotter(func, *args):
    import matplotlib.pyplot as plt #again,pls ignore
    import numpy as np
    y = func(self_money, *args)
    fig = plt.figure(figsize=(5, 2))
    plt.plot(self_money,y)
    plt.xlim(0,MAX_SELF)
    plt.xlim(0,MAX_SELF)
    plt.xlabel("Self")
    plt.ylabel("Utility")
    plt.title("Fehr-Schmidt Utility Function")
    return st.pyplot(fig)
"""



with st.expander(label='Show Code', expanded=False):
    st.code(gen_code)
exec(gen_code, globals(), locals())


# get field to input a number
st.write('Please choose a value for Other')
OTHER = st.slider('Other:', 0, 1000, 500, 1)
st.write("You chose Other: ", OTHER)

st.write('Please choose a value for Alpha')
alpha = st.slider('Alpha:', -1.0, 1.0, 0.0, 0.1)
st.write("You chose Alpha: ", alpha)


st.write('Please choose a value for Beta')
beta = st.slider('Beta:', -1.0, 1.0, 0.0, 0.1)
st.write("You chose Beta: ", beta)

plotter(fehr_schmidt_plot,OTHER, alpha, beta)