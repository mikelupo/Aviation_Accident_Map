import os

def accidents():
    accidents = []
    basedir = os.path.abspath(os.path.dirname(__file__))
    av_file = os.path.join(basedir, 'AviationData.txt')
    print av_file
    f = open(av_file, 'r')
    lines = f.readlines()[1:]
    f.close()

    for line in lines:
        temp = line.split(' | ')
        if temp[6]:
            accidents.append({temp[2]:[temp[6], temp[7]]})
