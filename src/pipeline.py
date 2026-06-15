import pandas as pd 
import os

from inspection import DataInspector
from structuring import DataStructurer
from transformations import DataTransformer

def run_auto_cleaner(file_path: str,target_col: str):

    df = pd.read_csv(file_path)
    inspector = DataInspector(df)

    inspector.auto_column_detection()
    # inspector.histogram('LotArea')
    inspector.dublicaterowsdrop()
    inspector.handle_missing_value()
    inspector.handle_outliers()
    clean_df = inspector.df  # get the clean dataframe

    structure =DataStructurer(df)
    structure.date_time()
    structure.feature_splitting('OverallQual','GrLivArea','QualXarea',operation='multiply')
    X_train,X_test,y_train,y_test = structure.split(target_column='SalePrice')

    train_transformer = DataTransformer(X_train)
    train_transformer.encode_categorian()
    train_transformer.handle_skewness()
    X_train_clean = train_transformer.scale_featurs()

    test_transformer = DataTransformer(X_test)
    test_transformer.encode_categorian()
    test_transformer.handle_skewness()
    X_test_clean = test_transformer.scale_featurs()

    os.makedirs('data/processed',exist_ok = True)

    X_train_clean.to_csv('data/processed/X_train.csv', index=False)
    X_test_clean.to_csv('data/processed/X_test.csv', index=False)
    y_train.to_csv('data/processed/y_train.csv', index=False)
    y_test.to_csv('data/processed/y_test.csv', index=False)






if __name__ == '__main__':
    try:
        run_auto_cleaner(file_path = 'data/raw/train.csv',target_col = 'SalePrice')

    except Exception as e:
        print(f"Pipeline failed: {e}")