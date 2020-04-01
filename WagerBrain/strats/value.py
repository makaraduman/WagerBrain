import numpy as np
import pandas as pd
from WagerBrain.probs import win_prob_to_odds


def spread_H_dog_to_fav(df):
    """
    American Odds of Home team winning after flipping from Dog to Fav
    If better than -235 (e.g., -200) that's a value bet. You're getting more favorable terms that historic results.
    :param df: dataframe of NBA odds provided in WagerBrain
    :return: The odds for the win % of function strategy
    """

    # How Often Does the Home Team Win When They Move From Dog to Fav
    idx = np.where((df['Home Spread Close'] < 0) & (df['Home Score'] > df['Away Score']))
    home_flip_spread_win = df.loc[idx]

    idc = np.where((df['Home Spread Close'] < 0))
    home_flip_spread_total = df.loc[idc]

    perc = len(home_flip_spread_win) / len(home_flip_spread_total)

    return win_prob_to_odds(perc)





file = '/Users/demmler/PycharmProjects/WagerBrain/WagerBrain/data/NBA Odds Complete.csv'
nba = pd.read_csv(file, header=0, parse_dates=['Date'])

print(spread_H_dog_to_fav(nba))