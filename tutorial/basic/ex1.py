import numpy as np
import matplotlib.pyplot as plt


from sal_timer import timer


def plot_1():
    plt.plot([25, 28, 30, 44])
    plt.show()


def plot_2():
    plt.plot(
        [25, 28, 30, 44],
        [2, 10, 30, 64]
    )
    plt.show()


def plot_3():
    plt.plot(
        [25, 28, 30, 44],
        [2, 10, 30, 64],
    )
    
    plt.plot(
        [2, 2, 3, 44],
        [2, 10, 30, 64]
    )
    plt.show()


def plot_4():
    plt.plot(
        [25, 28, 30, 44],
        [2, 10, 30, 64],
        [2, 2, 3, 44],
        [2, 10, 30, 64],
    )
    plt.show()


def plot_5():
    # too many code
    plt.plot(
        [25, 28, 30, 44],
        [2, 10, 30, 64],
        'rx-',
        [2, 2, 3, 44],
        [2, 10, 30, 64],
        'bo-',
        linewidth=.5
    )
    plt.show()


    # less code

    lines = plt.plot(
        [25, 28, 30, 44],
        [2, 10, 30, 64],
        [2, 2, 3, 44],
        [2, 10, 30, 64],
    )
    plt.setp(lines, c='r', linewidth=0.5)
    plt.show()


@timer
def main():
    # plot_1() # Simple plot
    # plot_2() # Simple plot with x/y
    # plot_3() # plot tow/... lines
    # plot_4() # plot tow/... lines using one method
    plot_5() # plot multi line with same style



if __name__ == '__main__':
    print('========================================== START ==========================================')
    #...
    main()
    print('========================================== END ============================================')