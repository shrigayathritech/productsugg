import pandas as pd

def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise Exception("File not found. Please check the file path.")

def filter_data(data, user_attributes):
    user_attributes_series = pd.Series(user_attributes)
    conditions = (
        (data['Age'] == user_attributes_series['Age']) &
        (data['Income'] == user_attributes_series['Income']) &
        (data['Student'] == user_attributes_series['Student']) &
        (data['Credit_Rating'] == user_attributes_series['Credit_Rating'])
    )
    
    filtered_data = data[conditions]
    print("Conditions:\n", conditions)  # Debugging line
    print("Filtered Data:\n", filtered_data)  # Debugging line
    suggestions = filtered_data.to_dict(orient='records')
    
    return suggestions
