#!/usr/bin/env python
# -*- coding: utf-8 -*-

from instabot import InstaBot

bot = InstaBot(login="robotitogram", password="gonzal0",
               like_per_day=1000,
               comments_per_day=0,
               tag_list=['marketing', 'herbalifenutricion'],
               max_like_for_one_tag=50,
               follow_per_day=150,
               follow_time=5*60*60,
               unfollow_per_day=150,
               unfollow_break_min=15,
               unfollow_break_max=30,
               log_mod=0)

'''
# if we want to set some particular words for a tag in particular         
comment_for_tags = {}
comment_for_tags["car"] = ["this", "the"],["car", "vehicle", "motorcar", "automobile"],["is", "looks", "feels", "is really"],["great", "super", "good", "very good", "awesome", "incredible", "amazing"]
bot.set_tag_comment_values(comment_for_tags)    
'''

bot.new_auto_mod()
