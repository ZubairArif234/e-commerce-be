import numpy as np

def convert_to_python_type(value):
    
    if isinstance(value, np.ndarray):
        return value.tolist()  # Convert NumPy array to Python list
    elif isinstance(value, np.generic):
        return value.item()  # Convert NumPy scalar to Python scalar
    return value