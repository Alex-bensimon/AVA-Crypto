import pandas as pd
import requests as rq

from ..utils.utils import get_base_url_cqt_api, get_cqt_api_key


def link_address_history(address, chain_id):
    """Retrieving and formatting information from the api

    Parameters:
    address (string): wallet address
    chain_id (int): chain id of the wallet

    Returns:
    df (Dataframe): dataframe usable with all the information of the api
    """
    api_key = get_cqt_api_key()
    base_url = get_base_url_cqt_api()
    url = "{}/address/{}/portfolio_v2/?key={}".format(chain_id, address, api_key)
    full_url = "".join([base_url, url])
    holding = rq.get(full_url).json()["data"]["items"][0]["holdings"]

    return pd.DataFrame(holding)


if __name__ == "__main__":
    print(link_address_history("0xb71f6064b01c7e2e14f3bb93db665400ac7acb37", 1))
