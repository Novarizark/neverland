import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import numpy as np

class _plot_network(n_smp):
    n_smp=50
    data = np.zeros(50, 50)
    data[0,:]=xrange(0,50)
    data[0,:]=xrange(0,50)
    fig, ax = plt.subplots()
    ax.imshow(data[i])
