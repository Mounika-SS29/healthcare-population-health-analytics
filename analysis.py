import pandas as pd

df = pd.read_csv("diabetes_state_burden.csv")

print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

print("\nUnique States:")
print(df["Location"].nunique())

print("\nYears Available:")
print(sorted(df["Year"].unique())[:10])

print("\nIndicators:")
print(df["Short Indicator Text"].nunique())

print("\nIndicators List:")
print(df["Short Indicator Text"].unique())

diabetes_df = df[df["Short Indicator Text"] == "Diabetes Prevalence"]

print("\nDiabetes Records:")
print(diabetes_df.shape)

print("\nTop 5 Diabetes Records:")
print(diabetes_df.head())


latest = diabetes_df[diabetes_df["Year"] == 2021].copy()


latest["Data Value"] = pd.to_numeric(
    latest["Data Value"],
    errors="coerce"
)


latest = latest.dropna(subset=["Data Value"])


top_states = (
    latest.groupby("Location")["Data Value"]
    .mean()
    .sort_values(ascending=False)
)

print("\nTop 10 States by Diabetes Prevalence (2021):")
print(top_states.head(10))

print("\nData Types:")
print(df.dtypes)

print("\nData Type Values:")
print(df["Data Type"].value_counts().head(20))

diabetes_clean = df[
    (df["Short Indicator Text"] == "Diabetes Prevalence") &
    (df["Data Type"] == "Age-adjusted Rate (per 100)")
]

diabetes_clean["Data Value"] = pd.to_numeric(
    diabetes_clean["Data Value"],
    errors="coerce"
)

print("\nClean Diabetes Dataset:")
print(diabetes_clean.shape)

print("\nTop 10 States by Diabetes Prevalence:")

print(
    diabetes_clean.groupby("Location")["Data Value"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)



import matplotlib.pyplot as plt

top10 = (
    diabetes_clean.groupby("Location")["Data Value"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
top10.plot(kind="bar")

plt.title("Top 10 States by Diabetes Prevalence")
plt.xlabel("State")
plt.ylabel("Diabetes Prevalence (%)")

plt.tight_layout()

plt.savefig("top10_diabetes_states.png")

print("\nChart saved as top10_diabetes_states.png")