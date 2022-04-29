import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Choose a function to plot")


gen_code = """
import streamlit as st
import numpy as np
MAX_TIME = 20

time = np.arange(0,MAX_TIME+1,1)

def samuelson(x, delta=0.9):
    return delta**x

def hyperbolic(x):
    return 1/(x+1)

def loewenstein(x, alpha = 10, beta = 5):
    m = (1 + alpha * x)
    e = beta/alpha
    return 1/(m**e)

def quasi_hyperbolic(x,beta=0.9, delta=0.9):
    import numpy as np #ignore
    return np.where(x > 0, beta*(delta**x), 1)

def plotter(func,time, *args):
    import matplotlib.pyplot as plt #again,pls ignore
    y = func(time, *args)
    fig = plt.figure(figsize=(20, 8))
    plt.plot(time,y)
    plt.ylim(0,1,0.1)
    plt.xlim(0,MAX_TIME)
    return st.pyplot(fig)
"""



with st.expander(label='Show Code', expanded=False):
    st.code(gen_code)
exec(gen_code, globals())



function_select = st.selectbox(
    'Please choose a function',
    ('Samuelson', 'Hyperbolic', 'Loewenstein', 'Quasi Hyperbolic'))

st.write(f'You have selected: **{function_select}**')

if function_select == 'Samuelson':
    st.write('Please choose a value for Delta')    
    delta = st.slider('Delta:', 0.0, 1.0, 0.9, 0.01)
    st.write("You chose Delta: ", delta)
    plotter(samuelson,time, delta)

if function_select == 'Hyperbolic':
    plotter(hyperbolic,time)

if function_select == "Loewenstein":
    st.write('Please choose a value for Alpha')
    alpha = st.slider('Alpha:', 0.0, 10.0, 10.0, 0.1)
    st.write("You chose Alpha: ", alpha)
    st.write('Please choose a value for Beta')
    beta = st.slider('Beta:', 0.0, 10.0, 5.0, 0.1)
    st.write("You chose Beta: ", beta)
    plotter(loewenstein,time, alpha, beta)

if function_select == "Quasi Hyperbolic":
    st.write('Please choose a value for Beta')
    beta = st.slider('Beta:', 0.0, 1.0, 0.9, 0.01)
    st.write("You chose Beta: ", beta)
    st.write('Please choose a value for Delta')
    delta = st.slider('Delta:', 0.0, 1.0, 0.9, 0.01)
    st.write("You chose Delta: ", delta)
    plotter(quasi_hyperbolic,time, beta, delta)