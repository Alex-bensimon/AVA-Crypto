from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
import pandas as pd

def test_price(crypto='bitcoin'):
    '''The current price of a cryptocurrency
    
    Parameters:
    crypto (string): name of the cryptocurrency
    
    Returns:
    price[crypto]['usd'] (float): the current price of the crytpo 
    'green' or 'red'(string): if the crypto is in profit or in loss since 24h
    '''
    r = cg.get_price(ids=crypto, vs_currencies='usd', include_24hr_change='true')
    price = pd.DataFrame(r)
    if price[crypto]['usd_24h_change'] >=0:
        return(price[crypto]['usd'], 'green')
    else :
        return(price[crypto]['usd'], 'red')

