from IPython import display
import pandas as pd
from pprint import pprint
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
import praw
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from datetime import datetime
from dotenv import load_dotenv


sns.set(style='darkgrid', context='talk', palette='Dark2')

# Initialize Reddit API client
reddit =praw.Reddit('DEFAULT') 
# Fetch headlines and their creation times
headlines = set()
dates = []

for submission in reddit.subreddit('SecretNetwork').new(limit=None):
    headlines.add(submission.title)
    dates.append(datetime.utcfromtimestamp(submission.created_utc).date())
    display.clear_output()
print(f"Collected {len(headlines)} headlines")

# Perform sentiment analysis on the headlines
sia = SIA()
results = []

for line in headlines:
    pol_score = sia.polarity_scores(line)
    pol_score['headline'] = line
    results.append(pol_score)

# Create a DataFrame from the sentiment results
df = pd.DataFrame.from_records(results)

# Add date column to the DataFrame (ensure length matches)
df['date'] = dates[:len(df)]  # Slice dates to match the length of df

# Assign sentiment labels
df['label'] = 0
df.loc[df['compound'] > 0.05, 'label'] = 1
df.loc[df['compound'] < -0.05, 'label'] = -1

# Group by date and count sentiment occurrences
df['date'] = pd.to_datetime(df['date'])

# Save the data to CSV
df2 = df[['headline', 'label']]
sentiment_over_time = df.groupby('date')['label'].value_counts().unstack(fill_value=0).reset_index()
# Rename columns for clarity
sentiment_over_time.columns = ['date', 'negative', 'neutral', 'positive']

df2.to_csv('reddit_headlines_labels.csv', mode='a', encoding='utf-8', index=False)

# Visualize sentiment trends over time
plt.figure(figsize=(12, 6))
plt.plot(sentiment_over_time['date'], sentiment_over_time['positive'], label='Positive', color='green', marker='o')
plt.plot(sentiment_over_time['date'], sentiment_over_time['neutral'], label='Neutral', color='blue', marker='o')
plt.plot(sentiment_over_time['date'], sentiment_over_time['negative'], label='Negative', color='red', marker='o')
plt.title('Sentiment Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Headlines')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Display positive and negative headlines
print("Positive headlines:\n")
pprint(list(df[df['label'] == 1].headline)[:5], width=200)
print("\nNegative headlines:\n")
pprint(list(df[df['label'] == -1].headline)[:5], width=200)

# Print label counts and percentages
print(df.label.value_counts())
print(df.label.value_counts(normalize=True) * 100)

# Tokenize and analyze word frequencies for positive and negative headlines
stop_words = stopwords.words('english')
tokenizer = RegexpTokenizer(r'\w+')

def process_text(headlines):
    tokens = []
    for line in headlines:
        toks = tokenizer.tokenize(line)
        toks = [t.lower() for t in toks if t.lower() not in stop_words]
        tokens.extend(toks)
    
    return tokens

pos_lines = list(df[df.label == 1].headline)
pos_tokens = process_text(pos_lines)
pos_freq = nltk.FreqDist(pos_tokens)
pos_freq.most_common(20)

neg_lines = list(df[df.label == -1].headline)
neg_tokens = process_text(neg_lines)
neg_freq = nltk.FreqDist(neg_tokens)
neg_freq.most_common(20)

# Visualize word frequencies for positive and negative sentiments
pos_freq_data = pd.DataFrame(pos_freq.most_common(20), columns=['Word', 'Frequency'])
plt.figure(figsize=(10, 6))
sns.barplot(x='Frequency', y='Word', data=pos_freq_data, palette='Greens_d')
plt.title('Top Words in Positive Headlines')
plt.show()

neg_freq_data = pd.DataFrame(neg_freq.most_common(20), columns=['Word', 'Frequency'])
plt.figure(figsize=(10, 6))
sns.barplot(x='Frequency', y='Word', data=neg_freq_data, palette='Reds_d')
plt.title('Top Words in Negative Headlines')
plt.show()

# Distribution of compound sentiment scores
plt.figure(figsize=(10, 6))
sns.histplot(df['compound'], bins=30, kde=True, color='blue')
plt.title('Distribution of Compound Sentiment Scores')
plt.xlabel('Compound Score')
plt.ylabel('Frequency')
plt.show()
