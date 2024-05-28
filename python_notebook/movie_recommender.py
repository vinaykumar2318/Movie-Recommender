#!/usr/bin/env python
# coding: utf-8

# # MOVIE RECOMMENDER SYSTEM

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


movies = pd.read_csv('movies.csv')
credits = pd.read_csv('credits.csv')
movies.head()


# In[3]:


movies = movies.merge(credits, on='title')
movies.shape


# In[4]:


movies.head()


# In[5]:


#Now we will drop columns we dont want
movies = movies[['movie_id','genres','keywords','cast','crew','title','overview']]
movies.head()


# In[6]:


movies.dropna(inplace = True)
movies.isnull().sum()


# In[7]:


movies.duplicated().sum()


# In[8]:


import ast

def doRequired(genre):
    tags = []
    for i in ast.literal_eval(genre):
        tags.append(i['name'])
    return tags

movies['genres'] = movies['genres'].apply(doRequired)
movies['keywords'] = movies['keywords'].apply(doRequired)
movies.head()


# In[9]:


def doRequiredNext(genre):
    tags = []
    start = 0
    for i in ast.literal_eval(genre):
        if start != 3:
            tags.append(i['name'])
            start += 1
        else:
            break
    return tags

movies['cast'] = movies['cast'].apply(doRequiredNext)

def doRequiredFind(genre):
    tags = []
    for i in ast.literal_eval(genre):
        if i['job']=='Director':
            tags.append(i['name'])
            break
    return tags

movies['crew'] = movies['crew'].apply(doRequiredFind)
movies.head()


# In[10]:


movies['overview'] = movies['overview'].apply(lambda x:x.split())
movies.head()


# In[11]:


movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['crew'] = movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])
movies.head()


# In[12]:


movies['tags'] = movies['overview'] + movies['keywords'] + movies['cast'] + movies['crew'] + movies['genres']
movies.head()


# In[13]:


final = movies[['movie_id','title','tags']]
final.head()


# In[14]:


final['tags'] = final['tags'].apply(lambda x:" ".join(x))
final['tags'] = final['tags'].apply(lambda x:x.lower())
final.head()


# In[15]:


import nltk


# In[16]:


from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def doStemming(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    
    return " ".join(y)

final['tags'] = final['tags'].apply(doStemming)
final.head()


# In[18]:


from sklearn.feature_extraction.text import TfidfVectorizer

vec = TfidfVectorizer(max_features=5000,stop_words='english')


# In[20]:


vectors = vec.fit_transform(final['tags']).toarray()


# In[27]:


print(list(vec.get_feature_names_out()))


# In[28]:


from sklearn.metrics.pairwise import cosine_similarity
similar = cosine_similarity(vectors)


# In[32]:


def recommend(movie_name):
    index = final[final['title']==movie_name].index[0]
    dist = similar[index]
    movies_list = sorted(list(enumerate(dist)),reverse = True, key = lambda x:x[1])[1:6]
    for i in movies_list:
        print(final.iloc[i[0]].title)


# In[40]:


recommend('Interstellar')


# In[41]:


import pickle
pickle.dump(final.to_dict(),open('movie.pkl','wb'))
pickle.dump(similar,open('similarity.pkl','wb'))


# In[ ]:




