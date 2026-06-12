import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv(r"Data/cleaned_covid_data.csv")


def plot_top_cases():
    top10 = df.sort_values(
        by="Cases",
        ascending=False
    ).head(10)

    plt.figure(figsize=(12, 6))

    plt.bar(
        top10["Country"],
        top10["Cases"]
    )

    plt.title("Top 10 Countries by COVID Cases")
    plt.xlabel("Country")
    plt.ylabel("Cases")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def plot_top_deaths():
    top10 = df.sort_values(
        by="Deaths",
        ascending=False
    ).head(10)

    plt.figure(figsize=(12, 6))

    plt.bar(
        top10["Country"],
        top10["Deaths"]
    )

    plt.title("Top 10 Countries by COVID Deaths")
    plt.xlabel("Country")
    plt.ylabel("Deaths")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def plot_top_death_rate():
    top10 = df.sort_values(
        by="Death_Rate",
        ascending=False
    ).head(10)

    plt.figure(figsize=(12, 6))

    plt.bar(
        top10["Country"],
        top10["Death_Rate"]
    )

    plt.title("Top 10 Countries by Death Rate")
    plt.xlabel("Country")
    plt.ylabel("Death Rate (%)")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def plot_top_recovery_rate():
    top10 = df.sort_values(
        by="Recovery_Rate",
        ascending=False
    ).head(10)

    plt.figure(figsize=(12, 6))

    plt.bar(
        top10["Country"],
        top10["Recovery_Rate"]
    )

    plt.title("Top 10 Countries by Recovery Rate")
    plt.xlabel("Country")
    plt.ylabel("Recovery Rate (%)")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def plot_cases_vs_deaths():
    plt.figure(figsize=(10, 6))

    plt.scatter(
        df["Cases"],
        df["Deaths"]
    )

    plt.title("Cases vs Deaths")
    plt.xlabel("Cases")
    plt.ylabel("Deaths")

    plt.tight_layout()
    plt.show()


def plot_risk_distribution():
    risk_counts = df["Risk_Level"].value_counts()

    plt.figure(figsize=(8, 8))

    plt.pie(
        risk_counts,
        labels=risk_counts.index,
        autopct="%1.1f%%"
    )

    plt.title("COVID Risk Distribution")
    plt.show()


if __name__ == "__main__":

    while True:

        print("\n" + "=" * 50)
        print("COVID-19 DATA ANALYZER")
        print("=" * 50)

        print("1. Top 10 Countries by Cases")
        print("2. Top 10 Countries by Deaths")
        print("3. Top 10 Countries by Death Rate")
        print("4. Top 10 Countries by Recovery Rate")
        print("5. Cases vs Deaths Scatter Plot")
        print("6. Risk Distribution Pie Chart")
        print("7. Exit")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            plot_top_cases()

        elif choice == "2":
            plot_top_deaths()

        elif choice == "3":
            plot_top_death_rate()

        elif choice == "4":
            plot_top_recovery_rate()

        elif choice == "5":
            plot_cases_vs_deaths()

        elif choice == "6":
            plot_risk_distribution()

        elif choice == "7":
            print("Exiting Program...")
            break

        else:
            print("❌ Invalid Choice")