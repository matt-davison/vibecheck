from flask import Flask, render_template, request
import jinja2
from Public import pubQuery
from News import newsQuery
from Financial import finQuery
from textblob import TextBlob

VERY_THRES = 0.4
THRES = 0.15
SCALE = 3.5
BALANCE = -.4

def getSentiment(category):
#simple mean of a category's scores
    score = 0.0
    for testimony in category:
        testimonial = TextBlob(testimony)
        score += testimonial.sentiment.polarity
    res = score/len(category) * SCALE + BALANCE
    if res > 1.0:
        res = 1.0
    elif res < -1.0:
        res = -1.0
    return res

app = Flask(__name__)

@app.route("/")
def query_template():
    queryReq = request.args.get('query')
    if (queryReq):
        pubScore = getSentiment(pubQuery(queryReq))
        newsScore = getSentiment(newsQuery(queryReq))
        finScore = getSentiment(finQuery(queryReq))
        overallScore = (pubScore + newsScore + finScore) / 3
    else:
        pubScore = 0.0
        newsScore = 0.0
        finScore = 0.0
        overallScore = 0.0
    if (overallScore >= VERY_THRES):
        overall = "very positively"
    elif (overallScore >= THRES):
        overall = "positively"
    elif (overallScore <= -1*VERY_THRES):
        overall = "very negatively"
    elif (overallScore <= -1*THRES):
        overall = "negatively"
    else:
        overall = "neutrally"
    data = {'pubScore': pubScore, 'newsScore': newsScore, 'finScore': finScore, 'VERY_THRESH': VERY_THRES, 'OP_THRESH': THRES}
    return render_template('query.html', query=queryReq, overall=overall, data=data)

if __name__ == '__main__':
    app.run()