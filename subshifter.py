import re
import sys
import datetime
import os

###################################
#   USAGE:
#   -$ python3 subshifter location.srt destination.srt [delta in milisseconds] [optional encoding]
#   Example: python subshifter subtitles.srt shiftedsubtitles -1000 latin



if (len(sys.argv) < 4 or len(sys.argv) > 5):
    print("fez merda ai")
    sys.exit(-1)

encoding = 'latin'
if len(sys.argv) == 5:
    encoding = sys.argv[4]


file = open(os.path.join(os.getcwd(),sys.argv[1]), 'r', encoding=encoding)
out_file = open(os.path.join(os.getcwd(),sys.argv[2]),'w',encoding=encoding)
delta = int( sys.argv[3])

lines = file.read().splitlines()

for line in lines:
    new_line = line
    results = re.finditer(r'\d\d:\d\d:\d\d,\d{3}', new_line) 
    for result in results:
        hora = result.group()
        time = datetime.datetime.strptime(hora, '%H:%M:%S,%f')
        new_time = time + datetime.timedelta(milliseconds=delta)
        new_line = new_line.replace(result.group(),str(new_time).split()[1].replace('.',',')[0:-3])

    out_file.write(new_line)
    out_file.write("\n")
out_file.close()