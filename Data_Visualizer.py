import seaborn as sns, matplotlib.pyplot as plt, numpy as np
import numpy as np
 
employees = np.array([
    "You (CEO)", "Employee 1", "Employee 2", "Employee 3", "Employee 4",
    "Employee 5", "Employee 6", "Employee 7", "Employee 8", "Employee 9", "Total"
])
 
titles = np.array([
    "CEO", "CFO", "COO", "VP", "Manager", "Project Lead",
    "Sales Associate", "Sales Associate", "Assistant", "Intern", ""
])
title_colors = {
    "CEO": "red",
    "CFO": "blue",
    "COO": "green",
    "VP": "purple",
    "Manager": "orange",
    "Project Lead": "cyan",
    "Sales Associate": "magenta",
    "Assistant": "yellow",
    "Intern": "gray",
    "": "black",  # For 'Total' or empty
}
salaries = np.array([150, 125, 125, 100, 100, 100, 95, 95, 75, 70, 0])
MeanSalary = np.mean(salaries).round()
ModeSalary = np.argmax(np.bincount(salaries)).round() # most common number in the array
MedianSalary = np.median(salaries).round()

# Create subplots: dotplot, histogram, boxplot, stemplot
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Dotplot (stripplot)
sns.stripplot(x=salaries, ax=axs[0,0], color='blue', size=8)
axs[0,0].set_title('Salary Distribution within Dotplot at David\'s Care')
axs[0,0].set_xlabel('Salary (thousands)')

# Histogram
axs[0,1].hist(salaries, bins=8, color='green', edgecolor='black')
axs[0,1].set_title('Salary Distribution within Histogram at David\'s Care')
axs[0,1].set_xlabel('Salary (thousands)')
axs[0,1].set_ylabel('Frequency')

# Boxplot
sns.boxplot(x=salaries, ax=axs[1,0], color='orange')
axs[1,0].set_title('Salary Distribution within Boxplot at David\'s Care')
axs[1,0].set_xlabel('Salary (thousands)')

# Stemplot
axs[1,1].stem(range(len(salaries)), salaries)
axs[1,1].set_title('Salary Distribution within Stem Plot at David\'s Care')
axs[1,1].set_xlabel('Employee Index')
axs[1,1].set_ylabel('Salary (thousands)')

plt.tight_layout()
plt.savefig('salary_plots.png')
print(MeanSalary, ModeSalary, MedianSalary)
print('Plots saved as salary_plots.png')
