import json
import subprocess
import os

for root, dirs, files in os.walk('.'):
  files = [ fi for fi in files if fi.endswith(".crop") ]
  #print files
  for fi in files:
    filename = root +"/"+ fi;
    json_data=open(filename).read()
    data = json.loads(json_data)
    #Need to parse the filenames!!
    name, extension = os.path.splitext(fi)
    name = root + "/" + name[1:]
    data["FILENAME"] = name #take off .crop
    name, extension = os.path.splitext(name)
    data["NEWFILENAME"] = name + "Thumb" + extension #take off .ext then add thumb and back ext
    print data
    subprocess.call(['convert', \
    '%(FILENAME)s' % data, \
    '-adaptive-resize', \
    '%(resize)d%%x%(resize)d%%' % data, \
    '-gravity', \
    'Center', \
    '-crop', \
    '%(sizeX)dx%(sizeY)d%(startX)+d%(startY)+d' % data, \
    '%(NEWFILENAME)s' % data \
    ]);

