import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load Dataset

file_path = 'employee_performance.csv'
df = pd.read_csv(file_path)
print(df.head())

# Distribution of Salary

sns.histplot(df['Salary'], kde=True, color='red')
plt.title('Distribution of Salary')
plt.show()

# Salary distribution by Department

sns.boxplot(x='Department', y='Salary', data=df, palette='Set1', hue='Department', legend=True)
plt.title('Salary Distribution by Department')
plt.show()

# Relationship between Experience and Performance Score

sns.scatterplot(x='Experience_Years', y='Performance_Score', data=df, hue='Department', palette='Set2')
plt.title('Relationship between Experience and Performance Score')
plt.show()

# Correlation Heatmap

corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()