from matplotlib.lines import Line2D
import matplotlib.pyplot as plt 
from sklearn.decomposition import PCA
import pandas as pd 
import numpy as np 

def compute_PCA(data_stand, n_components=None, plot=False):
    pca = PCA(n_components)
    X = pca.fit_transform(data_stand)
    principal_df = pd.DataFrame(data = X)
    cum_exp_var = np.cumsum(np.round(pca.explained_variance_ratio_, decimals=4)*100)
    if plot:
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(cum_exp_var, 'b-o')
        ax.set_xlabel('Number of Components')
        ax.set_ylabel('Cumulative Explained Variance')
        # write the cumulative explained variance on the plot
        ymin, ymax = ax.get_ylim()
        step = (ymax-ymin)/principal_df.shape[1]
        for i, ev in enumerate(cum_exp_var):
            y_cord = cum_exp_var[i]-0.2*step
            ax.text(i, y_cord, np.round(ev), 
                    ha='left', va='top', fontsize=10)
            # put a point 
            # ax.scatter(i, cum_exp_var[i], s=50, c='blue', marker='o')
        return principal_df, pca, fig, ax 
    else:
        return principal_df, pca

def plot_2D_embedding(principal_df, color_labels=None, shape_labels=None,):
    # 2D plotting PCA
    fig, ax = plt.subplots(figsize=(8, 6))
    if color_labels is not None: 
        cmap = plt.get_cmap('Paired')
        n_col = len(set(color_labels))
        colors = cmap(np.linspace(0, 1, n_col)) 
        colors_dict = {label: colors[i] for i, label in enumerate(set(color_labels))}
        colors = [colors_dict[label] for label in color_labels]
    else:
        colors = "royalblue"

    
    if shape_labels is not None:
        shapes = ["o", "v", "^", "s", "P", "*", "D", "X", "d", "h", "H", "p", "8", "1"]
        shapes_dict = {label: shapes[i] for i, label in enumerate(set(shape_labels))}
        markers = [shapes_dict[label] for label in shape_labels] 
    else:
        markers = 'o'
    
    plot_df = principal_df.copy()
    plot_df['color'] = colors
    plot_df['marker'] = markers
    for i, row in plot_df.iterrows():
        ax.scatter(row[0], row[1], 
                   color=row['color'], marker=row['marker'])
    ax.set_xlabel('Principal Component 1', fontsize=15)
    ax.set_ylabel('Principal Component 2', fontsize=15)
    ax.set_title('2 component PCA', fontsize=20)
    ax.grid()
    
    if color_labels is not None: 
        color_legend_elements = [
            Line2D([0], [0], marker='o', color='w',
            markerfacecolor=colors_dict[label], label=label) for label in set(color_labels)
        ]
        leg1 = ax.legend(handles=color_legend_elements, bbox_to_anchor=(1.05, 0.8), 
              loc='upper left')
        ax.add_artist(leg1)

    if shape_labels is not None:
        shape_legend_elements = [
            Line2D([0], [0], marker=shapes_dict[label], color='w',
            markerfacecolor='b', label=label) for label in set(shape_labels)
        ] 
        leg2 = ax.legend(handles=shape_legend_elements, bbox_to_anchor=(1.05, 0.3),
                    loc='lower left')
    
    return fig, ax

    
