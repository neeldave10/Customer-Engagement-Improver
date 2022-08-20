from main import soundAndAnalysis
import database_activity

sentence,analysis=soundAndAnalysis()
for i in sentence:
    answer = analysis.polarity_scores(i)

s=answer['compound']


if s>0.2:
    cust_status="Happy"
elif s<=0.2 and s>=-0.2:
    cust_status="Neutral"
else:
    cust_status="NotHappy"


cust_id=2
obj=database_activity.Database()
senti=obj.getSentiment(cust_id)
previous_sentiment=senti[0][0]


if cust_status==previous_sentiment:
    print("Previous Sentiment is same as the new one")
    pass
else:
    update_string=obj.changingSentiment(cust_status,cust_id)
    print(update_string)





