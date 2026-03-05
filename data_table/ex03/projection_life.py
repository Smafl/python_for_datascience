from load_csv import load
import sys
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def format_x_label(x, pos):
    return f"{int(x / 1000)}K"


def main():
    """
    Load the life expectancy dataset and income per person dataset
    and displays the projection of life expectancy in relation to
    the gross national product of the year 1900 for each country.
    """
    income_dataset = load(
        "data_table/ex03/"
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    life_expectancy_dataset = load("data_table/ex03/life_expectancy_years.csv")
    if income_dataset is None or life_expectancy_dataset is None:
        sys.exit("Failed to load dataset.")

    income_row = income_dataset["1900"]
    life_expectancy_row = life_expectancy_dataset["1900"]
    if income_row.empty or life_expectancy_row.empty:
        sys.exit("Data not found.")

    fig, ax = plt.subplots()
    ax.scatter(income_row, life_expectancy_row)
    # ax.legend()
    ax.set_xlabel("Gross domestic product")
    ax.set_ylabel("Life expectancy")
    ax.set_title("1900")
    ax.xaxis.set_major_formatter(FuncFormatter(format_x_label))
    plt.show()


if __name__ == "__main__":
    main()
