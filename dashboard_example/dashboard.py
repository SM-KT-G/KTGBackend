data = {'users': 150, 'revenue': 4500, 'active_sessions': 12}

def display_dashboard(metrics):
    print('--- Dashboard Metrics ---')
    for key, value in metrics.items():
        print(f'{key.capitalize()}: {value}')

if __name__ == '__main__':
    display_dashboard(data)