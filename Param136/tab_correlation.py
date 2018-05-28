import numpy as np
import matplotlib.pyplot as plt
from itertools import product
import seaborn as sns
from scipy.stats import pearsonr
from ridgeduu import clean_data
from sequoia import *

################################################################################
# Step 1: Form the domains
################################################################################
# Construct the domains for this problem 
from multifDomains3D import *
design_domain = buildDesignDomain(output = None)

# Clip -- truncate infinite domains at clip-standard deviations
random_domain = buildRandomDomain(clip = 3.)

# Form the combined domain
total_domain = design_domain + random_domain


################################################################################
# Step 2: Sample the domain
# Here we load data previously generated 
################################################################################

show_levels = [0,2,5,11]

level = 11
version = 13
step = 'e'

# This data comes from randomly sampling the domain
X_list = [np.loadtxt('uniform1.input'), ]

Y_list = [list([]) for i in show_levels] 
for i, slevel in enumerate(show_levels):
	Y_list[i].append(np.loadtxt('uniform1_level%d_v%d.output' % (slevel, version)))
print "loaded uniform samples"

for old_step in [chr(x) for x in range(ord('a'), ord(step))]:
	X_list.append(np.loadtxt('extend1%s_l%d_v%d.input' % (old_step, level, version)))
	for i, slevel in enumerate(show_levels):
		Y_list[i].append(np.loadtxt('extend1%s_l%d_v%d_level%d_v%d.output' % (old_step, level, version, slevel, version)))
	print "loaded step %s" % old_step

X = np.vstack(X_list)
X_norm = total_domain.normalize(X)

Ys = [np.vstack(Y_list[i]) for i in range(len(show_levels))]

################################################################################
# Step 3: Compute correlation
################################################################################
index = [0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

corr = np.nan*np.ones( (len(show_levels),len(show_levels)))
fig, axes = plt.subplots(4,4, figsize = (12,12))

for qoi, ax in zip(index, axes.flatten()):
	for i,j in product(range(len(show_levels)), repeat =2):
		l1 = show_levels[i]
		l2 = show_levels[j]
		corr[i,i] = 1.
		if l1 < l2:
			# Find valid points in each set
			I = clean_data(Ys[i][:,qoi]) & clean_data(Ys[j][:,qoi])
			corr[i,j] = pearsonr(Ys[i][I,qoi].flatten(), Ys[j][I,qoi].flatten())[0]

	sns.heatmap(corr, annot = True, fmt = '2.2f', linewidth = 0.5, ax = ax, cbar = False, vmin = -1, vmax = 1, cmap = 'RdBu_r', square = True)
	ax.set_title(qoi_names[qoi], y = 1.1)
	ax.yaxis.tick_right()
	ax.xaxis.tick_top()
	ax.set_xticklabels(show_levels)
	ax.set_yticklabels(show_levels[::-1])
fig.tight_layout()
plt.savefig('tab_correlation.png')
plt.show()



