import pandas as pd

df = pd.read_csv("students.csv")

df["Total"] = df["Python"] + df["Maths"] + df["AI"]
df["Average"] = df["Total"] / 3
df["Percentage"] = df["Average"]

df["Result"] = df["Percentage"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

df = df.sort_values("Percentage", ascending=False)

print(df)

print("\nHighest Scorer:")
print(df.iloc[0]["Name"])

print("\nSubject Averages:")
print("Python:", df["Python"].mean())
print("Maths:", df["Maths"].mean())
print("AI:", df["AI"].mean())