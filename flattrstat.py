#!/usr/bin/env python
# -*- coding:utf-8 -*-

#FlattrStat is a simple tool to give you some statistics about your flattr revenue.
#Download the CSV files from Flattr and then run the script in the same folder.
#
# Copyright (c) 2012 Lionel Dricot
#
# This script is under the WTFPL - Do What The Fuck You Want To Public License
# Source code: https://github.com/ploum/FlattrStt
# License : http://sam.zoy.org/wtfpl/

import csv, os

files=os.listdir(".")
#print files
things = {}

for f in files:
	if f.endswith(".csv"):
    		revenue = csv.reader(open(f, 'rb'),delimiter=';')
		#skipping the first line
		revenue.next()
		for row in revenue:
			#0 = month
			#1 = id
			#2 = flattr URL
			#3 = original URL
			#4 = Title
			#5 = clicks this month
			#6 = revenue this month
			#7 click total
			url=row[3].split('//')[1]
			domain=url.split('/',1)[0]
			if things.has_key(domain):
				dom = things[domain]
			else:
				dom = {}
				dom['domain'] = domain
				dom['clicks'] = 0
				dom['revenue'] = 0.0
				dom['things'] = {}
				things[domain] = dom

			if dom['things'].has_key(url):
				thing = dom['things'][url]
			else:
				thing = {}
				thing['domain'] = domain
				thing['url'] = url
				thing['title'] = row[4]
				thing['clicks'] = 0
				thing['revenue'] = 0.0
				dom['things'][url] = thing
			thing['clicks'] += int(row[5])
			thing['revenue'] += float(row[6].replace(',','.'))
			dom['clicks'] += int(row[5])
			rev = float(row[6].replace(',','.'))
			dom['revenue'] += rev

k = things.keys()
ord_k = sorted(k, reverse=True ,key=lambda x: things[x]['revenue'])

for dd in ord_k:
	d = things[dd]
	print "%s (%s clicks - %.2f euros)" %(d['domain'],d['clicks'],d['revenue'])

	kk = d['things'].keys()
	ord_kk = sorted(kk, reverse=True, key=lambda x: d['things'][x]['revenue'])
	for tt in ord_kk:
		t = d['things'][tt]
		print "     -> %s clicks/%.2f euros (%s)"\
					%(t['clicks'],t['revenue'],t['title'])
