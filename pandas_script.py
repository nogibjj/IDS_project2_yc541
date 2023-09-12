import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df_spotify = pd.read_csv("spotify-2023.csv", encoding="ISO-8859-1")

# Generate summary statistics for numeric columns
summary_statistics = df_spotify.describe().transpose()[['mean', '50%', 'std']]
summary_statistics.columns = ['Mean', 'Median', 'Standard Deviation']

# Handle non-numeric values in 'streams' column and convert it to integer type
df_spotify = df_spotify[df_spotify['streams'].astype(str).str.isnumeric()]
df_spotify['streams'] = df_spotify['streams'].astype(int)

# Data visualization: Top 10 songs by streams
sns.set_style("whitegrid")
top_10_songs = df_spotify.nlargest(10, 'streams')
plt.figure(figsize=(12, 8))
sns.barplot(data=top_10_songs, y='track_name', x='streams', hue='artist(s)_name', dodge=False, palette='muted')
plt.title('Top 10 Songs by Streams in Spotify 2023')
plt.xlabel('Number of Streams (in billions)')
plt.ylabel('Track Name')
plt.legend(title='Artist(s)', loc='lower right')
plt.tight_layout()
plt.savefig("top_10_songs_by_streams.png")
plt.show()
