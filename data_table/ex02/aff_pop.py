from load_csv import load
import sys
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def convert_to_millions(value):
    if value.endswith("M"):
        return float(value[:-1])
    elif value.endswith("B"):
        return float(value[:-1]) * 1000
    return float(value)


def format_y_label(x, pos):
    return f"{int(x)}M"


def main():
    """
    Load the population dataset and display the population in millions
    over time for two countries,
    provided as command-line arguments.
    """
    if (len(sys.argv) != 3):
        sys.exit("Usage: aff_pop.py <one country> <another country>")

    dataset = load("data_table/ex02/population_total.csv")
    if dataset is None:
        sys.exit("Failed to load dataset.")

    country1 = sys.argv[1]
    country2 = sys.argv[2]

    row_country1 = dataset[dataset["country"].str.lower() == country1.lower()]
    row_country2 = dataset[dataset["country"].str.lower() == country2.lower()]
    if row_country1.empty or row_country2.empty:
        print("Country not found.")
        countries = dataset["country"].tolist()
        print(f"Available countries:\n{countries}")
        sys.exit()

    years = dataset.columns[1:].astype(int)
    mask = (years >= 1800) & (years <= 2050)
    x = years[mask]

    y1 = row_country1.iloc[0, 1:].apply(convert_to_millions)[mask]
    y2 = row_country2.iloc[0, 1:].apply(convert_to_millions)[mask]

    fig, ax = plt.subplots()
    ax.plot(x, y1, label=country1)
    ax.plot(x, y2, label=country2)
    ax.legend()
    ax.set_xlabel("Year")
    ax.set_ylabel("Population")
    ax.set_title("Population Projections")
    ax.yaxis.set_major_formatter(FuncFormatter(format_y_label))
    plt.show()


if __name__ == "__main__":
    main()
