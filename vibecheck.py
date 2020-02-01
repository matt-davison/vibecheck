from flask import Flask, render_template, request
import jinja2
from Financial import finQuery
from Public import pubQuery
from News import newsQuery
app = Flask(__name__)

@app.route("/")
def query_template():
    queryReq = request.args.get('query')
    return render_template('query.html', query=queryReq)

if __name__ == '__main__':
    app.run()