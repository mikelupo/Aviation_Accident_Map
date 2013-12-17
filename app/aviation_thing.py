import os
import json

BASEURL='http://www.ntsb.gov/aviationquery/brief.aspx?ev_id='

def accidents():
    accidents = []
    basedir = os.path.abspath(os.path.dirname(__file__))
    av_file = os.path.join(basedir, 'AviationData.txt')
    f = open(av_file, 'r')
    lines = f.readlines()[1:]
    f.close()

    for line in lines:
        temp = line.split(' | ')
        if temp[6]:
            accidents.append({  'id':temp[2],
                                'lat':temp[6],
                                'lon':temp[7],
                                'inj-sev':temp[10],
                                'make':temp[14],
                                'model':temp[15],
                                'prob':BASEURL+temp[0]})
    return json.dumps(accidents)