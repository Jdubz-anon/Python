from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

die_1 = Die(8)
die_2 = Die(8)
results = []

for i in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
#print(results)

max_result = die_1.num_sides + die_2.num_sides
frequencies = []
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
#print(frequencies)

#visualize results

x_values = list(range(2,max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Results'}
my_layout = Layout(title='Results of rolling 2 D8 1000 times', xaxis=x_axis_config,
                   yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='2_d8.html')

