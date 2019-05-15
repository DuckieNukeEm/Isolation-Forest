import pandas as pd
from iForest import *
import line_profiler 

if __name__ == '__main__':
	df = pd.read_csv('../Kaggle_SCTP/Data/train.csv', nrows = 2000)
	df.drop(columns = ['ID_code','target'], inplace = True)
	
	iforest = iForest(df, 500, 256)
	
	tt = predict_iForest(df, iforest, 256)

	print(tt.describe())
