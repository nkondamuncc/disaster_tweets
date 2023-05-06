import streamlit as st
import nltk
import pandas as pd
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

stop_words = nltk.corpus.stopwords.words('english')
newStopWords = ['http','https','Û_','Û','co','Ûa']
stop_words.extend(newStopWords)

@st.cache_data
def load_data():
    df = pd.read_csv('data/train.csv')


    words = []
    for ind in df.index:
        text = df.loc[ind,'text']
        words = words + word_tokenize(text)
        text = " ".join([word for word in words if len(word)>3])

    dfg = df[df['target']==0]
    gwords = []
    for ind in dfg.index:
        gtext = dfg.loc[ind,'text']
        gwords = gwords + word_tokenize(gtext)
        gtext = " ".join([gword for gword in gwords if len(gword)>3])

    dfd = df[df['target']==1]
    dwords = []
    for ind in dfd.index:
        dtext = dfd.loc[ind,'text']
        dwords = dwords + word_tokenize(dtext)
        dtext = " ".join([dword for dword in dwords if len(dword)>3])
    
    subsets = {
    "All Tweets": [text,'Blues'],
    "Disaster Tweets": [dtext,'Reds'],
    "Non-Disaster Tweets": [gtext,'Greens'],
    }
    return subsets

def show_wc(text,cmap):
    bc = st.get_option('theme.backgroundColor')
    mask = np.array(Image.open(r'data/10wmt-superJumbo-v4.jpg'))
    st.write(bc)
    wordcloud = WordCloud( max_font_size=200,width=2000, height=1000,max_words=150,collocations=False,stopwords=stop_words,background_color='black', colormap=cmap, mask=mask).generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    st.pyplot(plt)

subsets = load_data()
data = st.selectbox('Choose Subset', (subsets.keys()))

show_wc(subsets[data][0],subsets[data][1])
