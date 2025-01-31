#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas matplotlib numpy')


# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
days = pd.date_range(start="2024-01-01", periods=30, freq='D')
temperature = np.random.randint(low=10, high=35, size=30)  # Random temperatures
humidity = np.random.randint(low=30, high=90, size=30)  # Random humidity levels

weather_data = pd.DataFrame({'Date': days, 'Temperature (°C)': temperature, 'Humidity (%)': humidity})

print("Weather Data Preview:")
display(weather_data.head())

plt.figure(figsize=(10, 5))
plt.plot(weather_data['Date'], weather_data['Temperature (°C)'], marker='o', label="Temperature (°C)", color='red')
plt.plot(weather_data['Date'], weather_data['Humidity (%)'], marker='s', label="Humidity (%)", color='blue')

plt.xlabel("Date")
plt.ylabel("Values")
plt.title("Weather Data Visualization")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

plt.show()


# In[ ]:




