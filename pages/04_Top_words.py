import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.util import ngrams
import seaborn as sns


@st.cache_data
def load_data():

    stop_words = nltk.corpus.stopwords.words('english')
    newStopWords = ['http','https','Û_','Û','co','Ûa']
    stop_words.extend(newStopWords)

    df = pd.read_csv('data/train.csv')
    
    def func1(text):
        ws = [w for w in text.split() if w.lower() not in stop_words]
        ws = [w for w in ws if w.isalnum()]
        return " ".join(ws)
    df['text1'] = df['text'].apply(func1)


    dfd = df[df['target'] == 1]
    dfg = df[df['target'] == 0]

    gunis = []
    gbigrams = []
    gtrigrams = []
    dunis = []
    dbigrams = []
    dtrigrams = []
    for ind in dfg.index:
        text = dfg.loc[ind,'text']
        text1 = dfg.loc[ind,'text1']
        gunis = gunis + [" ".join(g) for g in ngrams(text1.split(), 1)]
        gbigrams = gbigrams + [" ".join(g) for g in ngrams(text.split(), 2)]
        gtrigrams = gtrigrams + [" ".join(g) for g in ngrams(text.split(), 3)]
    for ind in dfd.index:
        text = dfd.loc[ind,'text']
        text1 = dfd.loc[ind,'text1']
        dunis = dunis + [" ".join(g) for g in ngrams(text1.split(), 1)]
        dbigrams = dbigrams + [" ".join(g) for g in ngrams(text.split(), 2)]
        dtrigrams = dtrigrams + [" ".join(g) for g in ngrams(text.split(), 3)]

    dftg_uni = pd.DataFrame(pd.DataFrame({'freq': gunis})['freq'].value_counts().head(10))
    dftg_uni.reset_index(inplace = True)
    dftd_uni = pd.DataFrame(pd.DataFrame({'freq': dunis})['freq'].value_counts().head(10))
    dftd_uni.reset_index(inplace = True)

    dftg_bi = pd.DataFrame(pd.DataFrame({'freq': gbigrams})['freq'].value_counts().head(10))
    dftg_bi.reset_index(inplace = True)
    dftd_bi = pd.DataFrame(pd.DataFrame({'freq': dbigrams})['freq'].value_counts().head(10))
    dftd_bi.reset_index(inplace = True)

    dftg_tri = pd.DataFrame(pd.DataFrame({'freq': gtrigrams})['freq'].value_counts().head(10))
    dftg_tri.reset_index(inplace = True)
    dftd_tri = pd.DataFrame(pd.DataFrame({'freq': dtrigrams})['freq'].value_counts().head(10))
    dftd_tri.reset_index(inplace = True)

    data_dict = {
        'Unigrams': {
                     'Disaster Tweets': dftd_uni,
                     'Non-Disaster Tweets': dftg_uni
                     },
        'Bigrams': {
                     'Disaster Tweets': dftd_bi,
                     'Non-Disaster Tweets': dftg_bi
                     },
        'Trigrams': {
                     'Disaster Tweets': dftd_tri,
                     'Non-Disaster Tweets': dftg_tri
                     }
        }
    return data_dict,dunis

data_dict,dunis = load_data()

data = st.selectbox('Choose Distribution', (data_dict.keys()))

subset = st.radio(
    "Choose subset",
    data_dict[data].keys())


if subset == 'Disaster Tweets':
    color = 'red'
else:
    color = 'green'
sns.barplot(data=data_dict[data][subset], x = 'freq', y = 'index',color = color, saturation=0.4)


plt.title(f'Top 10 most common {data} in {subset}')
st.pyplot(plt)