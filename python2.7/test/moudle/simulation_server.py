# coding:utf-8
import sys
if len(sys.argv)<2:
    print "error"
else:
    # 这样满足wsgi标准的web应用都能在这个服务器上跑了
    app_path =sys.argv[1]
    moudle, application = app_path.split(':')
    moudle = __import__(moudle)
    application = getattr(moudle, application)
    application()