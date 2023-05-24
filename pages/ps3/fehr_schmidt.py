import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Simple 2 Player Fehr Schmidt Utility Function")


gen_code = """
import streamlit as st
import numpy as np

def fehr_schmidt_plot(OTHER, alpha, beta):
    import numpy as np
    self_money = np.linspace(0,1001,1000)
    U = np.where(self_money < OTHER, self_money - (alpha * (OTHER - self_money)), self_money - (beta * (self_money - OTHER)))
    return U
    
def plotter(func, *args):
    import matplotlib.pyplot as plt #again,pls ignore
    import numpy as np
    self_money = np.linspace(0,1001,1000)

    y = func(*args)
    fig = plt.figure(figsize=(5, 2))
    plt.plot(self_money,y)
    plt.xlim(0,1000)
    plt.xlim(0,1000)
    plt.xlabel("Payoff Self")
    plt.ylabel("Utility")
    plt.plot(self_money,self_money, linestyle='--', alpha=0.5)
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