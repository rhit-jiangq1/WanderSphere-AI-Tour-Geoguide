import pandas as pd

file_path = 'flickr_photo_data.xlsx'
data = pd.ExcelFile(file_path)

df = data.parse('Flickr Photo Data')

df['Views'] = pd.to_numeric(df['Views'], errors='coerce').fillna(0)
df['Sentiment Score'] = pd.to_numeric(df['Sentiment Score'], errors='coerce').fillna(0)
df['Tags'] = df['Tags'].fillna('')

def calculate_ranking_score(row):
    view_score = row['Views']
    tag_score = len(row['Tags'].split(','))
    sentiment_score = row['Sentiment Score']
    return view_score + tag_score + sentiment_score

df['Ranking Score'] = df.apply(calculate_ranking_score, axis=1)

df_sorted = df.sort_values(by='Ranking Score', ascending=False)

top_10_images = df_sorted.head(10)[['Place Name', 'Image URL']]

top_10_images['Google Maps Link'] = top_10_images['Place Name'].apply(
    lambda name: f"https://www.google.com/maps/search/{name.replace(' ', '+')}"
)

top_10_images.reset_index(drop=True, inplace=True)
print(top_10_images)
