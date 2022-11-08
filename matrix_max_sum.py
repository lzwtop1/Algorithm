#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


class Solution:
    def partitionNumber(self, text):


# Write Code Here

try:
    _text = input()
except:
    _text = None

s = Solution()
res = s.partitionNumber(_text)

print(str(res) + "\n")