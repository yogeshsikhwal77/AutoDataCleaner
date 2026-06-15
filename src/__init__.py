# src/__init__.py

# 1. Package Metadata
__version__ = "0.1.0"
__author__ = "yogeshsikhwal77" 

# 2. Expose Core Tools
# This allows users to import these directly from the 'src' folder
from .inspection import DataInspector
from .transformations import DataTransformer
from .structuring import DataStructurer
from .pipeline import run_auto_cleaner

# 3. Define __all__
# This restricts what gets imported if someone runs: `from src import *`
__all__ = [
    "DataInspector",
    "DataTransformer",
    "DataStructurer",
    "run_auto_cleaner"
]