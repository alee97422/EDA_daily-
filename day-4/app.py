#Author: Anthony Lee
#date 11-15-2023
#made this program using the data set provided on kaggle (https://www.kaggle.com/datasets/willianoliveiragibin/ufo-sightings)


from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd 


df = pd.read_csv('ufo-sightings-transformed.csv')
words = df['Description'].tolist()
#print(successful) ### upset this program didnt run first try because i didnt put wrap successful in ' ' :( for shame
print('successful') # on some real left that there as a reminder that we are all human :) 
word_data = ' '.join(str(word) for word in words)
wordcloud = WordCloud(width=800, height=800, background_color='black').generate(word_data)
plt.figure(figsize=(8, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
plt.savefig('wordcloud_image.png')
