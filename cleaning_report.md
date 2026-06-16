
=======================================================
Starting AUTO-DATA Cleaner Pipeline
=======================================================

[STEP 1] Loading data from data/raw/train.csv...
[Info] initial dataset shape = 891 rows,12 coumns

 [STEP 2] Inspecting and cleaning data...
Found 7 Number columns: ['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
Found 5 Text columns: ['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']
[INFO] No duplicate rows found.
[INFO] Found missing data in 3 columns. Applying median/mode imputation
Found 7 Number columns: ['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
Found 5 Text columns: ['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']
Found 7 Number columns: ['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
Found 5 Text columns: ['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']
[INFO] Outliers: Capped a total of 441 extreme values across numerical columns using the IQR method.
[INFO] clean dataset shape: 891 rows, 12 columns.
/n [STEP 3] Applying data transformations...
[INFO] categorical encoding; ordinal encoded  'Name' (891 unique values)
[INFO] categorical encoding: One hot encoded 'Sex' (2' unique values). 
[INFO] categorical encoding; ordinal encoded  'Ticket' (681 unique values)
[INFO] categorical encoding; ordinal encoded  'Cabin' (147 unique values)
[INFO] categorical encoding: One hot encoded 'Embarked' (3' unique values). 
[INFO] Log Transforming 'SibSp' (Skewness: 1.62) 
[INFO] Log Transforming 'Fare' (Skewness: 1.08) 
[INFO] Log Transforming 'Cabin' (Skewness: 2.32) 
/n [STEP 4] structuring and splitting data...
[INFO] Splitting dataset using Target column: Survived
[INFO] Training feature(X_train) :      PassengerId  Pclass  Name  ...  Sex_male  Embarked_Q  Embarked_S
331        332.0     1.0   331  ...      True       False        True
733        734.0     2.0   733  ...      True       False        True
382        383.0     3.0   382  ...      True       False        True
704        705.0     3.0   704  ...      True       False        True
813        814.0     3.0   813  ...     False       False        True
..           ...     ...   ...  ...       ...         ...         ...
106        107.0     3.0   106  ...     False       False        True
270        271.0     1.0   270  ...      True       False        True
860        861.0     3.0   860  ...      True       False        True
435        436.0     1.0   435  ...     False       False        True
102        103.0     1.0   102  ...      True       False        True

[712 rows x 12 columns]
[INFO] testing feature(X_test) :      PassengerId  Pclass  Name  ...  Sex_male  Embarked_Q  Embarked_S
709        710.0     3.0   709  ...      True       False       False
439        440.0     2.0   439  ...      True       False        True
840        841.0     3.0   840  ...      True       False        True
720        721.0     2.0   720  ...     False       False        True
39          40.0     3.0    39  ...     False       False       False
..           ...     ...   ...  ...       ...         ...         ...
433        434.0     3.0   433  ...      True       False        True
773        774.0     3.0   773  ...      True       False       False
25          26.0     3.0    25  ...     False       False        True
84          85.0     2.0    84  ...     False       False        True
10          11.0     3.0    10  ...     False       False        True

[179 rows x 12 columns]
[INFO] X_train shape: (712, 12) | X_test shape: (179, 12)

[STEP 5] Scaling Features...
[INFO] Fitting scaler on Training Data...
[INFO] feature splitting : fitting and applying standardscaler to 9 numerical features
[INFO] Applying fitted scaler to Testing Data...
[INFO] Feature Scaling: Applying pre-fitted StandardScaler to 9 numerical features.

[STEP 6] Saving Processed Data...
[INFO] Successfully saved X_train, X_test, y_train, y_test to 'data/processed/' directory.

=======================================================
Pipeline completed successfully in seconds 0.13489794731140137
=======================================================
