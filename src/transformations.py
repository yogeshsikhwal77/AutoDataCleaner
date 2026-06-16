import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataTransformer:
    def __init__(self,df: pd.DataFrame):
        self.df = df.copy()

    def encode_categorian(self):
        text_columns = self.df.select_dtypes(exclude=np.number).columns.tolist()

        if not text_columns:
            print("[Info] no categorical columns found to encode")
        for col in text_columns:
            unique = self.df[col].nunique()
            if unique < 10 :
                print(f"[INFO] categorical encoding: One hot encoded '{col}' ({unique}' unique values). ")
                self.df = pd.get_dummies(self.df,columns=[col],drop_first=True)
            else :
                print(f"[INFO] categorical encoding; ordinal encoded  '{col}' ({unique} unique values)")
                self.df[col] = pd.factorize(self.df[col])[0]
        return self.df
                
    def handle_skewness(self):
        num_cols = self.df.select_dtypes(include=np.number).columns.tolist()
        
        transformed_count = 0
        for col in num_cols:
            skewness = self.df[col].skew()
            if skewness >1 or skewness < -1 :
                if self.df[col].min() >= 0 :
                    print(f"[INFO] Log Transforming '{col}' (Skewness: {skewness:.2f}) " )
                    self.df[col] = np.log1p(self.df[col])
                    transformed_count += 1
                else:
                    print(f"[Warning] skewness correction skipped for {col} (skewness = {skewness} ) because it contain negative values")
        if transformed_count == 0:
            print(f"[INFO] skewness correction: No highly skewed positive numerical colums found")
        return self.df
    
    def scale_featurs(self,fitted_scaler=None):
        num_col = self.df.select_dtypes(include=np.number).columns.tolist()
        num_col_only = [col for col in num_col if self.df[col].dtype != 'bool']

        if fitted_scaler is None:
            print(f"[INFO] feature splitting : fitting and applying standardscaler to {len(num_col_only)} numerical features")
            scaler = StandardScaler()
            self.df[num_col_only] = scaler.fit_transform(self.df[num_col_only])
            return self.df,scaler
        else:
            print(f"[INFO] Feature Scaling: Applying pre-fitted StandardScaler to {len(num_col_only)} numerical features.")
            self.df[num_col_only] = fitted_scaler.transform(self.df[num_col_only])
            return self.df

    

    
if __name__ == "__main__":
    try:
        fake_data = pd.read_csv('data/raw/train.csv')
        transformer = DataTransformer(fake_data)

        transformer.encode_categorian()
        transformer.handle_skewness()
        transformer.scale_featurs()


    except FileNotFoundError:
        print("File not found")

