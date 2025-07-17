# cars 
render: https://cars-7z5g.onrender.com




 Cars App
This is a simple web app where users can view, add, and manage cars.
You can try it live here:
👉 https://cars-7z5g.onrender.com

What This App Does
Displays a list of cars with information.

Lets you add new cars.

Lets you edit or delete cars.

How to Run This Cars App on Your Own Computer (Locally)
Follow these steps if you want to make this app run from your own laptop:

1️⃣ Install Node.js
Download it from here:
👉 https://nodejs.org/en/download/
(Pick the LTS version — it’s the one marked as “Recommended.”)

2️⃣ Clone the Project from GitHub
In your terminal or command prompt, type:

bash
Copy
Edit
git clone https://github.com/[your-username]/[your-repo-name].git
Make sure to replace [your-username] and [your-repo-name] with your actual GitHub info.

3️⃣ Go Into the Project Folder
bash
Copy
Edit
cd [your-repo-name]
4️⃣ Install App Dependencies
bash
Copy
Edit
npm install
5️⃣ Start the App Locally
bash
Copy
Edit
npm start
You’ll see something like:

arduino
Copy
Edit
Server is running on http://localhost:3000
6️⃣ Open the App in Your Browser
Go to:

arduino
Copy
Edit
http://localhost:3000
Now you can use the Cars app locally on your computer!

Notes
Make sure you have Node.js version 18 or higher.

If anything doesn’t work, try running:

nginx
Copy
Edit
npm install
again to make sure everything installed correctly.

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