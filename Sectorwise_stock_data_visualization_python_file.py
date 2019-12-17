import yfinance as yf


def data(ticker):
    data = yf.download(  # or pdr.get_data_yahoo(...
            # tickers list or string as well
            tickers = ticker + ".NS",
    
            # use "period" instead of start/end
            # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
            # (optional, default is '1mo')
            period = "60d",
    
            # fetch data by interval (including intraday if period < 60 days)
            # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
            # (optional, default is '1d')
            interval = "30m",
    
            # group by ticker (to access via data['SPY'])
            # (optional, default is 'column')
            group_by = 'ticker',
    
            # adjust all OHLC automatically
            # (optional, default is False)
            auto_adjust = True,
    
            # download pre/post regular market hours data
            # (optional, default is False)
            prepost = True,
    
            # use threads for mass downloading? (True/False/Integer)
            # (optional, default is True)
            threads = True,
    
            # proxy URL scheme use use when downloading?
            # (optional, default is None)
            proxy = None
        )
    
    return data


def makedf(list):
    d = {}
    for i in range(0,len(list)):
        d['df'+str(i+1)] = data(list[i])
    return d


def plot(list,sector):
    d = makedf(list)
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(10, 8))
    axes[0,0].plot(d['df1'].Close)
    axes[0,0].set(xlabel=list[0])
    axes[0,0].grid(axis='x')
    
    
    axes[0,1].plot(d['df2'].Close)
    axes[0,1].set(xlabel=list[1])
    axes[0,1].grid(axis='x')
    
    axes[0,2].plot(d['df3'].Close)
    axes[0,2].set(xlabel=list[2])
    axes[0,2].grid(axis='x')
    
    axes[1,0].plot(d['df4'].Close)
    axes[1,0].set(xlabel=list[3])
    axes[1,0].grid(axis='x')
    
    axes[1,1].plot(d['df5'].Close)
    axes[1,1].set(xlabel=list[4])
    axes[1,1].grid(axis='x')
    
    axes[1,2].plot(d['df6'].Close)
    axes[1,2].set(xlabel=list[5])
    axes[1,2].grid(axis='x')
    
    axes[2,0].plot(d['df7'].Close)
    axes[2,0].set(xlabel=list[6])
    axes[2,0].grid(axis='x')
    
    axes[2,1].plot(d['df8'].Close)
    axes[2,1].set(xlabel=list[7])
    axes[2,1].grid(axis='x')
    
    axes[2,2].plot(d['df9'].Close)
    axes[2,2].set(xlabel=list[8])
    axes[2,2].grid(axis='x')
    
    fig.suptitle(sector)
    fig.subplots_adjust(top=0.88)
    fig.tight_layout()
    #fig.autofmt_xdate(rotation=45)
    fig.savefig(r"C:\Users\Asus\Desktop\pproject\options algo\\" + sector + ".png")
    

nifty_bank = 'KOTAKBANK	INDUSINDBK	HDFCBANK	AXISBANK	ICICIBANK	RBLBANK	SBIN	BANKBARODA	FEDERALBNK	YESBANK	PNB	IDFCFIRSTB'
nifty_auto = 'MRF	EICHERMOT	BOSCHLTD	MARUTI	BAJAJ-AUTO	HEROMOTOCO	AMARAJABAT	M&M	TVSMOTOR	BHARATFORG	EXIDEIND	TATAMOTORS	APOLLOTYRE	MOTHERSUMI	ASHOKLEY'
nifty_finserv = 'BAJAJFINSV	BAJFINANCE	BAJAJHLDNG	HDFC	KOTAKBANK	ICICIGI	HDFCBANK	SRTRANSFIN	SBILIFE	AXISBANK	HDFCLIFE	ICICIPRULI	ICICIBANK	M&MFIN	SBIN	CHOLAFIN	IBULHSGFIN	RECLTD	EDELWEISS	PFC'
nifty_fmcg = 'NESTLEIND	PGHH	BRITANNIA	HINDUNILVR	JUBLFOOD	COLPAL	UBL	GODREJCP	MCDOWELL-N	DABUR	GODREJIND	MARICO	EMAMILTD	TATAGLOBAL	ITC'
nifty_it = 'TCS	NIITTECH	HCLTECH	TATAELXSI	TECHM	INFY	MINDTREE	JUSTDIAL	HEXAWARE	WIPRO'
nifty_media = 'PVR	SUNTV	SAREGAMA	INOXLEISUR	TVTODAY	ZEEL	DBCORP	BALAJITELE	JAGRAN	RADIOCITY	TV18BRDCST	NETWORK18	HATHWAY	DISHTV	ZEEMEDIA'
nifty_metal = 'APLAPOLLO	RATNAMANI	TATASTEEL	JSWSTEEL	HINDZINC	COALINDIA	HINDALCO	VEDL	MOIL	JINDALSTEL	WELCORP	NMDC	NATIONALUM	HINDCOPPER	SAIL'
nifty_pharma = 'DRREDDY	PEL	DIVISLAB	LUPIN	CIPLA	SUNPHARMA	AUROPHARMA	GLENMARK	BIOCON	CADILAHC'
nifty_psu = 'SBIN	CANBK	INDIANB	BANKBARODA	BANKINDIA	PNB	UNIONBANK	ORIENTBANK	J&KBANK	SYNDIBANK	ALBK	CENTRALBK'
nifty_private_bank = 'KOTAKBANK	INDUSINDBK	HDFCBANK	AXISBANK	ICICIBANK	RBLBANK	CUB	FEDERALBNK	YESBANK	IDFCFIRSTB'
nifty_realty = 'GODREJPROP	PHOENIXLTD	OBEROIRLTY	SUNTECK	SOBHA	MAHLIFE	PRESTIGE	DLF	BRIGADE	IBREALEST'



nifty_bank = nifty_bank.split()[0:9]
plot(nifty_bank,'nifty_bank')
df = makedf(nifty_bank)

nifty_auto = nifty_auto.split()[0:9]
plot(nifty_auto,'nifty_auto')

nifty_finserv = nifty_finserv.split()[0:9]
plot(nifty_finserv,'nifty_finserv')

nifty_fmcg = nifty_fmcg.split()[0:9]
plot(nifty_fmcg,'nifty_fmcg')

nifty_it = nifty_it.split()[0:9]
plot(nifty_it,'nifty_it')

nifty_media = nifty_media.split()[0:9]
plot(nifty_media,'nifty_media')

nifty_metal = nifty_metal.split()[0:9]
plot(nifty_metal,'nifty_metal')

nifty_pharma = nifty_pharma.split()[0:9]
plot(nifty_pharma,'nifty_pharma')

nifty_psu = nifty_psu.split()[0:9]
plot(nifty_psu,'nifty_psu')

nifty_private_bank = nifty_private_bank.split()[0:9]
plot(nifty_private_bank,'nifty_private_bank')

nifty_realty = nifty_realty.split()[0:9]
plot(nifty_realty,'nifty_realty')



# =============================================================================
# For Tableau
# =============================================================================

import pandas as pd
nifty_bank = 'KOTAKBANK	INDUSINDBK	HDFCBANK	AXISBANK	ICICIBANK	RBLBANK	SBIN	BANKBARODA	FEDERALBNK	YESBANK	PNB	IDFCFIRSTB'
nifty_bank = nifty_bank.split()[0:9]
plot(nifty_bank,'nifty_bank')
df = makedf(nifty_bank)

writer = ExcelWriter(r'C:\Users\Asus\Desktop\stock.xlsx')

for i in df.keys():
    df1  =  df[i]
    df1.reset_index(inplace=True)
    df1['Datetime'] = df1['Datetime'].dt.tz_localize(None)
    
    from pandas import ExcelWriter
    df1.to_excel(writer,'Sheet' + i)
writer.save()
    





















