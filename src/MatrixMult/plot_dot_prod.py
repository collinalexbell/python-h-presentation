import matplotlib.pyplot as plt

def writeStats(stats, f, data, size, implementation):
    time_taken, _ = f(*data)
    stats[implementation].append({'size': size, 'time_taken': time_taken})
    return stats
if __name__ == '__main__':
    implementations = [f for f in globals().keys() if callable(globals()[f]) and '_' in f and f != 'python_implementation']
    stats = {k: [] for k in implementations}

    for i in range(100, 1500, 100):
        data = generate(i, range_=(1, 100))
        for implementation in implementations:
            stats = writeStats(stats, globals()[implementation], data, i, implementation)

    for implementation, stats_ in stats.items():
        plt.plot([n['size'] for n in stats[implementation]], [n['time_taken'] for n in stats[implementation]], label=implementation)
    plt.legend()
    plt.xlabel('Matrix size')
    plt.ylabel('Time taken')
    plt.show()
