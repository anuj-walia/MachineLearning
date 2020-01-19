import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def plot_corr(dataframe, size=11):
    ##
    """
    Function plots a graphical correlation matrix for each pair pf columns in the dataframe

    :param dataframe: Dataframe for which correlation needs to be plotted
    :param size: vertical and horizontal size of plot
    :displays:
                matrix of correlation between columns. blue-cyan-yellow-red-darkred.
                0---------------------------------------------------------------->1
    """
    ##
    corr=df.corr()
    print(corr)
    fig, ax = plt.subplots(figsize=(size,size))
    ax.matshow(corr) #color code the correlations by the correlation value
    plt.xticks(range(len(corr.columns)),corr.columns) # draw x tickmarks
    plt.yticks(range(len(corr.columns)),corr.columns) # draw y tickmarks
    plt.show()


df = pd.read_csv("/tmp/ml/data/pima-data.csv")
print(df.shape)
print(df.isnull().values.any())
plot_corr(df)