import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import product
from sequoia import *

levels = [0,1,2,3,4,5,6,7,11]
index = [1,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

# Load data
Ys = { }
for level in levels:
	Ys[level] = np.loadtxt('sweep3_level%d_v22.output' % level)


fig, axes = plt.subplots(4,4,figsize = (12,12))
for qoi, ax in zip(index, axes.flatten()):
	arm = np.nan*np.zeros( (len(levels), len(levels)))
	for (i, l1), (j, l2) in product(enumerate(levels), enumerate(levels)):
		if i <= j:
			yi = Ys[l1][:,qoi]
			yj = Ys[l2][:,qoi]
			# find valid indices
			I = np.isfinite(yi) & np.isfinite(yj) & (yi >= 0.) & (yj >= 0.)
			fmax = max(np.nanmax(yi[I]), np.nanmax(yj[I]))
			fmin = min(np.nanmin(yi[I]), np.nanmin(yj[I]))
	
			# Average relative mismatch		
			arm[i,j] = np.linalg.norm(yi[I] - yj[I],1)/np.sum(I)/(fmax - fmin)
			#arm[i,j] = np.linalg.norm(yi[I] - yj[I],np.inf)/(fmax - fmin)
	
	sns.heatmap(arm, annot = True, fmt = '2.2f', 
			linewidth = 0.5, ax = ax, cbar = False, vmin = 0, vmax = 1, cmap = 'Blues', square = True, 
			annot_kws={"size": 8})
	ax.yaxis.tick_left()
	ax.xaxis.tick_top()
	ax.set_title(qoi_names[qoi], y = 1.1) 
	ax.set_xticklabels(levels)
	ax.set_yticklabels(levels)
fig.tight_layout()
plt.savefig('tab_corr_arm.png', dpi = 300)
plt.show()	
