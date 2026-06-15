import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataTransformer:
    def __init__(self,df: pd.DataFrame):
        self.df = df.copy()

    def encode_categorian(self):
        text_columns = self.df.select_dtypes(exclude=np.number).columns.tolist()
        for col in text_columns:
            unique = self.df[col].nunique()
            if unique < 10 :
                print(f"One hot encoding:'{unique}' unique values ")
                self.df = pd.get_dummies(self.df,columns=[col],drop_first=True)
            else :
                print(f"ordinal encoding '{col} ({unique} unique values)")
                self.df[col] = pd.factorize(self.df[col])[0]
        return self.df
                
    def handle_skewness(self):
        num_cols = self.df.select_dtypes(include=np.number).columns.tolist()

        for col in num_cols:
            skewness = self.df[col].skew()
            if skewness >1 or skewness < -1 :
                if self.df[col].min() >= 0 :
                    print(f"Log Transforming '{col}' (Skewness: {skewness:.2f}) " )
                    self.df[col] = np.log1p(self.df[col])

        return self.df
    
    def scale_featurs(self):
        num_col = self.df.select_dtypes(include=np.number).columns.tolist()
        scaler = StandardScaler()

        num_col_only = [col for col in num_col if self.df[col].dtype != 'bool']

        self.df[num_col_only] = scaler.fit_transform(self.df[num_col_only])

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

