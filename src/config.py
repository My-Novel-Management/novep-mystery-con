# -*- coding: utf-8 -*-
'''
Story Config
============
'''

ASSET = {
        "PERSONS": (
        # (tag / name / full / age (birth) / sex / job / call / info)
        ("kiri", "霧宮", "霧宮,麗斗", 17,(1,1), "male", "高校生", 'me:ボク'),
        ('natsu', '夏美', '比嘉,夏美', 17,(1,1), 'female', '高校生', 'me:わたし'),
        ('yuji', '優二', '倉敷,優二', 17,(1,1), 'male', '高校生', 'me:俺'),
        ('tobe', '砥部', '砥部,豊', 36,(1,1), 'male', '高校教師', 'me:おれ'),
        ('shiki', '式美', '倉敷,式美', 20,(1,1), 'female', '大学生', 'me:私'),
        ('hatake', '畠田', '畠田,きよ江', 65,(1,1), 'female', '清掃員', 'me:私'),
        ),
        "STAGES": (
        # (tag / name / parent / (geometry) / info)
        ('HighSchool', '県立高校', 'Tokyo'),
        ('bu-room', '文芸部部室', 'HighSchool', (100,100)),
        ),
        "DAYS": (
        # (tag / name / month / day / year)
        ('notice1', '幽霊ノートに気づいた', 6,10, 2020),
        ),
        "TIMES": (
        # (tag / name / hour / minute)
        ),
        "ITEMS": (
        # (tag / name / cate / info)
        ('bunnote', '文芸部ノート'),
        ),
        "WORDS": (
        # (tag / name / cate / info)
        ),
        "RUBIS": (
        # (origin / rubi / exclusions / always)
        ),
        }

