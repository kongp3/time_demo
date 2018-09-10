# -*- coding: utf-8 -*-
from datetime import datetime
if __name__ == '__main__':
    text = '20160816　12:16:32'
    y = datetime.strptime(text, '%Y%m%d　%H:%M:%S')   # 这里的格式只要和上面text格式一致就可以load进来
    print y
    z = datetime.now()
    diff = z - y
    print diff
