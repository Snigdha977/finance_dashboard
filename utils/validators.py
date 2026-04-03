def validate_record(data):
    required = ['amount', 'type', 'category']
    return all(field in data for field in required)


def validate_user(data):
    return 'name' in data and 'role' in data
