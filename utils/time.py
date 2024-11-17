from datetime import datetime

def get_formatted_datetime():
    # Get the current date and time
    current_datetime = datetime.now()
    # Format the date and time
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime

# Example usage
#print(get_formatted_datetime())