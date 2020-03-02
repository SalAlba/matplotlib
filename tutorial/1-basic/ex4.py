import numpy as np
import matplotlib.pyplot as plt


from sal_timer import timer



def plot_1():
    # ...
    names = ['group_a', 'group_b', 'group_c', 'group_d']
    values = [1., 10., -5., 0.]

    # ...
    plt.figure(figsize=(9, 3))

    plt.subplot(131)
    plt.bar(names, values)
    plt.subplot(132)
    plt.scatter(names, values)
    plt.subplot(133)
    plt.plot(names, values)
    plt.suptitle('Categorical Plotting')
    plt.show()



@timer
def main():
    plot_1()



if __name__ == '__main__':
    print('========================================== START ==========================================')
    #...
    main()
    print('========================================== END ============================================')