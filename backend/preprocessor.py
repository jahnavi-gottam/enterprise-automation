def preprocess_data(data):
    # Ensure data is a dictionary
    if not isinstance(data, dict):
        raise ValueError("Data must be a dictionary")

    # Example of required fields
    required_fields = ['name', 'email', 'age']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")

    # Return the validated data
    return data
