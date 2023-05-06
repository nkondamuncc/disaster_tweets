<img width="2534" alt="image" src="https://www.nj.gov/dep/parksandforests/fire/images/hero/emberawarenss-hero.jpg">

# Disaster Tweets
Twitter has become an important communication channel in times of emergency.

The ubiquitousness of smartphones enables people to announce an emergency they’re observing in real-time. Because of this, more agencies are interested in programatically monitoring Twitter (i.e. disaster relief organizations and news agencies).

**Streamlit app**: https://nkondamuncc-disaster-tweets-home-1dw46l.streamlit.app

The app is an attempt at analyzing disaster tweets against non disaster tweets and classifying a given tweet into one of these categories.

## Pages:

**Home**:
  - Introduction

**Tweet Detection**:
  - type in a tweet to check if it is about a disaster or otherwise

**Wordcloud**:
  - see what words are commonly used using the wordclouds for the whole data or each subset

**Top ngrams**:
  - see the frequencies of the most common unigrams, bigrams and trigras of each subset
  
  


## Data Preperation:

Text corpuses are semi-structured by nature. Data preperation involves converting it into structured format. Here are some steps followed:

1. **Data Cleaning**: Remove Links, Expand Contractions, Remove Special Characters, Stop Word Removal

2. **Normalization**:  Substitute Emojis with Text, Break Compound Words, Convert to Lowercase, Correct Spellings, Lemmatization

3. **Tokenization and vectorization**: Creating TF-IDF matrix




## Potential development:

**Efficient rescue operations**: By analyzing tweets related to disasters, the bot can provide real-time information about the situation on the ground, including the severity of the disaster and the location of those affected. This information can help rescue teams prioritize their efforts and allocate resources more efficiently.


