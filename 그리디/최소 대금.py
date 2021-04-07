# -*- coding: utf-8 -*-
pasta1 = int(input())
pasta2 = int(input())
pasta3 = int(input())
beverage1 = int(input())
beverage2 = int(input())

s1 = (pasta1 if pasta1 < pasta2 else pasta2) if (pasta1 if pasta1 < pasta2 else pasta2) < pasta3 else pasta3
s2 = (beverage1 if beverage1 < beverage2 else beverage2)

s = (s1 + s2) * 1.1

print(format(s, '.1f'))
