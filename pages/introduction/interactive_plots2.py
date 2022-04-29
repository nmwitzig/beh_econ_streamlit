import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Again: choose a function to plot")


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

def plotter(func, *args):
    import matplotlib.pyplot as plt #again,pls ignore
    import numpy as np
    y = func(time, *args)
    y_1 = np.roll(y,-1)
    y_1 = y_1[:-1]
    fig = plt.figure(figsize=(20, 8))
    plt.plot(time[:-1],(y_1/y[:-1]))
    plt.ylim(0,1,0.1)
    plt.xlim(0,MAX_TIME)
    plt.title("Per-period Discounting Factor")
    return st.pyplot(fig)

def plotter1(func, *args):
    import matplotlib.pyplot as plt #again,pls ignore
    import numpy as np
    y = func(time, *args)
    y_1 = np.roll(y,-1)
    y_1 = y_1[:-1]
    fig = plt.figure(figsize=(20, 8))
    plt.plot(time[:-1],((y[:-1]/y_1)-1))
    plt.ylim(0,1,0.1)
    plt.xlim(0,MAX_TIME)
    plt.title("Discount Rate")
    return st.pyplot(fig)

"""



with st.expander(label='Show Code', expanded=False):
    st.code(gen_code)
exec(gen_code, globals(), locals())



function_select = st.selectbox(
    'Please choose a function',
    ('Samuelson', 'Hyperbolic', 'Loewenstein', 'Quasi Hyperbolic'))

st.write(f'You have selected: **{function_select}**')

if function_select == 'Samuelson':
    st.write('Please choose a value for Delta')    
    delta = st.slider('Delta:', 0.0, 1.0, 0.9, 0.01)
    st.write("You chose Delta: ", delta)
    # generate two columns
    col1, col2 = st.columns(2)
    with col1:
        plotter(samuelson, delta)
    with col2:
        plotter1(samuelson, delta)

if function_select == 'Hyperbolic':
    col1, col2 = st.columns(2)
    with col1:
        plotter(hyperbolic)
    with col2:
        plotter1(hyperbolic)


if function_select == "Loewenstein":
    st.write('Please choose a value for Alpha')
    alpha = st.slider('Alpha:', 0.0, 10.0, 10.0, 0.1)
    st.write("You chose Alpha: ", alpha)
    st.write('Please choose a value for Beta')
    beta = st.slider('Beta:', 0.0, 10.0, 5.0, 0.1)
    st.write("You chose Beta: ", beta)
    col1, col2 = st.columns(2)
    with col1:
        plotter(loewenstein, alpha, beta)
    with col2:
        plotter1(loewenstein, alpha, beta)

if function_select == "Quasi Hyperbolic":
    st.write('Please choose a value for Beta')
    beta = st.slider('Beta:', 0.0, 1.0, 0.9, 0.01)
    st.write("You chose Beta: ", beta)
    st.write('Please choose a value for Delta')
    delta = st.slider('Delta:', 0.0, 1.0, 0.9, 0.01)
    st.write("You chose Delta: ", delta)
    col1, col2 = st.columns(2)
    with col1:
        plotter(quasi_hyperbolic,beta, delta)
    with col2:
        plotter1(quasi_hyperbolic,beta, delta)



