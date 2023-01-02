from flask import Flask
from newsapi import NewsApiClient
from datetime import date, datetime, timedelta
import pandas as pd
from nsepython import * 
from nsepy import get_history
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news')
def news():
    # /v2/top-headlines

    newsapi = NewsApiClient(api_key='4bfc19983cfc4f68badcdad72cdcc71d')
    current_dt = datetime.datetime.now().replace(microsecond = 0)
    past_dt = current_dt - \
                        timedelta(hours = 24)
    current_dt = current_dt.isoformat()

    past_dt = past_dt.isoformat()
    top_headlines = newsapi.get_everything(
                                        q = 'Nifty',
                                        qintitle='NSE',
                                        language='en',
                                        from_param=past_dt,
                                        to=current_dt,
                                        sort_by='relevancy',
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

@app.route('/stocks')
def stocks():
    positions = nsefetch('https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O')
    df=pd.DataFrame(positions['data'])
    df=df[['symbol','open','dayHigh', 'dayLow','lastPrice','totalTradedVolume','totalTradedValue','perChange30d']]
    return render_template('stocks.html',  tables=[df.to_html(classes='data')], titles=[])

@app.route('/report')
def report():
    #Market highlights, status, turnover, open interest
    #highlights
    import datetime

    current_dt = datetime.datetime.now().replace(microsecond = 0)
    past_dt = current_dt - \
                        timedelta(hours = 24)
    start_date = date.today()
    end_date = date.today()
    nse200_data = get_history(symbol = "NIFTY 200", start = past_dt, end = current_dt, index = True)

    #mkt status
    market_status = (nse_marketStatus())
    market_status = pd.DataFrame(market_status['marketState']).iloc[:,:8]

    #market turnover
        
    nifty = get_history(symbol="NIFTY", 
                        start=past_dt, 
                        end=current_dt,
                        index=True)

    bnifty = get_history(symbol="BANKNIFTY", 
                        start=past_dt, 
                        end=current_dt,
                        index=True)

    mkt_turnover=pd.concat([nifty,bnifty])


    import datetime
    end_date_avg = date.today()
    start_date_avg=(datetime.datetime.now()- datetime.timedelta(30)).date()
    nifty_avg = get_history(symbol="NIFTY", 
                        start=start_date_avg, 
                        end=end_date_avg,
                        index=True)
    avg_30_nifty=nifty_avg['Volume'].sum()/30.0

    bnifty_avg = get_history(symbol="BANKNIFTY", 
                        start=start_date_avg, 
                        end=end_date_avg,
                        index=True)
    avg_30_banknifty=bnifty_avg['Volume'].sum()/30.0

    mkt_turnover['30D Avg']=[avg_30_nifty,avg_30_banknifty]
    mkt_turnover.insert(loc=0,column='Category',value=['Nifty Index','BankNifty Index'])

 
    #open-interest options snapshot
    oi_data,ltp,crontime=oi_chain_builder('NIFTY')
    maxVal=oi_data.max()
    max_call_oi=maxVal['CALLS_OI']
    max_puts_oi=maxVal['PUTS_OI']
    max_call_oi_mov=maxVal['CALLS_Chng in OI']
    max_puts_oi_mov=maxVal['PUTS_Chng in OI']
    date_now=date.today()
    data={'Category':['Max Call Open Interest','Max Put Open Interest'],date_now:[max_call_oi,max_puts_oi],'Max OI Movement':[max_call_oi_mov,max_puts_oi_mov]}
    options_df = pd.DataFrame(data)

    #fiidii
    fiidii_data = nse_fiidii()

    return render_template('report.html', tables = [ mkt_turnover.to_html(classes='d3') , options_df.to_html(classes='d4'),  fiidii_data.to_html(classes='d5'),nse200_data.to_html(classes='d1'), market_status.to_html(classes='d2') ],
               titles = ['', "Market Turnover", "Options Snapshot", "Option Flows", "Market Highlights", "Market Status"])

if __name__ == "__main__":
    app.run(debug=True)