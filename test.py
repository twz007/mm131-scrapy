#!/usr/bin/python
# -*- coding: utf-8 -*
'''
  @Project        xztpic
  @FileName       test.py
  @Software       PyCharm
  @Author         twz
  @Date           2019/3/29 15:51
  @Description    
'''
import re
pattern = re.compile(r'\(\d+\)')

str = '空虚少妇王婉悠好色肉体搔首弄姿(2)'
print(pattern.findall(str))
out = re.sub(pattern=pattern, repl='', string=str)
print(out)