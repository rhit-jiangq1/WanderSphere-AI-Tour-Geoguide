import pandas as pd

# Load the Excel file
file_path = 'path_to_your_file/flickr_photo_data.xlsx'
data = pd.ExcelFile(file_path)

# Load the main sheet
df = data.parse('Flickr Photo Data')

# Fill missing values in relevant columns for processing
df['Views'] = pd.to_numeric(df['Views'], errors='coerce').fillna(0)
df['Sentiment Score'] = pd.to_numeric(df['Sentiment Score'], errors='coerce').fillna(0)
df['Tags'] = df['Tags'].fillna('')

# Define a function to calculate ranking score
def calculate_ranking_score(row):
    # Scoring based on Views, Tag count, and Sentiment Score
    view_score = row['Views']
    tag_score = len(row['Tags'].split(','))
    sentiment_score = row['Sentiment Score']
    # Equal weights for each parameter
    return view_score + tag_score + sentiment_score

# Apply the ranking score calculation
df['Ranking Score'] = df.apply(calculate_ranking_score, axis=1)

# Sort by the ranking score in descending order
df_sorted = df.sort_values(by='Ranking Score', ascending=False)

# Select the top 10 images
top_10_images = df_sorted.head(10)[['Place Name', 'Image URL']]

# Generate Google Maps links for each Place Name
top_10_images['Google Maps Link'] = top_10_images['Place Name'].apply(
    lambda name: f"https://www.google.com/maps/search/{name.replace(' ', '+')}"
)

# Reset index and display result
top_10_images.reset_index(drop=True, inplace=True)
print(top_10_images)
