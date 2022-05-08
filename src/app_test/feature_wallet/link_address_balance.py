import requests as rq
import pandas as pd

def link_address_balance(address, chain_id):
    api_key = 'ckey_4e20bd1de6b3424c81eefbd7157'
    endpoint1 = "balances_v2"  #balance de chaque crypto
    
    url = "https://api.covalenthq.com/v1/{}/address/{}/{}/?key={}".format(chain_id, address, endpoint1, api_key)
    
    r = rq.get(url).json()['data']['items']
    df = pd.DataFrame(r)
    return(df)

'''
Fonction qui prend en argument une adresse et le numero de la blockchain.
Et qui retourne une DataFrame comprenant les élément neccesaire pour annalyser le wallet en balance
'''