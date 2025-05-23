import math
import matplotlib.pyplot as plt
import pandas as pd


def output_multi_scatter(df: pd.DataFrame, columns: list[str], target: str):
    '''
    Display subplots with scatter plots between all pairs of columns,
      from the given subset. Colored by "target" column
    Arguments:
        df:  input dataframe
        columns: the columns to use from df 
        target: the "special" column for coloring
    '''
    # calculate number of plots
    number_of_plots = int(
        math.factorial(len(columns)) / (2*math.factorial(len(columns)-2))
    )
    
    # create a side by side view of that many plots
    fig, ax = plt.subplots(1, number_of_plots)

    # this is for compatability with the case of one plot.
    if number_of_plots == 1:
        ax = [ax]

    counter = 0
    for i in range(len(columns)):
        for j in range(len(columns)):
            if i>=j:
                continue
            scatp1 = df.plot.scatter(
                x=columns[i],
                y=columns[j],
                figsize=(24, 8),
                c='diagnosis',
                colormap="jet",
                ax=ax[counter],
                # fontsize=10
            )
            
            ax[counter].set_xlabel(ax[counter].get_xlabel(), fontsize=20)
            ax[counter].set_ylabel(ax[counter].get_ylabel(), fontsize=20)
            # TODO set font to colorbar
            counter += 1

    print('goo')