import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd

st.header('Homework 1')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)

x_limit = 100

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(0,x_limit,1)

# Create a random array of data that we will use for our y values
y_data = np.random.randint(1,101, x_limit)

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)


st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)

scatter = alt.Chart(df).mark_point().encode(x='x',y='y')

st.altair_chart(scatter, use_container_width=True)


st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)

st.markdown("The five changes I made were.....")
st.markdown("""
The 5 changes I made were:
- change point color to green
- change point opacity to 50%
- change point size to 80
- change point to be filled
- change default Streamlit theme to native Altair theme
""")
scatter = alt.Chart(df).mark_point(size=80,opacity=0.5,color='green', filled=True).encode(x='x',y='y')
st.altair_chart(scatter, theme=None, use_container_width=True)


st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)

bar = alt.Chart(df).mark_bar().encode(alt.X('y', bin=True), y='count()')
st.altair_chart(bar, use_container_width=True)

st.markdown("""
The 2 changes I made were:
- change number of bins to 5
- change bar color to green
"""
)

bar = alt.Chart(df).mark_bar(color='green').encode(alt.X('y', bin=alt.Bin(maxbins=5)), y='count()')
st.altair_chart(bar, use_container_width=True)

#my_chart = (bar + line)
