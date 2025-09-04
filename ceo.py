import seaborn as sns, matplotlib.pyplot as plt, numpy as np
import stemgraphic as stem

employees = np.array([
    "You (CEO)", "Employee 1", "Employee 2", "Employee 3", "Employee 4",
    "Employee 5", "Employee 6", "Employee 7", "Employee 8", "Employee 9", "Total"
])
 
titles = np.array([
    "CEO", "CFO", "COO", "VP", "Manager", "Project Lead",
    "Sales Associate", "Sales Associate", "Assistant", "Intern"
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
}
salaries = np.array([150,125,115,90,90,90,90,85,85,80])


MeanSalary = np.mean(salaries).round()
ModeSalary = np.argmax(np.bincount(salaries)).round()
MedianSalary = np.median(salaries).round()

# dotplot (stripplot)
plt.figure(figsize=(7, 5))
for i, (salary, title) in enumerate(zip(salaries, titles)):
    # to prevent overlapping
    count = list(salaries[:i+1]).count(salary)
    plt.scatter(salary, count, color=title_colors[str(title)],
                label=str(title) if title and str(title) not in plt.gca().get_legend_handles_labels()[1] else "", s=200) # s parameter for point size
plt.yticks([])
handles, labels = plt.gca().get_legend_handles_labels()
if labels:
    plt.legend(handles, [l for l in labels if l], title="Employee Title", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title("Salary Distribution within Dotplot at David's Care")
plt.xlabel('Salary (in thousands)')
plt.tight_layout()
plt.savefig('plots/salary_dotplot.png')
plt.close()


unique, counts = np.unique(salaries, return_counts=True)
frequency_table = dict(zip(unique, counts))
relative_frequencies = counts / counts.sum()

# plotting both histogram and frequency table
fig, (ax_hist, ax_table) = plt.subplots(2, 1, figsize=(7, 8), gridspec_kw={'height_ratios': [3, 1]})
ax_hist.hist(salaries, bins=15, color='green', edgecolor='black')
ax_hist.set_title("Salary Distribution & Frequency Table at David's Care")
ax_hist.set_xlabel('Salary (in thousands)')
ax_hist.set_ylabel('Frequency')

table_data = [[str(sal), str(freq), f"{rel:.2%}"] for sal, freq, rel in zip(unique, counts, relative_frequencies)]
ax_table.axis('off')
table = ax_table.table(cellText=table_data,
                      colLabels=["Salary", "Frequency", "Relative Frequency"],
                      cellLoc='center',
                      loc='center')
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1, 2)

plt.tight_layout()
plt.savefig('plots/salary_histogram_with_table.png')
plt.close()
    
# boxplot
plt.figure(figsize=(7, 5))
sns.boxplot(x=salaries, color='blue', flierprops=dict(markerfacecolor='red', marker='o')) # flierprops to highlight outliers 
plt.title("Salary Distribution within Boxplot at David's Care")
plt.xlabel('Salary (in thousands)')
plt.tight_layout()
plt.savefig('plots/salary_boxplot.png')
plt.close()

# stemplot
fig, ax = stem.stem_graphic(salaries, aggregation=False) # markerfmt to change marker color and style, basefmt to remove baseline
plt.title("Salary Distribution within Stem Plot at David's Care")
plt.xlabel('Employee Index')
plt.ylabel('Salary (in thousands)')
plt.savefig('plots/salary_stemplot.png', bbox_inches='tight') 
plt.close()

# plt.savefig is to save plot as img
print('Plots saved as images')
print(f"Mean Salary: ${MeanSalary * 1000}, Mode Salary: ${ModeSalary * 1000}, Median Salary: ${MedianSalary * 1000}")
