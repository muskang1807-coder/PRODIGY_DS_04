import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
file_path = r"C:\Users\MUSKAN\Downloads\twitter_training.csv"

# Read CSV
data = pd.read_csv(file_path, header=None)

# Give column names
data.columns = ["ID", "Topic", "Sentiment", "Tweet"]

# Display first 5 rows
print("========== FIRST 5 ROWS ==========")
print(data.head())

# Dataset information
print("\n========== DATASET INFO ==========")
print(data.info())

# Missing values
print("\n========== MISSING VALUES ==========")
print(data.isnull().sum())

# Statistical Summary
print("\n========== STATISTICAL SUMMARY ==========")
print(data.describe(include="all"))

# Sentiment Counts
print("\n========== SENTIMENT COUNTS ==========")
print(data["Sentiment"].value_counts())

# -------------------------------
# Bar Chart
# -------------------------------
plt.figure(figsize=(8,5))

data["Sentiment"].value_counts().plot(kind="bar")

plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Tweets")

plt.tight_layout()

plt.savefig("sentiment_distribution.png")

plt.show()

# -------------------------------
# Pie Chart
# -------------------------------
plt.figure(figsize=(6,6))

data["Sentiment"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")
plt.title("Sentiment Distribution")

plt.tight_layout()

plt.savefig("sentiment_pie.png")

plt.show()

print("\nTask 4 Completed Successfully!")