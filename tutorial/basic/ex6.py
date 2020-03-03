import numpy as np
import matplotlib.pyplot as plt


from sal_timer import timer



def plot_1():
    # ...
    ax = plt.subplot(111)

    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2*np.pi*t)
    line, = plt.plot(t, s, lw=2)

    # ...
    plt.text(1, -1.5, r'$\mu=100,\ \sigma=15$')
    plt.text(4, 1.5, r'$\sum_{i=0}^\infty x_i$')
    
    plt.annotate(
        'local max',
        xy=(2, 1),
        xytext=(3, 1.5),
        arrowprops=dict(facecolor='black', shrink=0.05),
        )

    plt.ylim(-2, 2)
    plt.show()






@timer
def main():
    # https://matplotlib.org/tutorials/text/mathtext.html
    # https://matplotlib.org/tutorials/text/text_props.html
    plot_1()


if __name__ == '__main__':
    print('========================================== START ==========================================')
    #...
    main()
    print('========================================== END ============================================')