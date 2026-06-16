import pandas as pd 
import os
import sys
import time

from inspection import DataInspector
from structuring import DataStructurer
from transformations import DataTransformer

def run_auto_cleaner(file_path: str,target_col: str,months_cols=None):
    start_time = time.time()
    
    print("\n" + "="*55)
    print("Starting AUTO-DATA Cleaner Pipeline")
    print("="*55)
    
    print(f"\n[STEP 1] Loading data from {file_path}...")
    df = pd.read_csv(file_path)
    print(f"[Info] initial dataset shape = {df.shape[0]} rows,{df.shape[1]} coumns")

    print(f"\n [STEP 2] Inspecting and cleaning data...")
    inspector = DataInspector(df)

    inspector.auto_column_detection()
    # inspector.histogram('LotArea')
    inspector.dublicaterowsdrop()
    inspector.handle_missing_value()
    inspector.handle_outliers()
    clean_df = inspector.df  # get the clean dataframe
    print(f"[INFO] clean dataset shape: {clean_df.shape[0]} rows, {clean_df.shape[1]} columns.")

    print("/n [STEP 3] Applying data transformations...")

    transformer = DataTransformer(clean_df)
    transformer.encode_categorian()
    transformer.handle_skewness()

    encoded_df = transformer.df

    print("/n [STEP 4] structuring and splitting data...")
    structure =DataStructurer(encoded_df)
    structure.date_time(cyclic_month_cols=months_cols)
    # structure.feature_splitting('OverallQual','GrLivArea','QualXarea',operation='multiply')

    print(f"[INFO] Splitting dataset using Target column: {target_col}")
    X_train,X_test,y_train,y_test = structure.split(target_column=target_col)
    print(f"[INFO] X_train shape: {X_train.shape} | X_test shape: {X_test.shape}")

    print("\n[STEP 5] Scaling Features...")
    print("[INFO] Fitting scaler on Training Data...")
    train_transformer = DataTransformer(X_train)
    X_train_clean,saved_scaler = train_transformer.scale_featurs(fitted_scaler=None)

    print("[INFO] Applying fitted scaler to Testing Data...")
    test_transformer = DataTransformer(X_test)
    X_test_clean = test_transformer.scale_featurs(fitted_scaler=saved_scaler)

    print("\n[STEP 6] Saving Processed Data...")
    os.makedirs('data/processed',exist_ok = True)

    X_train_clean.to_csv('data/processed/X_train.csv', index=False)
    X_test_clean.to_csv('data/processed/X_test.csv', index=False)
    y_train.to_csv('data/processed/y_train.csv', index=False)
    y_test.to_csv('data/processed/y_test.csv', index=False)

    print("[INFO] Successfully saved X_train, X_test, y_train, y_test to 'data/processed/' directory.")

    end_time = time.time()
    print("\n" + "="*55)
    print("Pipeline completed successfully in seconds",end_time-start_time)
    print("="*55)






if __name__ == '__main__':

    log_filename = 'cleaning_report.md'
    try:
        with open(log_filename, 'w',encoding='utf-8') as log_file:
            original_stdout = sys.stdout
            sys.stdout = log_file
            run_auto_cleaner(file_path = 'data/raw/train.csv',
                             target_col = 'Survived',
                             months_cols=[]
            )

            sys.stdout = original_stdout

            print(f" Processing complete : Open {log_filename} to see the full data report.")

    except Exception as e:
        sys.stdout = getattr(sys,'__stdout__',sys.stdout)
        print(f"Pipeline failed: {e}")