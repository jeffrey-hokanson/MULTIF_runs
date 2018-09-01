import numpy as np
import matplotlib.pyplot as plt
import itertools
from sequoia import *

level = 11
index = [1,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

#index = [1,4,20,21,22,23,24,25,26,27,28,29,30,31,32,32,34,35]


Ys = []
Ys.append(np.loadtxt('sweep3_level%d_v25.output' % level ))
for sst in ['sstc1', 'sstc2', 'sstc3', 'sstp1c1','sstp1c2']:
	Ys.append(np.loadtxt('sweep3_level%d_%s_v25.output' % (level, sst)))


for k in range(0,1):
	I = np.arange(20*k, 20*(k+1))

	fig, axes = plt.subplots(4,4, figsize = (9,9))
	for ax, i in zip(axes.flatten(), index):
		ax.set_title(qoi_names[i], fontsize = 10)
		for j in I:
			ax.plot([j,j], [np.min([Y[j,i] for Y in Ys]), np.max([Y[j,i] for Y in Ys])], 'k-', linewidth = 0.5, alpha = 0.5)
		
		ax.plot(Ys[0][I,i], linestyle = 'None', marker = '_', markersize = 6, color = 'k')
		
		for Y in Ys:
			ax.plot(Y[I,i], linestyle = 'None', marker = '.', markersize = 4)
		
		
	
		ax.get_xaxis().set_ticks([])
		bottom = min([np.nanmin(Y[:,i]) for Y in Ys])
		bottom = max([bottom, 0]) 
		top    = max([np.nanmax(Y[:,i]) for Y in Ys])
		ax.set_ylim(bottom = bottom, top = top)

	fig.tight_layout(rect = [0,0.15,1,1])
	fhandles, flabels = axes[0,0].get_legend_handles_labels()

	fig.savefig('sweep3_sst_%02d.png' % k, dpi = 300)
	plt.close(fig)
	print "sweep3 %d done" % k
