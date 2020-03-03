import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sal_timer import timer



def plot_1(df):
    plt.subplot(111)
    plt.plot('Open', data=df)
    # plt.plot('Date','Open', data=df)
    plt.title('Google')
    plt.show()






@timer
def main():
    df = pd.read_csv(DATA_PATH)
    print(df.shape)
    print(df.head())
    plot_1(df)



DATA_PATH = '/home/sal/Python/matplotlib/matplotlib/data/GOOGL.csv'

if __name__ == '__main__':
    print('========================================== START ==========================================')
    #...
    main()
    print('========================================== END ============================================')