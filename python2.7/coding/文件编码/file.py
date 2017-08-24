import os
import chardet
base_url = os.getcwd()
with open(base_url+'/static/f1') as f:
    print chardet.detect(f.read())