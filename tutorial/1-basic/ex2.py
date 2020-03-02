import numpy as np
import matplotlib.pyplot as plt


from sal_timer import timer



def plot_1():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
    plt.axis([0, 6, 0, 20])
    plt.show()


def plot_2_1():
    a = np.arange(0., 5., 0.2)

    plt.plot(a, a, 'r-')
    plt.plot(a, a**2, 'b--')
    plt.plot(a, a**3, 'g-.')
    plt.plot(a, a**4, 'c:')
    plt.plot(a, a**5, '^m:')
    
    plt.show()


def plot_2_2():
    a = np.arange(0., 5., 0.2)

    plt.plot(a, a, 'm*')
    plt.plot(a, a**2, 'b^')
    plt.plot(a, a**3, 'go')
    
    plt.show()


def plot_2_3():
    a = np.arange(0., 5., 0.2)

    plt.plot(a, a, 'm+')
    plt.plot(a, a**2, 'bx')

    
    plt.show()


def plot_2():
    a = np.arange(0., 5., 0.2)

    plt.subplot(131)
    plt.plot(a, a, 'r-')
    plt.plot(a, a**2, 'b--')
    plt.plot(a, a**3, 'g-.')
    plt.plot(a, a**4, 'c:')
    plt.subplot(132)
    plt.plot(a, a, 'm*')
    plt.plot(a, a**2, 'b^')
    plt.plot(a, a**3, '^k:')
    plt.subplot(133)
    plt.plot(a, a, 'm+')
    plt.plot(a, a**2, 'rx')
    plt.plot(a, a**3, 'go')

    plt.show()


@timer
def main():
    # plot_1() # Formatting the style of your plot
    plot_2()
    # plot_2_1() # list of line styles
    # plot_2_2() # list of line styles
    # plot_2_3() # list of line styles



if __name__ == '__main__':
    print('========================================== START ==========================================')
    #...
    main()
    print('========================================== END ============================================')