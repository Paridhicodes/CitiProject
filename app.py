from flask import Flask
from newsapi import NewsApiClient
from datetime import date, datetime, timedelta


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news')
def news():
    # /v2/top-headlines
    print("display news function reached")
    newsapi = NewsApiClient(api_key='4bfc19983cfc4f68badcdad72cdcc71d')
    current_dt = datetime.now().replace(microsecond = 0)
    past_dt = current_dt - \
                        timedelta(hours = 24)
    current_dt = current_dt.isoformat()
    # past_dt = date.today()
    past_dt = past_dt.isoformat()
    top_headlines = newsapi.get_everything(
                                        q = 'Nifty 200 Index',
                                        qintitle='NSE 200',
                                        language='en',
                                        from_param=past_dt,
                                        to=current_dt,
                                        sort_by='popularity',
                                       )
    articles = top_headlines['articles']
    desc = []
    news_title = []
    img = []
    source = []
    author = []
    p_date = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news_title.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage']) 
        source.append(myarticles['source'])
        author.append(myarticles['author'])
        p_date.append(myarticles['publishedAt'])
        url.append(myarticles['url'])
    
    mylist = zip(source, news_title, desc, author, img, p_date, url)

    return render_template('news.html', context = mylist)


if __name__ == "__main__":
    app.run(debug=True)