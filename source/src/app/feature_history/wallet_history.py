import dateutil.parser
import matplotlib.pyplot as plt
import pandas as pd
from source.src.app.feature_history.link_address_history import link_address_history


def wallet_history(address, chain_id):
    """Formatting the information retrieved for a wallet

    Parameters:
    address (string): wallet address
    chain_id (int): chain id of the wallet

    Returns:
    cf (Dataframe): dataframe usable with the Holdings (en USD) and the date of this balance of the wallet
    """
    holding = link_address_history(address, chain_id)
    history = {}
    history_response = []
    for i in range(len(holding)):
        x = holding.loc[i]

        date = x["timestamp"]
        date = dateutil.parser.isoparse(date)
        history["Date"] = date.strftime("%Y-%m-%d")

        history["Holdings (en USD)"] = x["quote_rate"]

        history_response.append(history)
        history = {}

    cf = pd.DataFrame(history_response)
    return cf


if __name__ == "__main__":
    cf = print(wallet_history("0xb71f6064b01c7e2e14f3bb93db665400ac7acb37", 1))
    cf.plot(x="Date", y="Holdings (en USD)", kind="line")
    plt.show()
