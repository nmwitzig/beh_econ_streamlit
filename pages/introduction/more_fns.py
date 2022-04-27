import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Start: Generate and plot data")


col_a, col_b = st.columns(2)


gen_code = """
import numpy as np
MAX_TIME = 20

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

time = np.linspace(0,MAX_TIME + 1,100)
y_a = samuelson(time)
y_b = hyperbolic(time)
y_c = loewenstein(time)
y_d = quasi_hyperbolic(time)
"""


plot_code = """
import matplotlib.pyplot as plt
import streamlit as st

fig = plt.figure(figsize=(10, 4))
plt.plot(time,y_a, 'r', label="A")
plt.plot(time,y_b, 'b', label="B")
plt.plot(time,y_c, 'g', label="C")
plt.plot(time,y_d, 'y', label="D")
plt.legend()
plt.title("Time Discounting Functions")
st.pyplot(fig)
"""
with col_a:
    st.write("### Generate Data")
    with st.expander(label='Show Code', expanded=True):
        st.code(gen_code)
    #st.write("### Generated Data")
    exec(gen_code)



with col_b:
    st.write("### Plot Data")
    with st.expander(label='Show Code'):
        st.code(plot_code)

    #st.write("### Output: Plot Data")
    exec(plot_code)


    #try:
    #    exec(st_code)
    #except Exception as e:
    #    st.error(f"Error: {e}")




#%%
import numpy as np
MAX_TIME = 20

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

# np.linspace with stepsize of 1
time = np.arange(0,MAX_TIME + 1, 1)
y_a = samuelson(time)
y_b = hyperbolic(time)
y_c = loewenstein(time)
y_d = quasi_hyperbolic(time)


#%%
import matplotlib.pyplot as plt

#%%
# shift y_a one to the left
y_list = [y_a, y_b, y_c, y_d]
y_1_list = [np.roll(y,-1) for y in y_list]

#%%
y_list = [y[:-1] for y in y_list]
y_1_list = [y[:-1] for y in y_1_list]

labels = ['A', 'B', 'C', 'D']
colors = ['r', 'b', 'g', 'y']

#%%
fig = plt.figure(figsize=(10, 4))
for y, y1, label, color in zip(y_list, y_1_list, labels, colors):
    plt.plot(time[:-1],(y1/y), color, label=label)
plt.legend()
plt.title("Per-period Discounting Functions")
    


#%%
fig = plt.figure(figsize=(10, 4))
for y, y1, label, color in zip(y_list, y_1_list, labels, colors):
    plt.plot(time[:-1],((y/y1)-1), color, label=label)
plt.legend()
plt.title("Discount Rates")  

