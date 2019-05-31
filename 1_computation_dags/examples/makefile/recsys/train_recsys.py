""" train_recsys.py: [ Documentation here ] """
import pandas as pd
import joblib

def train_recsys_model(u2i):
	from sklearn.decomposition import NMF
	model = NMF().fit(u2i)
	return model

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('u2i_filename', type=str)
    parser.add_argument('model_filename', type=str)

    args = parser.parse_args()

    u2i = pd.read_parquet(args.u2i_filename)
    model = train_recsys_model(u2i)
    joblib.dump(model, args.model_filename)