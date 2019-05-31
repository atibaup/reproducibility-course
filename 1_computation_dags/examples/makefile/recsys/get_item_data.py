""" get_item_data.py: [ Documentation here ] """
import pandas as pd
import numpy as np

def get_item_data(db_credentials):
	n_cols = 10
	return pd.DataFrame(np.random.rand(10, n_cols),
		columns=['col-%d' % i for i in range(n_cols)],
		index = range(10))


if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument('item_data_filename', type=str)
	args = parser.parse_args()
	data = get_item_data(None)
	data.to_parquet(args.item_data_filename)