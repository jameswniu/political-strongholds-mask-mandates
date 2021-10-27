import os, sys
import re
from datetime import datetime, timedelta
from collections import defaultdict


os.chdir(r'C:\Users\wendi\My Drive\project\Resources')  # SPECIFY
# Please download and select csv from the url below as file is too large to upload to GitHub
url = 'https://catalog.data.gov/dataset/u-s-state-and-territorial-public-mask-mandates-from-april-10-2020-through-january-10-2021--e0ce3'
# Place file in same folder as script
file = 'U.S._State_and_Territorial_Public_Mask_Mandates_From_April_10__2020_through_August_15__2021_by_County_by_Day.csv'

########################################################################################################################
# pick out relevant variables only
########################################################################################################################
# UNCOMMENT YOU NEED TO RUN THIS ONLY ONCE
# fw = open('mandates_raw.csv', 'w')
#
# i = 0
# with open(file, 'r') as fr:
#     head = 'state,county,statefips,countyfips,month,mask'
#     print(head, file=fw)
#     print(head)
#
#     next(fr)
#
#     for line in fr:
#         line = line.strip()
#
#         tmp = line.split(',')
#
#         if len(tmp[0]) != 2:
#             continue
#
#         date = datetime.strptime(tmp[4], '%m/%d/%Y')
#         mth = datetime.strftime(date, '%Y%m%d')
#         # print(date)
#         # print(mth)
#
#         if tmp[6] == 'Yes':
#             mask = 1
#         else:
#             mask = 0
#
#         newline = f'{tmp[0]},{tmp[1]},{tmp[2]},{tmp[3]},{mth},{mask}'
#         print(newline, file=fw)
#         print(newline)
#
#         # i += 1
#         # if i == 100:
#         #     break
# fw.close()


########################################################################################################################
# create mask mandates by county by month
########################################################################################################################
fw = open('mandates_by_county_by_month.csv', 'w')

dicy = defaultdict(int)
pot = defaultdict(int)
jar = {}
with open(r'mandates_raw.csv', 'r') as fr:
    head = 'state,county,statefips,countyfips,month,maskdays,days,maskcoverage'
    print(head, file=fw)
    print(head)

    next(fr)

    for line in fr:
        line = line.strip()
        tmp = line.split(',')

        k = f'{tmp[0]},{tmp[1]},{tmp[2]},{tmp[3]},{tmp[4][:6]}'
        v = int(tmp[5])

        dicy[k] += v
        pot[k] += 1


    for k in dicy:
        maskdays = dicy[k]
        days = pot[k]
        maskrate = round(float(dicy[k]) / float(pot[k]), 2)
        jar[k] = f'{maskdays},{days},{maskrate}'

    for k, v in jar.items():
        print('{},{}'.format(k, v), file=fw)
        print('{},{}'.format(k, v))

fw.close()


########################################################################################################################
# create mask mandates by county
########################################################################################################################
fw = open('mandates_by_county.csv', 'w')

dicy = defaultdict(int)
pot = defaultdict(int)
jar = {}
with open(r'mandates_raw.csv', 'r') as fr:
    head = 'state,county,statefips,countyfips,maskdays,days,maskcoverage'
    print(head, file=fw)
    print(head)

    next(fr)

    for line in fr:
        line = line.strip()
        tmp = line.split(',')

        k = f'{tmp[0]},{tmp[1]},{tmp[2]},{tmp[3]}'
        v = int(tmp[5])

        dicy[k] += v
        pot[k] += 1


    for k in dicy:
        maskdays = dicy[k]
        days = pot[k]
        maskrate = round(float(dicy[k]) / float(pot[k]), 2)
        jar[k] = f'{maskdays},{days},{maskrate}'

    for k, v in jar.items():
        print('{},{}'.format(k, v), file=fw)
        print('{},{}'.format(k, v))

fw.close()


########################################################################################################################
# create mask mandates by state
########################################################################################################################
fw = open('mandates_by_state.csv', 'w')

dicy = defaultdict(int)
pot = defaultdict(int)
jar = {}
with open(r'mandates_raw.csv', 'r') as fr:
    head = 'state,statefips,maskdays,days,maskcoverage'
    print(head, file=fw)
    print(head)

    next(fr)

    for line in fr:
        line = line.strip()
        tmp = line.split(',')

        k = f'{tmp[0]},{tmp[2]}'
        v = int(tmp[5])

        dicy[k] += v
        pot[k] += 1


    for k in dicy:
        maskdays = dicy[k]
        days = pot[k]
        maskrate = round(float(dicy[k]) / float(pot[k]), 2)
        jar[k] = f'{maskdays},{days},{maskrate}'

    for k, v in jar.items():
        print('{},{}'.format(k, v), file=fw)
        print('{},{}'.format(k, v))

fw.close()
