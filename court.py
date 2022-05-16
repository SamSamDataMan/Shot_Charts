import seaborn as sns
from matplotlib.patches import Arc
import matplotlib.pyplot as plt

def draw_court(plot):
    """ draw_court draws an NBA halfcourt

    @param plot (seaborn.axisgrid.JointGrid): Figure
        object containing the plotted shot density
    Returns:

        fig (seaborn.axisgrid.JointGrid): Figure object visualizing
            an NBA court, overlayed with shot density
    """

    # These create the straight line portions of the court markings
    plot.ax_joint.plot([-250, 250], [-40, -40], 'k-')  # endline
    plot.ax_joint.plot([-250, 250], [430, 430], 'k-')  # halfcourt line
    plot.ax_joint.plot([-250, -250], [-40, 430], 'k-')  # sideline
    plot.ax_joint.plot([250, 250], [-40, 430], 'k-')  # sideline
    plot.ax_joint.plot([-30, 30], [-10, -10], 'k-')  # backboard
    plot.ax_joint.plot([-60, -60], [-40, 150], 'k-')  # lane
    plot.ax_joint.plot([60, 60], [-40, 150], 'k-')  # lane
    plot.ax_joint.plot([-80, -80], [-40, 150], 'k-')  # lane
    plot.ax_joint.plot([80, 80], [-40, 150], 'k-')  # lane
    plot.ax_joint.plot([-80, 80], [150, 150], 'k-')  # foul line

    plot.ax_joint.plot([220, 220], [-40, 90], 'k-')  # 3pt straight
    plot.ax_joint.plot([-220, -220], [-40, 90], 'k-')  # 3pt straight

    # These create the several circular portions of the court markings
    three_point = Arc((0, 0), width=237.5 * 2, height=237.5 * 2, theta1=22, theta2=158, linewidth=1.5)
    top_key = Arc((0, 150), width=60 * 2, height=60 * 2, theta1=0, theta2=180, linewidth=1.5)
    bottom_key = Arc((0, 150), width=60 * 2, height=60 * 2, theta1=180, theta2=360, linewidth=1.5, linestyle='--')
    basket = Arc((0, 0), width=7.5 * 2, height=7.5 * 2, theta1=0, theta2=360, linewidth=1.5)
    restricted = Arc((0, 7.5), width=40 * 2, height=40 * 2, theta1=0, theta2=180, linewidth=1.5)
    half_court = Arc((0, 430), width=60 * 2, height=60 * 2, theta1=180, theta2=360, linewidth=1.5)

    plot.ax_joint.add_patch(three_point)
    plot.ax_joint.add_patch(top_key)
    plot.ax_joint.add_patch(bottom_key)
    plot.ax_joint.add_patch(basket)
    plot.ax_joint.add_patch(restricted)
    plot.ax_joint.add_patch(half_court)

    # Adjusting figure properties
    plot.ax_joint.set_ylim(-50, 450)
    plot.ax_joint.set_aspect('equal')
    plot.fig.set_size_inches(10, 10)
    plot.ax_joint.set_xlabel('')
    plot.ax_joint.set_ylabel('')
    plot.ax_joint.set(xticks=[])
    plot.ax_joint.set(yticks=[])
    plot.ax_joint.set_axis_off()

    return plot


def plot_shot_chart(shot_df, title, plot_type='hex'):
    # Plot the type of 2D shot density estimation desired
    if plot_type == 'hex':
        plot = sns.jointplot(x=-shot_df['X Location'], y=shot_df['Y Location'], kind=plot_type, gridsize=30)
    elif plot_type == 'kde':
        plot = sns.jointplot(x=-shot_df['X Location'], y=shot_df['Y Location'], kind=plot_type)  # TODO Slider for number of levels in kde plot
    elif plot_type == 'contour':
        plot = (sns.jointplot(x=-shot_df['X Location'],
                              y=shot_df['Y Location'],
                              color='b',
                              alpha=0.005).plot_joint(sns.kdeplot, zorder=0, n_levels=45))  # TODO Slider for number of levels in contour plot
    else:
        print("Oops! You've provided an invalid plot_type value. Please use 'hex', 'kde', or 'contour'")
        return None

    # Draw NBA court markings and write title
    plot = draw_court(plot)
    plot.ax_joint.set_title(title, fontsize=14)
    plt.show()
    plt.close()

    return plot


def shot_chart_scatterplot(shot_df, title):
    grid = sns.JointGrid(x=-shot_df['X Location'], y=shot_df['Y Location'])
    g = grid.plot_joint(sns.scatterplot,
                        hue=shot_df['Shot Made Flag'],
                        style=shot_df['Shot Made Flag'],
                        markers=['X', 'o'],
                        palette=['r', 'g'],
                        s=75)

    # Draw NBA court markings and write title
    plot = draw_court(g)
    plot.ax_joint.set_title(title, fontsize=14)
    plt.show()
    plt.close()
    return plot
