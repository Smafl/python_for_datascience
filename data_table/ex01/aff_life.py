from load_csv import load
import sys
import matplotlib.pyplot as plt


def main():
    """
    Load the life expectancy dataset and display the life expectancy
    over time for a given country provided as a command-line argument.
    """
    if (len(sys.argv) != 2):
        sys.exit("Usage: aff_life.py <Country>")

    dataset = load("data_table/ex00/life_expectancy_years.csv")
    if dataset is None:
        sys.exit("Failed to load dataset.")

    country = sys.argv[1]

    row = dataset[dataset["country"].str.lower() == country.lower()]
    if row.empty:
        print("Country not found.")
        countries = dataset["country"].tolist()
        print(f"Available countries:\n{countries}")
        sys.exit()

    years = dataset.columns[1:]
    x = years.astype(int)
    y = row.iloc[0, 1:]
    y = y.astype(float)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel("Year")
    ax.set_ylabel("Life expectancy")
    ax.set_title(f"{country} Life Expectancy Projections")
    plt.show()


if __name__ == "__main__":
    main()
