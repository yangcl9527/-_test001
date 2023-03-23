import json

def redata1():
    with open("D:\lianxi\data\data_1.json") as f:
        datalist = []
        data = json.load(f)
        for i in data:
            user_id = i.get("user_id")
            token = i.get("token")
            platform = i.get("platform")
            identity = i.get("identity")
            match_type_1 = i.get("match_type_1")
            cl = i.get("cl")
            match_type = i.get("match_type")
            datalist.append((user_id, token, platform, identity, match_type_1, cl, match_type))
        return datalist
