import numpy as np
import matplotlib.pyplot as plt
import itertools
from sequoia import *

levels = [0,2,5,11]
index = [0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

kwargs = itertools.cycle( (
	{'marker': '.', 'markersize': 4},
	{'marker': '+', 'markersize': 4},
	{'marker': 'x', 'markersize': 4},
	{'marker': 'o', 'markersize': 4, 'mfc' : 'none'}))


Ys = []
for level in levels:
	Ys.append(np.loadtxt('sweep3_level%d_v19.output' % level ))


for k in range(0,50):
	I = np.arange(20*k, 20*(k+1))

	fig, axes = plt.subplots(4,4, figsize = (9,9))
	for ax, i in zip(axes.flatten(), index):
		ax.set_title(qoi_names[i])
		for Y, level in zip(Ys, levels):
			ax.plot(Y[I,i], linestyle = 'None', label = level_names[level], **kwargs.next())
		if i == 3:
			pass
			#ax.set_ylim(bottom = 0, top = 60e3)
		#ax.set_ylim(bottom = np.min(Ys[0][I,i]), top = np.max(Ys[0][I,i]))
		ax.get_xaxis().set_ticks([])	

	fig.tight_layout(rect = [0,0.15,1,1])
	fhandles, flabels = axes[0,0].get_legend_handles_labels()
	plt.legend(fhandles, [level_names[i] for i in levels],
			loc='upper right', bbox_to_anchor=(0.5, -0.3))

	fig.savefig('sweep3_%02d.png' % k, dpi = 300)
	plt.close(fig)
	print "sweep3 %d done" % k