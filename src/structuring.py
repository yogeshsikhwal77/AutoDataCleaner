import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class DataStructurer:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def date_time(self,cyclic_month_cols):

        if cyclic_month_cols is None:
            cyclic_month_cols =[]
        

        for col in cyclic_month_cols:
            if col in self.df.columns:
                print(f"found temporal feature/date column: {col}")

         
                self.df[col +'_sin'] = np.sin(2 * np.pi* self.df[col]/12)
                self.df[col +'_cos'] = np.cos(2 * np.pi* self.df[col]/12)
                self.df.drop(columns=[col],inplace = True)
                print(f"coverted '{col}' into cyclic sin/cos waves")
            else:
                print("temporal coloum not fouund in dataset")

        return self.df
        
    def feature_splitting(self,col1: str,col2:str,new_col:str,operation='add'):
        
        if col1 in self.df.columns and col2 in self.df.columns:
            if operation == 'multiply':
                self.df[new_col] = self.df[col1] * self.df[col2]
            elif operation == 'add':
                self.df[new_col] = self.df[col1] +  self.df[col2]

            print(f"synthesized new feture: {new_col}")
        else:
            print(f"skipping synthesis: coloumns '{col1}' or '{col2}' not found")
        return self.df

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

        structure.date_time('datacoloum')

        structure.feature_splitting('OverallQual','GrLivArea','QualXarea',operation='multiply')

        X_train,X_test,y_train,y_test = structure.split(target_column='SalePrice')

    except  FileNotFoundError :
        print("file not found")
    
    