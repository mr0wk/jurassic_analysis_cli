import matplotlib.pyplot as plt


def bar_plot_diet(df):
    plt.figure(figsize=(10, 6))
    df["diet"].value_counts().plot(kind="bar")
    plt.title("Number of Dinosaurs by Diet")
    plt.xlabel("Diet")
    plt.ylabel("Count")
    plt.show()


def bar_plot_period(df):
    plt.figure(figsize=(10, 6))
    df["period"].value_counts().plot(kind="bar")
    plt.title("Number of Dinosaurs by Period")
    plt.xlabel("Period")
    plt.ylabel("Count")
    plt.show()


def scatter_plot_length(df):
    plt.figure(figsize=(10, 6))
    for diet in df["diet"].unique():
        subset = df[df["diet"] == diet]
        plt.scatter(subset["type"], subset["length"], label=diet)
    plt.title("Length of Dinosaurs by Type and Diet")
    plt.xlabel("Type")
    plt.ylabel("Length")
    plt.legend()
    plt.show()


def histogram_dinosaur_lengths(df):
    plt.figure(figsize=(10, 6))
    df["length"].plot(kind="hist", bins=20)
    plt.title("Distribution of Dinosaur Lengths")
    plt.xlabel("Length")
    plt.ylabel("Frequency")
    plt.show()


def pie_chart_country_lived_in(df):
    plt.figure(figsize=(10, 6))
    df["lived_in"].value_counts().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Dinosaurs by Country Lived In")
    plt.ylabel("")  # Hide the y-label
    plt.show()
