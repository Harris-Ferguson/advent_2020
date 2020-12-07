import sys
import re

def make_user(user_string):
    data = {}
    matches = re.findall("[A-Za-z]+:[^\s]+", user_string)
    for match in matches:
        keyval = re.split("[:]", match)
        data[keyval[0]] = keyval[1]
    return data

def get_data(path):
    data = []
    with open(path) as f:
        content = f.readlines()
        user_string = ''
        for line in content:
            if line != '\n':
                user_string += line
            elif line == '\n':
                data.append(make_user(user_string))
                user_string = ''
    data.append(make_user(user_string))
    return data

def get_reqs(path):
    with open(path) as f:
        return [line.replace("\n", '') for line in f]

def find_users_with_required_fields(data, reqs):
    valid_users = []
    for user in data:
        valid = True
        for req in reqs:
            if req not in user:
                valid = False
        if valid:
            valid_users.append(user)
    return valid_users

batch_path = sys.argv[1]
reqs_path = sys.argv[2]
data = get_data(batch_path)
for user in data:
    print(user)
reqs = get_reqs(reqs_path)
valid = find_users_with_required_fields(data, reqs)
print("There are {0} valid users".format(len(valid)))
