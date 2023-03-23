#coding:UTF-8

import unittest
from parameterized import parameterized
from api import report
from data.redata_1 import redata1
from data.redata_2 import redata2


class Test001(unittest.TestCase):
    def setUp(self):
        self.geturl1 = report.geturl1
        self.geturl2 = report.geturl2

    # 列表接口
    @parameterized.expand(redata1())
    def test01(self, user_id, token, platform, identity, match_type_1, cl,match_type):
        response = self.geturl1(user_id, token, platform, identity, match_type_1, cl)
        self.assertEqual(match_type, response.json().get("data")[0].get("match_type"))

    # 详情接口
    @parameterized.expand(redata2())
    def test02(self,user_id, token,platform,identity,id,activity_id,
               name,match_type,team_limit,share_img,description,icon,
                             head,poster,starttm,endtm,attend_num,bonus_num,status,whether_participate,join_time
               ):
        response = self.geturl2(user_id, token, platform, identity, id)
        self.assertEqual(activity_id, response.json().get("data").get("activity_id"))
        self.assertEqual(match_type, response.json().get("data").get("match_type"))
        self.assertEqual(name, response.json().get("data").get("name"))
        self.assertEqual(team_limit, response.json().get("data").get("team_limit"))
        self.assertEqual(share_img, response.json().get("data").get("share_img"))
        self.assertEqual(description, response.json().get("data").get("description"))
        self.assertEqual(icon, response.json().get("data").get("icon"))
        self.assertEqual(head, response.json().get("data").get("head"))
        self.assertEqual(poster, response.json().get("data").get("poster"))
        self.assertEqual(starttm, response.json().get("data").get("starttm"))
        self.assertEqual(endtm, response.json().get("data").get("endtm"))
        self.assertEqual(attend_num, response.json().get("data").get("attend_num"))
        self.assertEqual(bonus_num, response.json().get("data").get("bonus_num"))
        self.assertEqual(status, response.json().get("data").get("status"))
        self.assertEqual(whether_participate, response.json().get("data").get("whether_participate"))
        self.assertEqual(join_time, response.json().get("data").get("join_time"))