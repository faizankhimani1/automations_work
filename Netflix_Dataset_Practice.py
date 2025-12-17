import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

CSV_FILE = r"C:\Users\Faizan\Downloads\archive\netflix_titles.csv"
OUTPUT_FILE = r"C:\Users\Faizan\Downloads\archive\netflix_top20_recent.csv"

# Load dataset
df = pd.read_csv(CSV_FILE)

# Fix date_added
df['date_added'] = df['date_added'].astype(str).str.strip()
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Sort by recent added shows
df_sorted = df.sort_values(by='date_added', ascending=False)

# Take top 20 most recent shows
top20 = df_sorted.head(20)

# Select relevant columns
top20 = top20[['title', 'type', 'release_year', 'rating', 'duration', 'listed_in']]

# Save CSV
top20.to_csv(OUTPUT_FILE, index=False)
print(f"✅ Top 20 recent Netflix shows saved in '{OUTPUT_FILE}'")

# -----------------------------
# Graph 1: Horizontal Bar Chart for recent shows
plt.figure(figsize=(10,6))
sns.barplot(x='release_year', y='title', data=top20, palette="viridis")
plt.title("Top 20 Recent Netflix Shows by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Title")
plt.tight_layout()
plt.show()

# -----------------------------
# Graph 2: Top Genres Distribution
genres_series = top20['listed_in'].str.split(', ').explode()
top_genres = genres_series.value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_genres.values, y=top_genres.index, palette="magma")
plt.title("Top Genres among Top 20 Recent Shows")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.tight_layout()
plt.show()
