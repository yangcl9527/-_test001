import json

def redata2():
    with open("D:\lianxi\data\data_2.json") as f:
        datalist = []
        data = json.load(f)
        for i in data:
            user_id = i.get("user_id")
            token = i.get("token")
            platform = i.get("platform")
            identity = i.get("identity")
            id = i.get("id")
            activity_id = i.get("activity_id")
            name = i.get("name")
            match_type = i.get("match_type")
            team_limit = i.get("team_limit")
            share_img = i.get("share_img")
            description = i.get("description")
            icon = i.get("icon")
            head = i.get("head")
            poster = i.get("poster")
            starttm = i.get("starttm")
            endtm = i.get("endtm")
            attend_num = i.get("attend_num")
            bonus_num = i.get("bonus_num")
            status = i.get("status")
            whether_participate = i.get("whether_participate")
            join_time = i.get("join_time")

            datalist.append((user_id, token, platform, identity, id, activity_id,
                             name, match_type,team_limit,share_img,description,icon,
                             head,poster,starttm,endtm,attend_num,bonus_num,status,whether_participate,join_time
                             ))
        return datalist


