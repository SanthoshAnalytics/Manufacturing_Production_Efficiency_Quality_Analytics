import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("default")
sns.set_theme(style="whitegrid")


def plot_histogram(df, column):
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], kde=True)

    plt.title(f"{column} Distribution")
    plt.xlabel(column)
    plt.ylabel("Frequency")

    plt.show()


def plot_boxplot(df, column):
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df[column])

    plt.title(f"{column} Box Plot")

    plt.show()


def correlation_heatmap(df):

    plt.figure(figsize=(12, 8))

    sns.heatmap(
        df.corr(numeric_only=True),
        annot=True,
        cmap="Blues",
        fmt=".2f"
    )

    plt.title("Correlation Heatmap")

    plt.show()
    
