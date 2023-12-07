import pandas as pd
import matplotlib.pyplot as plt

# Using Excel data to generate line plot
#excel_file = 'demo.xlsx'
# Read the Excel file using pandas
#df = pd.read_excel(excel_file)

# Using csv file to generate line plot.
csv_file = 'demo.csv'
df = pd.read_csv(csv_file)

# Assuming your Excel file has columns 'x' and 'y' for the data
x = df['x']
y = df['y']

# Create a line plot
print(x)
print(y)
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sample Line Plot')

# Show the plot (you can also save it to a file using plt.savefig())
plt.show()
