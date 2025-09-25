import pandas as pd

df = pd.read_csv("Most Streamed Spotify Songs 2024.csv", encoding="latin1")

keep_cols = [
    "Track", "Artist", "Album Name", "Release Date",
    "Spotify Streams", "Spotify Popularity",
    "YouTube Views", "TikTok Likes", "Shazam Counts", "Explicit"
]
df = df[[c for c in keep_cols if c in df.columns]].copy()

df.columns = [c.strip().replace(" ", "_") for c in df.columns]

if "Release_Date" in df.columns:
    df["Release_Date"] = pd.to_datetime(df["Release_Date"], errors="coerce")

for col in df.select_dtypes(include=["float64", "int64"]).columns:
    df[col] = df[col].fillna(0)

df = df.fillna("Unknown")

if {"Track", "Artist"}.issubset(df.columns):
    df = df.drop_duplicates(subset=["Track", "Artist"])

df.to_csv("spotify_clean.csv", index=False)
df.to_excel("spotify_clean.xlsx", index=False)
