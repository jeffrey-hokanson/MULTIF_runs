level_names = ["NONIDEALNOZZLE,1e-8,AEROTHERMOSTRUCTURAL,LINEAR,0.5",
		 "NONIDEALNOZZLE,1e-8,AEROTHERMOSTRUCTURAL,NONLINEAR,0.5",
		"EULER,2D,COARSE,AEROTHERMOSTRUCTURAL,LINEAR,0.5",
		"EULER,2D,MEDIUM,AEROTHERMOSTRUCTURAL,LINEAR,0.5",
		"EULER,2D,FINE,AEROTHERMOSTRUCTURAL,LINEAR,0.5",
		"EULER,3D,COARSE,AEROTHERMOSTRUCTURAL,LINEAR,0.5",
		"EULER,3D,MEDIUM,AEROTHERMOSTRUCTURAL,LINEAR,0.5",
		"EULER,3D,FINE,AEROTHERMOSTRUCTURAL,LINEAR,0.5",
		"RANS,2D,COARSE,AEROTHERMOSTRUCTURAL,LINEAR,0.5",
		"RANS,2D,MEDIUM,AEROTHERMOSTRUCTURAL,LINEAR,0.5",
		"RANS,2D,FINE,AEROTHERMOSTRUCTURAL,LINEAR,0.5",
		"RANS,3D,COARSE,AEROTHERMOSTRUCTURAL,LINEAR,0.5",
		"RANS,3D,MEDIUM,AEROTHERMOSTRUCTURAL,LINEAR,0.5",
		"RANS,3D,FINE,AEROTHERMOSTRUCTURAL,LINEAR,0.5"
	]

qoi_names = ['Mass',
		 'MASS_WALL_ONLY',
		 'VOLUME', # 2
		 'Thrust', 
		 'Thermal temp failure', # 4
		 'Load inside temp failure',
		 'Load middle temp failure', # 6
		 'Load outside temp failure',
		 'Thermal layer failure', # 8
		 'Load inside failure',
		 'Load middle failure', # 10
		 'Load outside failure',
		 'Stringer failure', # 12
		 'Baffle 1 failure',
		 'Baffle 2 failure',# 14
		 'Baffle 3 failure',
		 'Baffle 4 failure',# 16
		 'Baffle 5 failure',
		 'THERMAL_LAYER_TEMP_RATIO',# 18
		 'LOAD_LAYER_INSIDE_TEMP_RATIO',
		 'LOAD_LAYER_MIDDLE_TEMP_RATIO',# 20
		 'LOAD_LAYER_OUTSIDE_TEMP_RATIO',
		 'THERMAL_LAYER_FAILURE_CRITERIA',# 22
		 'LOAD_LAYER_INSIDE_FAILURE_CRITERIA',
		 'LOAD_LAYER_MIDDLE_FAILURE_CRITERIA',# 24
		 'LOAD_LAYER_OUTSIDE_FAILURE_CRITERIA',
		 'WALL_PRESSURE',# 26
		 'PRESSURE',
		 'VELOCITY' # 28
		]