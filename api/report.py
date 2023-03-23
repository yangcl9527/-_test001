import requests
from data import redata_1

def geturl1(id, token, platform, identity, match_type, cl):
    url = "http://paps.funshion.com/v1/applet/bonusactivities?user_id={id}&token={token}&platform={platform}&identity={identity}&cl={cl}&match_type={match_type}".format(id=id,token=token,platform=platform,identity=identity,cl= cl,match_type=match_type)
    respones = requests.get(url=url)
    return respones


def geturl2(user_id, token, platform, identity, id):
    url = "http://paps.funshion.com/v1/applet/bonusactivity?user_id={user_id}&token={token}&platform={platform}&identity={identity}&id={id}".format(user_id=user_id,token=token,platform=platform,identity=identity,id=id)
    resource = requests.get(url=url)
    return resource
