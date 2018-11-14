from connect_db import *
from db_schema import * 
from datetime import date
from get_tt import trending_topics
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

count = {}
data  = {}
avg_sentiment = {}

for tweet in Tweet.objects(retrieved__gte=date.today()):
    data[tweet.topic]  = data.get(tweet.topic,[]) + [float(tweet.sentiment)]
    count[tweet.topic] = count.get(tweet.topic, 0) + 1

for key in data:
    avg_sentiment[key] = round(sum(data[key])/count[key],4)

topic=[]
sentiment=[]

for t in trending_topics[:]:
    if t in avg_sentiment:
        topic.append(t)
        sentiment.append(avg_sentiment[t])

colors = []
for s in sentiment:
    if s < 0.40:
        colors.append('red')
    elif s > 0.60:
        colors.append('green')
    else:
        colors.append('gray')

#sns.scatterplot(topic,sentiment,palette=colors,alpha=0.8)
plt.scatter(topic,sentiment,c=colors,alpha=0.8)
plt.grid(True)
plt.xticks(rotation=90,fontsize=10)
plt.show()