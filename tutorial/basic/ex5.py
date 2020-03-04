import numpy as np
import matplotlib.pyplot as plt


from sal_timer import timer



def plot_1():
    plt.subplot(1,2,1)
    plt.title('121')
    plt.subplot(1,2,2)
    plt.title('122')
    plt.show()


def plot_2():
    # third arg is index where to set the fig. ranges from 1 to numrows*numcols.

    # ...
    plt.subplot(341)
    plt.title('341')
    plt.subplot(342)
    plt.title('342')
    plt.subplot(343)
    plt.title('343')
    plt.subplot(344)
    plt.title('344')

    # ...
    plt.subplot(345)
    plt.title('345')
    plt.subplot(346)
    plt.title('346')
    plt.subplot(347)
    plt.title('347')
    plt.subplot(348)
    plt.title('348')

    # ...
    plt.subplot(349)
    plt.title('349')
    plt.subplot(3,4,10)
    plt.title('3,4,10')
    plt.subplot(3,4,11)
    plt.title('3,4,11')
    plt.subplot(3,4,12)
    plt.title('3,4,12')

    # ...
    plt.show()


def plot_3():
    plt.subplot(311)
    plt.title('311')
    plt.subplot(312)
    plt.title('312')
    plt.subplot(313)
    plt.title('313')
    plt.show()


def plot_4():
    plt.subplot(131)
    plt.title('131')
    plt.subplot(132)
    plt.title('132')
    plt.subplot(133)
    plt.title('133')
    plt.show()




@timer
def main():
    plot_1()
    plot_2()
    plot_3()
    plot_4()



if __name__ == '__main__':
    print('========================================== START ==========================================')
    #...
    main()
    print('========================================== END ============================================')