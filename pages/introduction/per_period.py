import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

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

time = np.arange(0,MAX_TIME + 1,1)
y_a = samuelson(time)
y_b = hyperbolic(time)
y_c = loewenstein(time)
y_d = quasi_hyperbolic(time)


st.title("Per period discounting factor + Discount rates")





gen_code = """
# Previous code imported and executed here
# from more_fn import gen_code
# exec(gen_code)

import numpy as np
y_list = [y_a, y_b, y_c, y_d]
y_1_list = [np.roll(y,-1) for y in y_list]

y_list = [y[:-1] for y in y_list]
y_1_list = [y[:-1] for y in y_1_list]

labels = ['A', 'B', 'C', 'D']
colors = ['r', 'b', 'g', 'y']
"""


plot_code1 = """
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5, 2))
for y, y1, label, color in zip(y_list, y_1_list, labels, colors):
    plt.plot(time[:-1],(y1/y), color, label=label)
plt.legend()
plt.title("Per-period Discounting Factors")
st.pyplot(fig)
"""

plot_code2 = """
fig = plt.figure(figsize=(5, 2))
for y, y1, label, color in zip(y_list, y_1_list, labels, colors):
    plt.plot(time[:-1],((y/y1)-1), color, label=label)
plt.legend()
plt.title("Discount Rates")  
st.pyplot(fig)
"""

st.write("### Preliminaries")
with st.expander(label='Show Code', expanded=False):
    st.code(gen_code)
exec(gen_code, globals(), locals())



col_a, _, col_c = st.columns([5, 1, 5])
with col_a:
    st.write("### Plot PPDF")
    with st.expander(label='Show Code'):
        st.code(plot_code1)

    #st.write("### Output: Plot Data")
    exec(plot_code1, globals(), locals())

with col_c:
    st.write("### Plot DR")
    with st.expander(label='Show Code'):
        st.code(plot_code2)

    #st.write("### Output: Plot Data")
    exec(plot_code2, globals(), locals())

    #try:
    #    exec(st_code)
    #except Exception as e:
    #    st.error(f"Error: {e}")

