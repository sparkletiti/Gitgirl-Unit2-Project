#A Python script to calculate the profit based on revenue and expense data for ABD company

#Step1 is to import the Numpy, Pandas and Matplotlib packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#months of the year for which the revenue and expenses data are provided
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#revenue data, assume to be in US $
revenue = [145, 760, 861, 917, 805, 810, 114, 976, 103, 143, 107, 154]
#expenses data, assume to be in US dollars
expenses = [120, 569, 123, 120, 865, 840, 328, 582, 697, 166, 100, 380]

#convert the revenue and expenses into Numpy Arrays.
np_revenue =np.array(revenue)
np_expenses = np.array(expenses)

#Calculate the profit based on the revenue and expenses data.
np_profit = np_revenue - np_expenses
print('Profit for ABD Company from Jan to Dec is ' + str(np_profit))

#Script to extract data from month and profit into a dictionary to be named ‘Fin_status’
Fin_status= dict(zip(months, np_profit))
print('ABD Company Financial status per month is ' + str(Fin_status))

#Python script to convert the dictionary to a Pandas series
finstatus_pd = pd.Series(Fin_status, index= months)
print(finstatus_pd)

#matplotlib script to plot the months on the x axis and the profit on the y axis, label the x and y axes, provide a title for the plot
plt.xticks(np.arange(len(finstatus_pd.index)), finstatus_pd.index)
plt.xlabel('months')
plt.ylabel('Profit')
plt.title('Plot of Profit per month for ABD company')
finstatus_pd.plot()
plt.show()
