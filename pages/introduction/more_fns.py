import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("More Discount Functions")


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

time = np.arange(0,MAX_TIME + 1,1)
y_a = samuelson(time)
y_b = hyperbolic(time)
y_c = loewenstein(time)
y_d = quasi_hyperbolic(time)
"""


plot_code = """
import matplotlib.pyplot as plt
import streamlit as st

fig = plt.figure(figsize=(2.5, 1))
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
    exec(gen_code, globals(), locals())



with col_b:
    st.write("### Plot Data")
    with st.expander(label='Show Code'):
        st.code(plot_code)

    #st.write("### Output: Plot Data")
    exec(plot_code, globals(), locals())

    #try:
    #    exec(st_code)
    #except Exception as e:
    #    st.error(f"Error: {e}")
