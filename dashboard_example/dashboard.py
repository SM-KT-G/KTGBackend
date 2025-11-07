data = {'users': 150, 'revenue': 4500, 'active_sessions': 12}

def display_dashboard(metrics):
    """Prints the dashboard metrics."""
    print('=== KT&G Simple Dashboard ===')
    print(f"Total Users: {metrics['users']}")
    print(f"Revenue: ${metrics['revenue']}")
    print(f"Active: {metrics['active_sessions']}")
    print('---------------------------')

if __name__ == '__main__':
    display_dashboard(data)