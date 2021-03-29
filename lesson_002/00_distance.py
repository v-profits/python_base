#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint
# Есть словарь координат городов
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris' : (480, 480),
}
# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2
distances = {}
moscow=sites['Moscow']
london=sites['London']
paris =sites['Paris' ]
distances['moscow_london']=((moscow[0]-london[0])**2 + (moscow[1]-london[1])**2)**0.5
distances['moscow_paris' ]=((moscow[0]-paris [0])**2 + (moscow[1]-paris [1])**2)**0.5
distances['london_paris' ]=((paris [0]-london[0])**2 + (paris [1]-london[1])**2)**0.5
distances['london_moccow']=((moscow[0]-london[0])**2 + (moscow[1]-london[1])**2)**0.5
distances['paris_london' ]=((paris [0]-london[0])**2 + (paris [1]-london[1])**2)**0.5
distances['paris_moscow' ]=((moscow[0]-paris [0])**2 + (moscow[1]-paris [1])**2)**0.5
pprint(distances)




