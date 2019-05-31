""" build_u2i_matrix.py: [ Documentation here ] """
import pandas as pd

def build_u2i_matrix(u, i):
	return u.merge(i, left_index=True, right_index=True)

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument('item_data_filename', type=str)
	parser.add_argument('user_data_filename', type=str)
	parser.add_argument('u2i_filename', type=str)

	args = parser.parse_args()

	user = pd.read_parquet(args.user_data_filename)
	item = pd.read_parquet(args.item_data_filename)
	u2i = build_u2i_matrix(user, item)

	u2i.to_parquet(args.u2i_filename)