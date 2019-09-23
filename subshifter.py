import re
import sys
import datetime
import os

# Args handling
if (len(sys.argv) < 3 or len(sys.argv) > 4):
    print(r'subshifter usage: subshifter subtitles.srt [delta in milisseconds] [encoding (optional)]')
    print("Please try again...")
    sys.exit(0)


if (sys.argv[1][-4:] != ".srt") :
    print("ERROR: entry file must be a .srt subtitle")
    print(r'subshifter usage: subshifter subtitles.srt [delta in milisseconds] [encoding (optional)]')
    print("Please try again...")
    sys.exit(0)

#  Default encoding = latin
encoding = 'latin'
if len(sys.argv) == 5:
    encoding = sys.argv[3]


# Args reading
file = open(os.path.join(os.getcwd(),sys.argv[1]), 'r', encoding=encoding)
out_buff = []

# Checking if delta is a valid numbe r
try:
    delta = int(sys.argv[2])
except ValueError:
    print("ERROR: delta must be an integer number")
    print(r'subshifter usage: subshifter subtitles.srt [delta in milisseconds] [encoding (optional)]')
    print("Please try again...")
    sys.exit(0)



print("Reading and Shifting subtitles in {} milisseconds...".format(delta))

lines = file.read().splitlines()

for line in lines:
    new_line = line

    # Looking for time marks by using regex
    results = re.finditer(r'\d\d:\d\d:\d\d,\d{3}', new_line) 

    # iterating through time marks and shifting
    for result in results:
        second = result.group()
        time = datetime.datetime.strptime(second, '%H:%M:%S,%f')
        new_time = time + datetime.timedelta(milliseconds=delta)
        new_line = new_line.replace(second, str(new_time).split()[1].replace('.',',')[0:-3])

    # appending to output buffer
    out_buff.append(new_line+"\n")

file.close()

print("saving changes...")
file = open(os.path.join(os.getcwd(),sys.argv[1]), 'w', encoding=encoding)
file.writelines(out_buff)
file.close()

print("done!")