import plotly.offline as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np

py.init_notebook_mode()

N = 500
random_x = np.linspace(0, 1, N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y
)

data = [trace]

py.iplot(data, filename='basic-line')
