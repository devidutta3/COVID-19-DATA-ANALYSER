import pandas as pd

# Load Dataset
df = pd.read_csv(r"Data/covid_data.csv")

print("=" * 50)
print("FIRST 5 ROWS")
print(df.head())

print("=" * 50)
print("DATASET INFORMATION")
print(df.info())

print("=" * 50)
print("STATISTICAL SUMMARY")
print(df.describe())

# -------------------------
# Top 10 Countries by Cases
# -------------------------

print("=" * 50)
print("TOP 10 COUNTRIES BY CASES")

top_cases = df.sort_values(
    by="Cases",
    ascending=False
)

print(
    top_cases[
        ["Country", "Cases", "Deaths", "ReCovered"]
    ].head(10)
)

# -------------------------
# Top 10 Countries by Deaths
# -------------------------

print("=" * 50)
print("TOP 10 COUNTRIES BY DEATHS")

top_deaths = df.sort_values(
    by="Deaths",
    ascending=False
)

print(
    top_deaths[
        ["Country", "Cases", "Deaths", "ReCovered"]
    ].head(10)
)

# -------------------------
# Feature Engineering
# -------------------------

df["Death_Rate"] = (
    df["Deaths"] /
    df["Cases"].replace(0, pd.NA)
) * 100

df["Recovery_Rate"] = (
    df["ReCovered"] /
    df["Cases"].replace(0, pd.NA)
) * 100

# -------------------------
# Top Death Rate Countries
# -------------------------

print("=" * 50)
print("TOP 10 COUNTRIES BY DEATH RATE")

top_death_rate = df.sort_values(
    by="Death_Rate",
    ascending=False
)

print(
    top_death_rate[
        ["Country", "Death_Rate"]
    ].head(10)
)

# -------------------------
# Top Recovery Rate Countries
# -------------------------

print("=" * 50)
print("TOP 10 COUNTRIES BY RECOVERY RATE")

top_recovery = df.sort_values(
    by="Recovery_Rate",
    ascending=False
)

print(
    top_recovery[
        ["Country", "Recovery_Rate"]
    ].head(10)
)

# -------------------------
# Risk Classification
# -------------------------

def risk_level(rate):
    if rate > 5:
        return "High Risk"
    elif rate > 2:
        return "Medium Risk"
    else:
        return "Low Risk"


df["Risk_Level"] = df["Death_Rate"].apply(risk_level)

print("=" * 50)
print("RISK LEVEL DISTRIBUTION")

print(
    df["Risk_Level"].value_counts()
)

# -------------------------
# Save Cleaned Dataset
# -------------------------

df.to_csv(
    r"Data/cleaned_covid_data.csv",
    index=False
)

print("\n✅ Cleaned Dataset Saved Successfully")