import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class DataStructurer:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def split(self , target_column: str,test_size = 0.2,random_state: int=42):
        if target_column not in self.df.columns:
            raise ValueError(f"Error: target column {target_column} not found in dataset")
        
        X = self.df.drop(columns=[target_column])
        y = self.df[target_column]
        
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=test_size,random_state=random_state)

        print(f"Training feature(X_train) : {X_train}")
        print(f"testing feature(X_test) : {X_test}")
        return X_train,X_test,y_train,y_test


### testing block

if __name__ == "__main__":
    try:
        fake_data = pd.read_csv('data/raw/train.csv')

        structure =DataStructurer(fake_data)

        X_train,X_test,y_train,y_test = structure.split(target_column='SalePrice')
    except  FileNotFoundError :
        print("file not found")
    
    