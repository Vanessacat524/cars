# cars 
render: https://cars-7z5g.onrender.com

Make the table of cars
We create a table (called a DataFrame) that lists different cars—like their brand, model, year, and price.

Add a "Run" button
We put a button in the app that says Run. Nothing happens until you click it.

Filter the cars when you click
When you press Run, the app checks the table and pulls out only the cars that are Ford or Jeep.

Show the filtered list
Finally, the app shows a smaller table with just the Ford and Jeep cars.



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