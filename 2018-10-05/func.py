import numpy as np
import matplotlib.pyplot as plt

def plot_data(inputs,targets,weights):
    plt.figure(figsize=(10,6))
    plt.box(False)
    plt.grid(True)
    plt.yticks(np.unique(inputs[:,1]))
    plt.xticks(np.unique(inputs[:,0]))
    for input,target in zip(inputs,targets):
        plt.plot(input[0],input[1],'ro' if (target == 1.0) else 'bo', markersize=12)
    for i in np.linspace(np.amin(inputs[:,:1]),np.amax(inputs[:,:1])):
        slope = -(weights[0]/weights[2])/(weights[0]/weights[1])  
        intercept = -weights[0]/weights[2]
        y = (slope*i) + intercept
        plt.plot(i, y, 'ko', markersize=10)
