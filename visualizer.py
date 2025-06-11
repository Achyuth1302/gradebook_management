import matplotlib.pyplot as plt
import seaborn as sns

def plot_grade_distribution(merged_df, output_path):
    plt.figure(figsize=(8, 5))
    sns.countplot(data=merged_df, x='letter_grade', palette='pastel', order=['A', 'B', 'C', 'D', 'F'])
    plt.title('Distribution of Letter Grades')
    plt.xlabel('Letter Grade')
    plt.ylabel('Number of Students')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
