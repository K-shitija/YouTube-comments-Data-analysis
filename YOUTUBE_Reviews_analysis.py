# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 12:36:55 2024

@author: KSHITIJA
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from  textblob import TextBlob
from wordcloud import WordCloud , STOPWORDS 
import emoji
from collections import Counter
import plotly.graph_objs as go
from plotly.offline import iplot
import seaborn as sns


comments = pd.read_csv(r'F:\Python_project_persoanl\youtube_analysis\UScomments.csv', error_bad_lines=False)
print(comments.head())
print(comments.isnull().sum())

testing_polarity = TextBlob("The end though 😭👍🏻❤️").sentiment.polarity
print(testing_polarity, 'testing_polarity')
polarity = []

print(comments.shape)
sample_df = comments[0:20]
print(sample_df.shape)
for comment in comments['comment_text']:
    try :
        polarity.append(TextBlob(comment).sentiment.polarity)
        print(comment)
    except :
        polarity.append(0)
        
print(len(polarity) ,"lenght of polarity")
comments['polarity'] = polarity
print(comments.head(5))

filter_1 = comments['polarity']==1
comments_positive = comments[filter_1]
print(comments_positive.head(5))

filter_2 = comments['polarity']== -1
comments_negative = comments[filter_2]
print(comments_negative.head(5))

print("Type of comment_text column:  ",type(comments['comment_text']))

total_comments_positive = ' '.join(comments_positive['comment_text'])
print(total_comments_positive)
#STOPWORDS : set of strings or NONE that will be eliminated.
#meaningless wors i.e that , is , the ,it ,so ,there 
#set : unique elements
#print("set of stopwords: ", set(STOPWORDS))

wordcloud = WordCloud(stopwords = set(STOPWORDS)).generate(total_comments_positive)

print('list of wordcloud',wordcloud)
print("list printed")
print("Plot of wordcloud",plt.imshow(wordcloud))
print("plot printed")
plt.axis('off')
print("going to negative plot")
total_comments_negative = ' '.join(comments_negative['comment_text'])
print(total_comments_negative)
wordcloud1 =  WordCloud(stopwords = set(STOPWORDS)).generate(total_comments_negative)
print('list of wordcloud1',wordcloud1)
print("Plot of wordcloud1",plt.imshow(wordcloud1))
plt.axis('off')

#EMOJI ANALYSIS

print('Version of emoji is :', emoji.__version__)

comments['comment_text'].head(6)

# using list comprehension 
# [char for char in comment if char in emoji.EMOJI_DATA]
#can be written as
# emoji_list = []
# for char in comment:
#     if char in emoji.EMOJI_DATA:
#         emoji_list.append(char)

all_emojis_list = []
for comment in comments['comment_text'].dropna():
    for char in comment:
        if char in emoji.EMOJI_DATA:
            all_emojis_list.append(char)

print(all_emojis_list[0:10])

#calculate the number of times a specific emoji is observed

print(Counter(all_emojis_list).most_common(10))
# to get emoji and count
print("emojii and count",Counter(all_emojis_list).most_common(10)[0])
# to get only 
print("Emojii: ",Counter(all_emojis_list).most_common(10)[0][0])
#to get only count
print("Count: ",Counter(all_emojis_list).most_common(10)[0][1])

print("list of emojii's")
emojis = [Counter(all_emojis_list).most_common(10)[i][0] for i in range(10)]
print("list of emojis :",emojis)
freqs = [Counter(all_emojis_list).most_common(10)[i][1] for i in range(10)]

print("frequency of emojis :", freqs)

###PLOTTING BAR CHART

# trace= go.Bar(x = emojis , y= freqs)
# print(type(trace))
# print(iplot([trace]))
figure=sns.barplot(x=emojis , y = freqs)
print(figure)
# trace is list , take care of brackets



