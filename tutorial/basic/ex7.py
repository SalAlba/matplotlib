import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sal_timer import timer

import matplotlib.cbook as cbook
import matplotlib.dates as mdates

def plot_1(df):
    fig, ax = plt.subplots()
    # plt.plot('Open', data=df)
    plt.plot('Date','Open', data=df)
    fig.autofmt_xdate()

    plt.title('Google')
    plt.show()






@timer
def main():
    df = pd.read_csv(DATA_PATH)
    df['Date'] = pd.to_datetime(df['Date'])
    print(df.shape)
    print(df.head())
    plot_1(df)



DATA_PATH = '/home/sal/Python/matplotlib/matplotlib/data/GOOGL.csv'

if __name__ == '__main__':
    print('========================================== START ==========================================')
    #...
    main()
    print('========================================== END ============================================')