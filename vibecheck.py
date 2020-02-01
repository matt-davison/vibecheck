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
    if (queryReq):
        pubScore = getSentiment(pubQuery(queryReq))
        newsScore = getSentiment(newsQuery(queryReq))
        finScore = getSentiment(finQuery(queryReq))
        overallScore = pubScore + newsScore + finScore
    else:
        pubScore = 0.0
        newsScore = 0.0
        finScore = 0.0
        overallScore = 0.0
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
    data = {'pubScore': pubScore, 'newsScore': newsScore, 'finScore': finScore}
    return render_template('query.html', query=queryReq, overall=overall, data=data)

if __name__ == '__main__':
    app.run()