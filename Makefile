prepare_stage1:
	python3 src/Data/Separate_reactants.py

prepare_stage2:
	python3 src/Data/Encode_formulas.py

data_prepare: prepare_stage1 prepare_stage2

training:
	python3 src/models/Prediction_model.py