# Roadrecon MFA users
Parser of [Roadrecon](https://github.com/dirkjanm/ROADtools) results looking to enabled MFA for all the users. The script will produce two files:
- `results_users.csv` with all the users with information about enabled/disabled MFA
- `results_roles.csv` with all the users with information about enabled/disabled MFA organized by role

# Execution
Run the following command:
```bash
python roadrecon_mfa_users.py
```

Then, when the application prompts the information, insert the URL of your running Roadrecon server.