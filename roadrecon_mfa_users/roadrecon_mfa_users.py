import requests
import json

def mfa_users(address):
    response = requests.get(f'{address}/api/users')
    json_data = json.loads(response.text)

    with open('results_users.csv', 'w', encoding="utf-8") as f:
        f.write(';'.join(list(json_data[0].keys())))
        f.write('\n')

        for x in json_data:
            keys = list(x.keys())
            for k in keys[:-1]:
                if k == "strongAuthenticationDetail":
                    if x[k]["methods"]:
                        for method in x[k]["methods"][:-1]:
                            f.write(f"{method['methodType']},")

                        f.write(f"{method['methodType']};")
                    else:
                        f.write('NONE;')

                else:
                    f.write(f'{x[k]};')
            
            f.write(f'{x[keys[-1]]}\n')


def mfa_users_by_role(address):
    response = requests.get(f'{address}/api/roledefinitions')
    json_data = json.loads(response.text)

    with open('results_roles.csv', 'w', encoding="utf-8") as f:
        for role in json_data:
            for user in role['assignments']:
                keys = list(user['principal'].keys())

                if "appDisplayName" not in keys:
                    for k in keys:
                        if k == "strongAuthenticationDetail":
                            if user['principal'][k]["methods"]:
                                for method in user['principal'][k]["methods"][:-1]:
                                    f.write(f"{method['methodType']},")

                                f.write(f"{method['methodType']};")
                            else:
                                f.write('NONE;')

                        else:
                            f.write(f"{user['principal'][k]};")
                                                
                    f.write(f"{role['displayName']}\n")
                    print(role['displayName'])
                

def main():
    ADDRESS = input("Insert the URL of the Roadrecon tool (e.g. http://127.0.0.1:5000):\n")

    mfa_users(ADDRESS)
    mfa_users_by_role(ADDRESS)

if __name__=="__main__":
    main()