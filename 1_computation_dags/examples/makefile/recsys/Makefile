.data_folder_done:
	mkdir -pv data
	touch .data_folder_done

.artifacts_folder_done:
	mkdir -pv artifacts
	touch .artifacts_folder_done

data/u.parquet: get_user_data.py .data_folder_done
	python get_user_data.py data/u.parquet

data/i.parquet: get_item_data.py .data_folder_done
	python get_item_data.py data/i.parquet

data/u2i.parquet: build_u2i_matrix.py data/u.parquet data/i.parquet
	python build_u2i_matrix.py data/u.parquet data/i.parquet data/u2i.parquet

artifacts/model.pkl: train_recsys.py data/u2i.parquet .artifacts_folder_done
	python train_recsys.py data/u2i.parquet artifacts/model.pkl

.PHONY: recsys
recsys: artifacts/model.pkl

.PHONY: clean
clean:
	rm -Rf data
	rm -Rf artifacts
	rm .artifacts_folder_done
	rm .data_folder_done

.DEFAULT_GOAL := recsys