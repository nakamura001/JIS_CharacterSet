#! /usr/bin/env python
# coding: utf-8

import codecs

ch_list = []
f = open('table_files/JIS0212.TXT', 'r')
for row in f:
    if row[0] != '#':
        c = row.split("\t")[1]
        ch_list.append(unichr(int(c, 16)))
f.close()

f = codecs.open('JIS_X_0212_utf8.txt', 'w', 'utf-8')
txt = "".join(ch_list)
#txt = "\n".join(ch_list)
f.write(txt)
f.close()