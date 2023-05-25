import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Simple 2 Player Fehr Schmidt Utility Function")


gen_code = """
import streamlit as st
import numpy as np

def fehr_schmidt_plot(SELF_CONST, alpha, beta):
    import numpy as np
    other_money = np.linspace(0,1001,1000)
    U = np.where(other_money > SELF_CONST, SELF_CONST - (alpha * (other_money - SELF_CONST)), SELF_CONST - (beta * (SELF_CONST - other_money)))
    return U
    
def plotter(func, *args):
    import matplotlib.pyplot as plt #again,pls ignore
    import numpy as np
    other_money = np.linspace(0,1001,1000)

    y = func(*args)
    fig = plt.figure(figsize=(5, 2))
    plt.plot(other_money,y)
    plt.xlim(0,1000)
    plt.xlim(0,1000)
    plt.xlabel("Payoff Other")
    plt.ylabel("Utility")
    plt.plot(other_money,other_money, linestyle='--', alpha=0.5)
    plt.title("Fehr-Schmidt Utility Function")
    return st.pyplot(fig)
"""



with st.expander(label='Show Code', expanded=False):
    st.code(gen_code)
exec(gen_code, globals(), locals())


# get field to input a number
st.write('Please choose a value for Self')
SELF_CONST = st.slider('Self:', 0, 1000, 500, 1)
st.write("You chose Self: ", SELF_CONST)

st.write('Please choose a value for Alpha')
alpha = st.slider('Alpha:', -1.0, 1.0, 0.0, 0.1)
st.write("You chose Alpha: ", alpha)


st.write('Please choose a value for Beta')
beta = st.slider('Beta:', -1.0, 1.0, 0.0, 0.1)
st.write("You chose Beta: ", beta)

plotter(fehr_schmidt_plot,SELF_CONST, alpha, beta)