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

def find_users_with_valid_data(data):
    """
    this makes me wanna throw up
     Ideally I would read these requirements from a config
     but I wanna get this question done and I don't wanna fuck with getting that working
     in case future me or someone else wants to do this for fun:
        - store format as a csv with
            field,min,max,format(regex pattern)
        read these into a dict and then compare all the user data
     """
    valid_users = []
    for user in data:
        #validate the years first
        if len(user["byr"]) > 4:
            continue
        if int(user["byr"]) < 1920 or int(user["byr"]) > 2002:
            continue
        if len(user["iyr"]) > 4:
            continue
        if int(user["iyr"]) < 2010 or int(user["iyr"]) > 2020:
            continue
        if len(user["eyr"]) > 4:
            continue
        if int(user["eyr"]) < 2020 or int(user["iyr"]) > 2030:
            continue

        # check that the height has a valid unit and value
        height_unit = re.findall("[A-Za-z]+", user["hgt"])
        height_val = re.findall("[\d]+", user["hgt"])
        try:
            if height_unit[0] == "in":
                if int(height_val[0]) < 59 or int(height_val[0]) > 76:
                    continue
            elif height_unit[0] == "cm":
                if int(height_val[0]) < 150 or int(height_val[0]) > 193:
                    continue
            else:
                continue
        except IndexError:
            continue

        # check hair color
        if not bool(re.search("#([\d]|[a-f]){6}", user["hcl"])):
            continue
        # eye color
        if not bool(re.search("(amb|blu|brn|gry|grn|hzl|oth)", user["ecl"])):
            continue
        # PID has 9 digits
        if not bool(re.search("[\d]{9}", user["pid"])):
            continue
        valid_users.append(user)
    return valid_users



batch_path = sys.argv[1]
reqs_path = sys.argv[2]
data = get_data(batch_path)
reqs = get_reqs(reqs_path)
good_fields = find_users_with_required_fields(data, reqs)
valid = find_users_with_valid_data(good_fields)
for user in valid:
    print(user)
print("There are {0} valid users".format(len(valid)))
