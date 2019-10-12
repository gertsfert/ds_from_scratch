# %% [markdown]
# # Basic Plotting
# *Chapter 3 - Visulizing Data*

from matplotlib import pyplot as plt
from collections import Counter

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# %%
# ## Creating a line chart
# Line charts are good for showing continous change of
# a single dimension.
# In this instance a plot with years on x-axis,
# gdp on y-axis
plt.plot(years, gdp, color='green', marker='o',
         linestyle='solid')

# adding a title and labels
plt.title("Nominal GDP")
plt.ylabel("Billions of $")
plt.show()


# %% [markdown]
# ## Creating a barchart
# Barcharts are good when showing quantity variations
# across a set of discrete items

movies = [
    "Annie Hall",
    "Ben-Hur",
    "Casablanca",
    "Gandhi",
    "West Side Story"]

num_oscars = [5, 11, 3, 8, 10]

# plot bars with left x-coordinates
plt.bar(range(len(movies)), num_oscars)

plt.title("My Favourite Movies")
plt.ylabel("# of academy awards")

# labelling x axis with movie names
plt.xticks(range(len(movies)), movies)

plt.show()

# %% [markdown]
# ## Distribution Plotting
# Barcharts are also a good choice to display how
# values are distributed within data.

grades = [83, 95, 91, 87, 70, 0, 85,
          82, 100, 67, 73, 77, 0]

# bucket grades by decile, but put 100 in with the 90s
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.bar([
    x + 5 for x in histogram.keys()],   # shift bars to right by 5
    histogram.values(),                 # set height
    10,                                 # set width
    edgecolor=(0, 0, 0))                # set boundary colour

plt.axis([-5, 105, 0, 5])  # x axis from -5 to 105, y from 0 to 5

plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# students")
plt.title("Distrbution of Exam 1 grades")
plt.show()


# %% [markdown]
# ## Line Charts for showing Trends
varience = [2**n for n in range(9)]
bias_squared = [2**n for n in range(8, -1, -1)]
total_error = [x + y for x, y in zip(varience, bias_squared)]
xs = [i for i, _ in enumerate(varience)]

# Can make multiple calls to plt.plot to show multiple
# series in the same chart
plt.plot(xs, varience, 'g-', label='varience')  # green solid line
plt.plot(xs, bias_squared, 'r-.', label='bias^2')  # red dot-dash line
plt.plot(xs, total_error, 'y:', label='total error')  # white dotted line

# as labels have beenm assigned to each series
# we can get a legend for free
plt.legend(loc=9)  # put legend in top-centre
plt.xlabel("model complexity")
plt.xticks([])
plt.title("The bias-variance tradeoff")

plt.show()
# %% [markdown]
# ## Scatter plots
# Scatter plots are good for showing how two data sets are related

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

# label each point
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy=(friend_count, minute_count),
                 xytext=(5, -5),
                 textcoords='offset points')

plt.title("Daily minutes vs Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("Daily minutes spent on the site")
plt.show()

# %%
