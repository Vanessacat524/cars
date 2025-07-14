# cars 
render: https://cars-7z5g.onrender.com



 Checkbox Toggle
The st.checkbox widget toggles which plot is rendered. Checking it switches to a scatter plot, unchecking displays the histogram—creating dynamic, interactive behavior.

 Plotly Figures
px.histogram(...) builds the distribution of price.

px.scatter(...) plots odometer vs price, colored by condition.

Plotly Express (px) is ideal for clean and quick visualizations from DataFrames 
Galaxy
+2
plotly.com
+2
GitHub
+2


 Embedding with st.plotly_chart
st.plotly_chart(fig, use_container_width=True) renders the interactive Plotly figure.

Including use_container_width=True ensures the chart auto-resizes to fill its container, making it responsive across different screens and devices.