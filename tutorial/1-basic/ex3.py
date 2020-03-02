import numpy as np
import matplotlib.pyplot as plt


from sal_timer import timer



def plot_1():
    # ...
    data = {
        'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)
    }
    data['b'] = data['a'] + 10 * np.random.randn(50)
    data['d'] = np.abs(data['d']) * 100

    # ...
    # x : x
    # y : y
    # c : color
    # s : size
    plt.scatter(x='a', y='b', c='c', s='d', data=data)

    # ...
    plt.xlabel('entry a')
    plt.ylabel('entry b')
    plt.show()



@timer
def main():
    plot_1()



if __name__ == '__main__':
    print('========================================== START ==========================================')
    #...
    main()
    print('========================================== END ============================================')