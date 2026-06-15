import pandas as pd 
import os

from inspection import DataInspector
from structuring import DataStructurer
from transformations import DataTransformer

def run_auto_cleaner(file_path: str,target_col: str,months_cols=None):

    df = pd.read_csv(file_path)
    inspector = DataInspector(df)

    inspector.auto_column_detection()
    # inspector.histogram('LotArea')
    inspector.dublicaterowsdrop()
    inspector.handle_missing_value()
    inspector.handle_outliers()
    clean_df = inspector.df  # get the clean dataframe

    transformer = DataTransformer(clean_df)
    transformer.encode_categorian()
    transformer.handle_skewness()

    encoded_df = transformer.df

    structure =DataStructurer(encoded_df)
    structure.date_time(cyclic_month_cols=months_cols)
    # structure.feature_splitting('OverallQual','GrLivArea','QualXarea',operation='multiply')
    X_train,X_test,y_train,y_test = structure.split(target_column=target_col)

    train_transformer = DataTransformer(X_train)
    X_train_clean,saved_scaler = train_transformer.scale_featurs(fitted_scaler=None)

    test_transformer = DataTransformer(X_test)
    X_test_clean = test_transformer.scale_featurs(fitted_scaler=saved_scaler)

    os.makedirs('data/processed',exist_ok = True)

    X_train_clean.to_csv('data/processed/X_train.csv', index=False)
    X_test_clean.to_csv('data/processed/X_test.csv', index=False)
    y_train.to_csv('data/processed/y_train.csv', index=False)
    y_test.to_csv('data/processed/y_test.csv', index=False)






if __name__ == '__main__':
    try:
        run_auto_cleaner(file_path = 'data/raw/train.csv',
                         target_col = 'SalePrice',
                         months_cols=[]
        )

    except Exception as e:
        print(f"Pipeline failed: {e}")