#Program 4
#CIS 443-75
#Grading ID: P5696
#Due: 4-21-21
#This lab analyzes csv file of reviews to determine if they are positive, neutral, or negative using Text Blob.

import pandas as pd
import csv
from textblob import TextBlob

#defines starter variables
yelp = pd.read_csv('yelp.csv', usecols = ['stars', 'text'])
star_rating = ''
ratingsList = []
textSentiment = []
textRating = []
text_rating = ''
agreeVar = 'true'
agreeList = []
agree = 0
disagree = 0
star5 = []
star4 = []
star3 = []
star2 = []
star1 = []
i = 0

#Calculates the rating sentiment
for rating in yelp['stars']:
        if rating == 4 or rating == 5:
            star_rating = 'positive'
        elif rating == 3:
            star_rating = 'neutral'
        elif rating == 1 or rating == 2:
            star_rating = 'negative'
        ratingsList.append(star_rating)
yelp['Star Sentiment'] = ratingsList

#Calculates the polarity of the text in the review
for text in yelp['text']:
    blob = TextBlob(text)
    textSentiment.append(blob.sentiment.polarity)
yelp['Text Polarity'] = textSentiment
    
#Classifies the polarity of the review to be positive, negative, or neutral
for sentiment in yelp['Text Polarity']:
    if sentiment > 0.05:
        text_rating = 'positive'
    elif sentiment < -0.05:
        text_rating = 'negative'
    elif sentiment >= -0.05 and sentiment <= 0.05:
        text_rating = 'neutral'
    textRating.append(text_rating)
yelp['Polarity'] = textRating

#Determines if the Text and Star sentiments match
for index in range(len(ratingsList)):
    if ratingsList[index] == textRating[index]:
        agreeVar = 'true'
    else:
        agreeVar = 'false'
    agreeList.append(agreeVar)
yelp['Agree?'] = agreeList

agree = agreeList.count('true')
disagree = agreeList.count('false')
percentAgree = (agree / (agree + disagree))*100
percentDisagree = (disagree / (agree + disagree))*100

print(f"{agree} ({percentAgree}%) reviews had the same sentiment for the star rating and text")
print(f"{disagree} ({percentDisagree}%) reviews were not the same")

for rating in yelp['stars']:
    if rating == 5:
        star5.append(agreeList[i])
    if rating == 4:
        star4.append(agreeList[i])
    if rating == 3:
        star3.append(agreeList[i])    
    if rating == 2:
        star2.append(agreeList[i])
    if rating == 1:
        star1.append(agreeList[i])
    i+=1

star5_agree = star5.count('true')
star4_agree = star4.count('true')
star3_agree = star3.count('true')
star2_agree = star2.count('true')
star1_agree = star1.count('true')

#Analysis for reviews with the same sentiment for rating and text
print("Stars \t\t Same Sentiment for Rating and Text")
print(f"  5\t\t\t\t {star5_agree}/{len(star5)} = {(star5_agree/len(star5))*100:>.2f}%")
print(f"  4\t\t\t\t {star4_agree}/{len(star4)} = {(star4_agree/len(star4))*100:>.2f}%")
print(f"  3\t\t\t\t {star3_agree}/{len(star3)} = {(star3_agree/len(star3))*100:>.2f}%")
print(f"  2\t\t\t\t {star2_agree}/{len(star2)} = {(star2_agree/len(star2))*100:>.2f}%")
print(f"  1\t\t\t\t {star1_agree}/{len(star1)} = {(star1_agree/len(star1))*100:>.2f}%")

print()

#Analysis for reviews with differing sentiment for rating and text    
print("Stars \t\t Different Sentiment for Rating and Text")
print(f"  5\t\t\t\t {(len(star5) - star5_agree)}/{len(star5)} = {(1 - (star5_agree/len(star5)))*100:>.2f}%")
print(f"  4\t\t\t\t {(len(star4) - star4_agree)}/{len(star4)} = {(1 - (star4_agree/len(star4)))*100:>.2f}%")
print(f"  3\t\t\t\t {(len(star3) - star3_agree)}/{len(star3)} = {(1 - (star3_agree/len(star3)))*100:>.2f}%")
print(f"  2\t\t\t\t {(len(star2) - star2_agree)}/{len(star2)} = {(1 - (star2_agree/len(star2)))*100:>.2f}%")
print(f"  1\t\t\t\t {(len(star1) - star1_agree)}/{len(star1)} = {(1 - (star1_agree/len(star1)))*100:>.2f}%")
