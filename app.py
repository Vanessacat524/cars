import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv('/Users/anits/tripleten_test/vehicles_us.csv')

# Example histograms
fig = px.histogram(df, x='price')
fig.show()

# Example scatterplot
fig = px.scatter(df, x='odometer', y='price', color='condition')
fig.show()