from flask import Flask, render_template, request
import jinja2
from Public import pubQuery
from News import newsQuery
from Financial import finQuery
from textblob import TextBlob

def getSentiment(category):
#simple mean of a category's scores
    score = 0.0
    for testimony in category:
        testimonial = TextBlob(testimony)
        score += testimonial.sentiment.polarity
    return score/len(category)

app = Flask(__name__)

@app.route("/")
def query_template():
    queryReq = request.args.get('query')
    '''
    pubScore = getSentiment(pubQuery(queryReq))
    newsScore = getSentiment(newsQuery(queryReq))
    finScore = getSentiment(finQuery(queryReq))
    overallScore = pubScore + newsScore + finScore
    '''
    pubScore = 0.2
    newsScore = 0.4
    finScore = 1.0
    overallScore = 0.6
    if (overallScore >= 0.7):
        overall = "very positively"
    elif (overallScore >= 0.2):
        overall = "positively"
    elif (overallScore <= -0.7):
        overall = "very negatively"
    elif (overallScore <= -0.2):
        overall = "negatively"
    else:
        overall = "neutrally"
    
    return render_template('query.html', query=queryReq, pub=pubScore, news=newsScore, fin=finScore, overall=overall)

if __name__ == '__main__':
    app.run()