import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Start: Exponential Discounting")


col_a, col_b = st.columns(2)



gen_code = """
import numpy as np
import pandas as pd
MAX_TIME = 20

# Define function
def samuelson(x, delta=0.9):
    return delta**x

# Generate time variable, apply function
time = np.arange(0,MAX_TIME + 1,1)
y_a = samuelson(time)

# Show first 5 Elements of y vector
df = pd.DataFrame({"time": time, "y": y_a})
st.dataframe(df.head())
"""

plot_code = """
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5, 2))
plt.plot(time,y_a)
plt.title("Samuelson")
plt.xlabel("Time")
plt.ylabel("Discount Factor")
st.pyplot(fig)
"""
with col_a:
    st.write("### Generate Data")
    with st.expander(label='Show Code'):
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