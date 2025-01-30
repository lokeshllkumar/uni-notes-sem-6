import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# to generate 10000 random values of a Gaussian distribution and verify if it fits the distribution

mean, std = 0, 1
normal_dist_vals = np.random.normal(mean, std, 10000)

plt.figure(figsize = (10, 5))
plt.hist(normal_dist_vals, bins = 50, density = True, alpha = 0.6, color = 'b', label = "Histogram")

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, mean, std)
plt.plot(x, p, 'k', linewidth = 2, label = "Normal PDF")

plt.title("Histogram of Generated Data with Normal PDF")
plt.legend()
plt.show()