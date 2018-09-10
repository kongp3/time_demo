# -*- coding: utf-8 -*-
import arrow
'''...'''
if __name__ == '__main__':
    utc = arrow.utcnow()
    print utc                   # 2018-09-10T02:37:13.860450+00:00

    # 前后时间随意获取
    print utc.shift(hours=-1)   # 2018-09-10T01:39:44.621774+00:00
    print utc.shift(weeks=+3)

    # 一些常用属性
    print utc.datetime
    print utc.year
    print utc.month
    print utc.day
    print utc.weekday()
    print utc.naive
    print utc.tzinfo

    # 获取各地时间

    '''
    安装Linux时选时区，在下拉列表中就会发现，里面没有北京，却有上海和重庆，还有乌鲁木齐。这是为什么呢？
    原因是1949年以前，中国一共分了5个时区，以哈尔滨、上海、重庆、乌鲁木齐和喀什为代表
    分别是：长白时区GMT+8:30、中原标准时区 GMT+8、陇蜀时区GMT+7、新藏时区GMT+6和昆仑时区GMT+5:30。
    它是1912年北京观象台制订，后由内政部批准过

    对于自己的城市不在列表中这个大问题，LinuxJournal也讲了怎么把自己的城市加入时区列表的做法：
    到/usr/share/zoneinfo或/usr/lib/zoneinfo目录下，
    将Asia/Shanghai拷贝为Asia/Beijing， 因为时区一样，数据也就一样。
    编辑zone.tab文件，还是找到刚才copy的城市再copy一行，只是其中的数字代表城市的经纬度，需要修改正确。
    '''

    us_local = utc.to('US/Pacific')
    cn_local = utc.to('Asia/Shanghai')
    eu_local = utc.to('Europe/Berlin')
    print cn_local
    print cn_local.timestamp
    print cn_local.tzinfo
    print eu_local.tzinfo


    # 格式化
    print cn_local.format()
    print cn_local.format('YYYY-MM-DD-------HH:mm:ss ZZ')  # 这里可以随意定义输出格式

    # 输出一个人能看的懂得文字
    print cn_local.humanize()
    print cn_local.humanize(locale='ko_kr')
    print cn_local.humanize(locale='zh_CN')

    # 获取now
    print arrow.utcnow()
    print arrow.now()    # 这个是如何识别当地时间的呢? 看了源码,是底层代码操作的,所以还是加上时区比较靠谱
    print arrow.now('Asia/Shanghai')

    # 花式获取arrow对象
    print arrow.get(1367900664)
    print arrow.get('1367900664')
    print arrow.get('2013-05-11T21:23:58.970460+00:00')
    print arrow.get('2013-05-05 12:30:45', 'YYYY-MM-DD HH:mm:ss')  # 任意格式的string可以获取arrow对象
    print arrow.get('June was born in May 1980', 'MMMM YYYY')  # 这个自动搜索功能有点儿牛逼了
    print arrow.get(2013, 5, 5)
    print arrow.Arrow(2013, 5, 5)

    from datetime import datetime
    print arrow.get(datetime.utcnow())
    print arrow.get(datetime(2013, 5, 5), 'US/Pacific')

    # 时间转换
    arw = arrow.utcnow()
    print arw
    print arw.replace(hour=4, minute=40)
    print arw.replace(tzinfo='US/Pacific')

    # 四舍五入
    arrow.utcnow().floor('hour')
    arrow.utcnow().ceil('hour')

    # 时间循环
    start = datetime(2013, 5, 5, 12, 30)
    end = datetime(2013, 5, 5, 17, 15)
    for r in arrow.Arrow.span_range('hour', start, end):
        print r

    arrow.ArrowFactory()

    '''
    Formate时候的高频字符
                        Token	Output

    Year	            YYYY	2000, 2001, 2002 ... 2012, 2013
                        YY	    00, 01, 02 ... 12, 13
    Month	            MMMM	January, February, March ...
                        MMM	    Jan, Feb, Mar ...
                        MM	    01, 02, 03 ... 11, 12
                        M	    1, 2, 3 ... 11, 12
    Day of Year     	DDDD	001, 002, 003 ... 364, 365
                        DDD	    1, 2, 3 ... 4, 5
    Day of Month	    DD	    01, 02, 03 ... 30, 31
                        D	    1, 2, 3 ... 30, 31
                        Do	    1st, 2nd, 3rd ... 30th, 31st
    Day of Week	        dddd	Monday, Tuesday, Wednesday ...
                        ddd	    Mon, Tue, Wed ...
                        d	    1, 2, 3 ... 6, 7
    Hour	            HH	    00, 01, 02 ... 23, 24
                        H	    0, 1, 2 ... 23, 24
                        hh	    01, 02, 03 ... 11, 12
                        h	    1, 2, 3 ... 11, 12
    AM / PM	            A	    AM, PM, am, pm
                        a	    am, pm
    Minute	            mm	    00, 01, 02 ... 58, 59
                        m	    0, 1, 2 ... 58, 59
    Second	            ss	    00, 01, 02 ... 58, 59
                        s	    0, 1, 2 ... 58, 59
    Sub-second	        S...	0, 02, 003, 000006, 123123123123...
    Timezone	        ZZZ	    Asia/Baku, Europe/Warsaw, GMT ...
                        ZZ	    -07:00, -06:00 ... +06:00, +07:00
                        Z	    -0700, -0600 ... +0600, +0700
    Timestamp	        X	    1381685817
    '''
