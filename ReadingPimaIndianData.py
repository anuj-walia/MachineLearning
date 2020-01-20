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
    # plt.show()


df = pd.read_csv("/tmp/ml/data/pima-data.csv")
print(df.shape)
print(df.isnull().values.any())
plot_corr(df)
print(df.head(10))
# print(df['skin','thickness'])
print("=================skin column=================")
print(df['skin'])
print("=================skin column end=================")
del df['skin']
print("==============printing first 10 rows====================")
print(df.head(10))
print("================printing first 10 rows end========================")
print("=================printing shape=================")
print(df.shape)
print("=================printing shape end=================")
plot_corr(df)
plot_corr(df,10)

boolean_map={True:1,False:0}
boolean_map_String={'True':1,'False':0}
df['diabetes']=df['diabetes'].map(boolean_map)

print("==============printing first 10 rows====================")
print(df.head(10))
print("================printing first 10 rows end========================")

num_true=len(df.loc[df['diabetes']==1])
num_false=len(df.loc[df['diabetes']==0])
print('Number of true cases: {0} {1:2.2f}'.format(num_true,(num_true/(num_false+num_true))*100))
print('Number of false cases: {0} {1:2.2f}'.format(num_false,(num_false/(num_false+num_true))*100))