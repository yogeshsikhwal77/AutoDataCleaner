import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class DataInspector:
    def __init__ (self , df: pd.DataFrame):
        self.df = df.copy()

    def auto_column_detection(self):
        # Auto detect data types

        num_cols = self.df.select_dtypes(include = np.number).columns.tolist()
        text_cols = self.df.select_dtypes(exclude = np.number).columns.tolist()

        print(f"Found {len(num_cols)} Number columns: {num_cols}")
        print(f"Found {len(text_cols)} Number columns: {text_cols}")
        return num_cols,text_cols

    def histogram(self, column_name):
        if column_name in self.df.select_dtypes(include=np.number).columns:
           print(f"Plotting histogram for {column_name}")
           plt.figure(figsize=(8,5))
           sns.histplot(data = self.df ,x=column_name,kde = True,color='red')
           plt.title(f"Distribution of {column_name}")
           plt.xlabel(column_name)
           plt.ylabel("Frequency")
           plt.show()

        else:
            print("error : column not found or a column is not numerical")

    def dublicaterowsdrop(self):
        initial_row = len(self.df)
        self.df.drop_duplicates(inplace=True)
        final_row = len(self.df)
        print("Total row dropped :" , initial_row-final_row)
        return self.df
    
    def handle_missing_value(self):
        print(self.df.isnull().sum())
        num_cols , cat_cols = self.auto_column_detection()
        for col in num_cols:
            if self.df[col].isnull().sum() > 0:
                self.df[col] = self.df[col].fillna(self.df[col].median())

        for col in cat_cols:
            if self.df[col].isnull().sum() > 0:
                mode_vals = self.df[col].mode()
                if not mode_vals.empty:
                    self.df[col] = self.df[col].fillna(mode_vals[0])
                else:
                    self.df.drop(columns=[col],inplace=True)

        return self.df
    
    def handle_outliers(self):
        num_cols , cat_cols = self.auto_column_detection()
        outlier_capped = 0
        for col in num_cols:
            p_25 = self.df[col].quantile(0.25)
            p_75 = self.df[col].quantile(0.75)
            iqr = p_75 - p_25
            upper_bound = p_75 + 1.5 * iqr
            lower_bound = p_25 - 1.5 * iqr

            outliers = ((self.df[col] < lower_bound) | (self.df[col] > upper_bound)).sum()
            outlier_capped += outliers

            self.df[col] = np.where(
                self.df[col] > upper_bound,
                upper_bound,
                np.where(
                    self.df[col] < lower_bound,
                    lower_bound,
                    self.df[col]
                )
            )

        print(f"Total Outlier detect: ",outlier_capped)
        return self.df


# TESTING BLOCK
if __name__ == "__main__":

    try:
        fake_data = pd.read_csv('data/raw/train.csv')
        inspector = DataInspector(fake_data)
        inspector.auto_column_detection()
        # inspector.histogram('LotArea')
        inspector.dublicaterowsdrop()
        inspector.handle_missing_value()
        inspector.handle_outliers()
    except FileNotFoundError:
        print("Please add the file")