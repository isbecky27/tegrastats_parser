import csv
import matplotlib.pyplot as plt
import pandas as pd

colors = ['red', 'green', 'blue', 'yellow', 'pink', 'black', 'orange',
          'purple', 'brown', 'gray', 'cyan', 'magenta']

# pairs = [('Time (mS)', 'Used GR3D (%)'), ('Time (mS)', 'Current VDD_GPU_SOC Power Consumption (mW)')]

class Graph:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file, skiprows=1, header=0, index_col=0)
        self.pairs = [('Time (mS)', col)for col in self.df.head()[1:]]

    def scatter_plot(self, x, y):
        plt.figure()
        plt.title(f'{x} vs. {y}')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.plot(self.df.loc[:, x], self.df.loc[:, y])
        plt.savefig(f'{x} vs. {y}.png')

    def plots(self):
        for pair in self.pairs:
            self.scatter_plot(pair[0], pair[1])

if __name__ == '__main__':
    csv_file = 'log.csv'

    graph = Graph(csv_file)
    graph.plots()
