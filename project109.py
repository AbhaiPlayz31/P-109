import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics 
import plotly.graph_objects as go
import pandas as pd 

df = pd.read_csv('project109.csv')
data = df['reading score'].tolist()


mean = sum(data)/len(data)
median = statistics.median(data)
mode = statistics.mode(data)
std = statistics.stdev(data)

print('Mean is:', mean)
print('Median is:', median)
print('Mode is:', mode)
print('STD:', std)

firststdStart, firststdEnd = mean-std,mean+std
list_of_data_within_1_std=[result for result in data if result > firststdStart and result < firststdEnd]
print('{}% of data lies within 1 or more std'.format(len(list_of_data_within_1_std)*100/len(data)))

secondstdStart, secondstdEnd = mean-(2*std),mean+(2*std)
list_of_data_within_2_std=[result for result in data if result > secondstdStart and result < secondstdEnd]
print('{}% of data lies within 2 or more std'.format(len(list_of_data_within_2_std)*100/len(data)))

thirdstdStart, thirdstdEnd = mean-(3*std),mean+(3*std)
list_of_data_within_3_std=[result for result in data if result > thirdstdStart and result < thirdstdEnd]
print('{}% of data lies within 3 or more std'.format(len(list_of_data_within_3_std)*100/len(data)))

fig = ff.create_distplot([data], ["Reading Score"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.17], mode = 'lines', name = 'mean'))

fig.add_trace(go.Scatter(x=[firststdStart,firststdStart], y = [0, 0.17], mode = 'lines', name = 'firststdStart'))
fig.add_trace(go.Scatter(x=[firststdEnd,firststdEnd], y = [0, 0.17], mode = 'lines', name = 'firststdEnd'))

fig.add_trace(go.Scatter(x=[secondstdStart,secondstdStart], y = [0, 0.17], mode = 'lines', name = 'secondstdStart'))
fig.add_trace(go.Scatter(x=[secondstdEnd,secondstdEnd], y = [0, 0.17], mode = 'lines', name = 'secondstdEnd'))

fig.add_trace(go.Scatter(x=[thirdstdStart,thirdstdStart], y = [0, 0.17], mode = 'lines', name = 'thirdstdStart'))
fig.add_trace(go.Scatter(x=[thirdstdEnd,thirdstdEnd], y = [0, 0.17], mode = 'lines', name = 'thirdstdEnd'))

fig.show()


