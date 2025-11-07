data = {'users': 150, 'revenue': 4500, 'active_sessions': 12}

def display_dashboard(metrics):
    """Prints the dashboard metrics."""
    print('=== KT&G Simple Dashboard ===')
    for key, value in metrics.items():
        print(f'{key.capitalize()}: {value}')

if __name__ == '__main__':
    display_dashboard(data)