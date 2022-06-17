from ssl import ALERT_DESCRIPTION_HANDSHAKE_FAILURE
import seaborn as sns
from matplotlib.patches import Arc
import matplotlib.pyplot as plt

def draw_court(fig, ax):
    fig = fig
    ax = ax

    plt.plot([-250, 250], [-40, -40], 'k-')
    plt.plot([-250, 250], [430, 430], 'k-')  # halfcourt line
    plt.plot([-250, -250], [-40, 430], 'k-')  # sideline
    plt.plot([250, 250], [-40, 430], 'k-')  # sideline
    plt.plot([-30, 30], [-10, -10], 'k-')  # backboard
    plt.plot([-60, -60], [-40, 150], 'k-')  # lane
    plt.plot([60, 60], [-40, 150], 'k-')  # lane
    plt.plot([-80, -80], [-40, 150], 'k-')  # lane
    plt.plot([80, 80], [-40, 150], 'k-')  # lane
    plt.plot([-80, 80], [150, 150], 'k-')  # foul line

    plt.plot([220, 220], [-40, 90], 'k-')  # 3pt straight
    plt.plot([-220, -220], [-40, 90], 'k-')  # 3pt straight

    # These create the several circular portions of the court markings
    three_point = Arc((0, 0), width=237.5 * 2, height=237.5 * 2, theta1=22, theta2=158, linewidth=1.5)
    top_key = Arc((0, 150), width=60 * 2, height=60 * 2, theta1=0, theta2=180, linewidth=1.5)
    bottom_key = Arc((0, 150), width=60 * 2, height=60 * 2, theta1=180, theta2=360, linewidth=1.5, linestyle='--')
    basket = Arc((0, 0), width=7.5 * 2, height=7.5 * 2, theta1=0, theta2=360, linewidth=1.5)
    restricted = Arc((0, 7.5), width=40 * 2, height=40 * 2, theta1=0, theta2=180, linewidth=1.5)
    half_court = Arc((0, 430), width=60 * 2, height=60 * 2, theta1=180, theta2=360, linewidth=1.5)

    ax.add_patch(three_point)
    ax.add_patch(top_key)
    ax.add_patch(bottom_key)
    ax.add_patch(basket)
    ax.add_patch(restricted)
    ax.add_patch(half_court)

    # Adjusting figure properties
    ax.set_ylim(-50, 450)
    ax.set_aspect('equal')
    fig.set_size_inches(10, 10)
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set(xticks=[])
    ax.set(yticks=[])
    ax.set_axis_off()

def shot_chart_scatterplot(shot_df, marker_size, markers, palette):
    return sns.scatterplot(x=-shot_df['X Location'],
                           y=shot_df['Y Location'],
                           hue=shot_df['Shot Made Flag'],
                           style=shot_df['Shot Made Flag'],
                           markers=markers,
                           palette=palette,
                           s=marker_size)

def shot_chart_hex(shot_df, grid_size):
    return plt.hexbin(x=-shot_df['X Location'],
                      y=shot_df['Y Location'],
                      gridsize=grid_size,
                      bins='log',
                      cmap='Reds'
                      )

def shot_chart_kde(shot_df, levels):
    return sns.kdeplot(data=shot_df,
                       x=-shot_df['X Location'],
                       y=shot_df['Y Location'],
                       color='seagreen',
                       thresh=.1,
                       shade=True,
                       shade_lowest=False,
                       levels=levels)

def shot_chart_contour(shot_df, levels):
    return sns.kdeplot(data=shot_df,
                       x=-shot_df['X Location'],
                       y=shot_df['Y Location'],
                       color='seagreen',
                       thresh=.1,
                       levels=levels)
