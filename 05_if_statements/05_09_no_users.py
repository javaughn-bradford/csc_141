#05_10_checking_usernames
current_users = ['javaughn', 'charlie', 'walter', 'chris', 'bob']
new_users = ['javaughn', 'tiger', 'chris', 'bobby', 'tim']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")
