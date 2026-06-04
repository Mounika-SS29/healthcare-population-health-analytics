import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    """Load CDC dataset"""
    df = pd.read_csv("diabetes_state_burden.csv")
    return df


def explore_data(df):

    print("Dataset Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns)

    print("\nUnique States:")
    print(df["Location"].nunique())

    print("\nYears Available:")
    print(sorted(df["Year"].unique()))

    print("\nIndicators:")
    print(df["Short Indicator Text"].nunique())


def clean_diabetes_data(df):

    diabetes_clean = df[
        (df["Short Indicator Text"] == "Diabetes Prevalence")
        & (df["Data Type"] == "Age-adjusted Rate (per 100)")
    ].copy()

    diabetes_clean["Data Value"] = pd.to_numeric(
        diabetes_clean["Data Value"],
        errors="coerce"
    )

    diabetes_clean = diabetes_clean.dropna(
        subset=["Data Value"]
    )

    return diabetes_clean


def analyze_top_states(diabetes_clean):

    top10 = (
        diabetes_clean.groupby("Location")["Data Value"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    print("\nTop 10 States:")
    print(top10)

    return top10


def create_top10_chart(top10):

    plt.figure(figsize=(10, 6))

    ax = top10.plot(
        kind="bar",
        color="grey"
    )

    plt.title("Top 10 States by Diabetes Prevalence")

    plt.xlabel("State")

    plt.ylabel("Diabetes Prevalence (%)")

    for p in ax.patches:

        ax.annotate(
            f"{p.get_height():.1f}",
            (
                p.get_x() + p.get_width() / 2,
                p.get_height()
            ),
            ha="center",
            va="bottom"
        )

    plt.tight_layout()

    plt.savefig("top10_diabetes_states.png")

    print("\nTop 10 chart saved successfully")


def create_bottom10_chart(diabetes_clean):

    bottom10 = (
        diabetes_clean.groupby("Location")["Data Value"]
        .mean()
        .sort_values()
        .head(10)
    )

    print("\nBottom 10 States:")
    print(bottom10)

    plt.figure(figsize=(10, 6))

    ax = bottom10.plot(
        kind="barh",
        color="royalblue"
    )

    plt.title("Bottom 10 States by Diabetes Prevalence")

    plt.xlabel("Diabetes Prevalence (%)")

    plt.ylabel("State")

    for p in ax.patches:

        ax.annotate(
            f"{p.get_width():.1f}",
            (
                p.get_width(),
                p.get_y() + p.get_height() / 2
            ),
            ha="left",
            va="center"
        )

    plt.tight_layout()

    plt.savefig("bottom10_diabetes_states.png")

    print("\nBottom 10 chart saved successfully")


def create_histogram(diabetes_clean):

    mean_val = diabetes_clean["Data Value"].mean()

    median_val = diabetes_clean["Data Value"].median()

    plt.figure(figsize=(10, 6))

    plt.hist(
        diabetes_clean["Data Value"],
        bins=15,
        color="darkorange",
        edgecolor="black"
    )

    plt.axvline(
        mean_val,
        color="red",
        linestyle="--",
        linewidth=2,
        label=f"Mean = {mean_val:.2f}"
    )

    plt.axvline(
        median_val,
        color="blue",
        linestyle="--",
        linewidth=2,
        label=f"Median = {median_val:.2f}"
    )

    plt.title("Distribution of Diabetes Prevalence")

    plt.xlabel("Diabetes Prevalence (%)")

    plt.ylabel("Frequency")

    plt.legend()

    plt.text(
        12.5,
        18,
        f"Min: {diabetes_clean['Data Value'].min():.1f}\n"
        f"Max: {diabetes_clean['Data Value'].max():.1f}",
        bbox=dict(facecolor="white")
    )

    plt.tight_layout()

    plt.savefig("diabetes_distribution.png")

    print("\nHistogram saved successfully")


def create_risk_category_chart(diabetes_clean):

    state_avg = (
        diabetes_clean.groupby("Location")["Data Value"]
        .mean()
    )

    high = (state_avg > 12).sum()

    medium = (
        (state_avg >= 9)
        & (state_avg <= 12)
    ).sum()

    low = (state_avg < 9).sum()

    categories = [
        "High Risk",
        "Medium Risk",
        "Low Risk"
    ]

    counts = [
        high,
        medium,
        low
    ]

    colors = [
        "crimson",
        "orange",
        "forestgreen"
    ]

    print("\nRisk Categories:")
    print(f"High Risk States: {high}")
    print(f"Medium Risk States: {medium}")
    print(f"Low Risk States: {low}")

    plt.figure(figsize=(8, 8))

    plt.pie(
        counts,
        labels=categories,
        colors=colors,
        autopct="%1.1f%%"
    )

    plt.title("State Diabetes Risk Categories")

    plt.savefig("risk_categories.png")

    print("\nRisk category chart saved successfully")


def create_summary_chart(diabetes_clean):

    mean_val = diabetes_clean["Data Value"].mean()
    median_val = diabetes_clean["Data Value"].median()
    max_val = diabetes_clean["Data Value"].max()
    min_val = diabetes_clean["Data Value"].min()
    std_val = diabetes_clean["Data Value"].std()

    print("\n========== SUMMARY STATISTICS ==========")
    print(f"Mean Diabetes Prevalence: {mean_val:.2f}")
    print(f"Median Diabetes Prevalence: {median_val:.2f}")
    print(f"Maximum Diabetes Prevalence: {max_val:.2f}")
    print(f"Minimum Diabetes Prevalence: {min_val:.2f}")
    print(f"Standard Deviation: {std_val:.2f}")

    labels = [
        "Mean",
        "Median",
        "Maximum",
        "Minimum",
        "Std Dev"
    ]

    values = [
        mean_val,
        median_val,
        max_val,
        min_val,
        std_val
    ]

    colors = [
        "royalblue",
        "orange",
        "crimson",
        "forestgreen",
        "purple"
    ]

    plt.figure(figsize=(10, 6))

    bars = plt.bar(
        labels,
        values,
        color=colors
    )

    plt.title("Diabetes Summary Statistics")

    plt.ylabel("Value")

    for bar in bars:

        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.15,
            f"{height:.2f}",
            ha="center",
            fontweight="bold"
        )

    plt.tight_layout()

    plt.savefig("summary_statistics.png")

    print("\nSummary statistics chart saved successfully")


def export_state_rankings(diabetes_clean):

    rankings = (
        diabetes_clean.groupby("Location")["Data Value"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    rankings.columns = [
        "State",
        "Average Diabetes Prevalence"
    ]

    rankings.to_csv(
        "state_diabetes_rankings.csv",
        index=False
    )

    print("\nState rankings CSV exported successfully")

def main():

    df = load_data()

    explore_data(df)

    diabetes_clean = clean_diabetes_data(df)

    top10 = analyze_top_states(diabetes_clean)

    create_top10_chart(top10)

    create_bottom10_chart(diabetes_clean)

    create_histogram(diabetes_clean)

    create_risk_category_chart(diabetes_clean)

    create_summary_chart(diabetes_clean)

    export_state_rankings(diabetes_clean)


if __name__ == "__main__":
    main()