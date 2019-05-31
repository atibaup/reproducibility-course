def task_create_data_folder():
	"""Creates the folder where data will be stored"""
	return {
        'targets': ['data/'],
        'actions': ['mkdir -pv data'],
	}

def task_create_artifacts_folder():
	"""Creates the folder where artifacts will be stored"""
	return {
        'targets': ['artifacts/'],
        'actions': ['mkdir -pv artifacts'],
	}

def task_get_user_data():
	"""Retrieves user data and stores it"""
	return {
		'file_dep': ['get_user_data.py'],
		'task_dep': ['create_data_folder'],
        'targets': ['data/u.parquet'],
        'actions': ['python get_user_data.py %(targets)s'],
	}

def task_get_item_data():
	"""Retrieves item data and stores it"""
	return {
		'file_dep': ['get_item_data.py'],
        'task_dep': ['create_data_folder'],
        'targets': ['data/i.parquet'],
        'actions': ['python get_item_data.py %(targets)s'],
	}

def task_build_u2i_matrix():
	"""Builds user to item matrix"""
	return {
		'file_dep': ['build_u2i_matrix.py', 'data/u.parquet', 'data/i.parquet',],
        'targets': ['data/u2i.parquet'],
        'actions': ['python build_u2i_matrix.py data/u.parquet data/i.parquet %(targets)s'],
	}

def task_recsys():
	"""Trains and persists recsys model"""
	return {
		'file_dep': ['train_recsys.py', 'data/u2i.parquet', ],
        'targets': ['artifacts/model.pkl'],
        'actions': ['python train_recsys.py data/u2i.parquet %(targets)s'],
	}

