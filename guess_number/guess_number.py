#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2019-2023, Liu Zhiyuan
# All rights reserved
import random


name = input('请问尊姓大名：')
print('欢迎 ', name)
print('请输入1-100的数字')

target_number = random.randint(1, 100)
for i in range(8):
    guess_number = input('请输入：')
    guess_number = int(guess_number)
    if guess_number < target_number:
        print('小了')
    elif guess_number > target_number:
        print('大了')
    else:
        print('对了')
        break

if target_number == guess_number:
    print('恭喜猜对，猜了', i, '次')
else:
    print('还需要加油,正确答案是:', target_number)
