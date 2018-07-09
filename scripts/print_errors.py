def print_distr(t_crit_right, t_crit_left, t, u0, u1):
	 """Plots distribution data, critical values and error areas.

    Keyword arguments:
    t_crit_right -- right critical value
    t_crit_left -- left critical value
    t -- an array of t values for distributions
    u0 -- probability density for H0
    u1 -- probability density for H1
    """

	import matplotlib.pyplot as plt
	import matplotlib.patches as mpatches

	# plot statistical distributions
	h0_dist, = plt.plot(t, u0, 'r', alpha=0.35, label='PrD(T|H0)')
	h1_dist, = plt.plot(t, u1, 'b', alpha=0.35, label='PrD(T|H1)')
	
	# plot critical t values
	left_crit_line = plt.axvline(
		x=t_crit_left, color='red', label='T_critical_left',
		ymin = 0.05, ymax = 0.95, alpha=0.7, linewidth=1.5
		)
	right_crit_line = plt.axvline(
		x=t_crit_right, color='blue', label='T_critical_right', 
		ymin = 0.05, ymax = 0.95, alpha=0.7, linewidth=1.5
		)

	# fill in error areas
	plt.fill_between(t, u1, where=t <= t_crit_right, facecolor='blue', alpha=0.35)
	plt.fill_between(t, u0, where=t >= t_crit_right, facecolor='red', alpha=0.35)
	plt.fill_between(t, u0, where=t <= t_crit_left, facecolor='red', alpha=0.35)

	red_patch = mpatches.Patch(color='red', alpha=0.35, label='type 1 (alpha) error')
	blue_patch = mpatches.Patch(color='blue', alpha=0.35, label='type 2 (beta) error')

	# labels and legend
	plt.xlabel('T')
	plt.ylabel('Probability density')
	plt.legend(
		handles=[h0_dist, h1_dist, left_crit_line, right_crit_line, red_patch, blue_patch], 
		loc='upper center', bbox_to_anchor=(0.5, 1.00), ncol=3
		)
	plt.title("Type 1 and Type 2 errors")
	plt.grid(True)
	plt.show()