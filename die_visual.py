from die import Die
import plotly.express as px

# Create a D6.
die1 = Die()
die2 = Die()

# Make some rolls, ad store results in a list.
results = []
for roll_num in range(100):
    result = die1.roll() + die2.roll()
    results.append(result)  

# Analyze the results.
frequencies = []
max_result = die1.num_sides + die2.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visual the results.
title = "Result of Rolling Two D6 1,000 Times"
labels = { 'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis=dict(dtick=1))

fig.show()

print(frequencies)