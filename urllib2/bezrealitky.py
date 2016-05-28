    import urllib2
    import time
    import tweepy
    import os
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_secret = ''
 #   tweet_string = 'twitter set @dhruvbaldawa Result for %s %s declared.'
 #   url = 'http://results.mu.ac.in/choose_nob.php?exam_id=%s&exam_year=2012&exam_month=MAY'
    url = 'http://www.bezrealitky.cz/vyhledat#?order=time_order_desc&advertoffertype=nabidka-pronajem&ownership=&equipped=&address=Praha&map=50.064401,14.398165,50.081065,14.433999,15&priceFrom=null&priceTo=null&construction=&description=&surfaceFrom=&surfaceTo=&balcony=&terrace=&polygon=[{%22lat%22:50.07589846383411,%22lng%22:14.413204193115234},{%22lat%22:50.07631159023149,%22lng%22:14.413676261901855},{%22lat%22:50.07881781407393,%22lng%22:14.414019584655762},{%22lat%22:50.07801914157734,%22lng%22:14.424748420715332},{%22lat%22:50.07757848898739,%22lng%22:14.429640769958496},{%22lat%22:50.075843380045505,%22lng%22:14.429168701171875},{%22lat%22:50.074796776038575,%22lng%22:14.42929744720459},{%22lat%22:50.07358489022698,%22lng%22:14.429211616516113},{%22lat%22:50.072483149274085,%22lng%22:14.429340362548828},{%22lat%22:50.07107839284687,%22lng%22:14.429340362548828},{%22lat%22:50.06937059431849,%22lng%22:14.430155754089355},{%22lat%22:50.067414814852604,%22lng%22:14.43079948425293},{%22lat%22:50.06512837999673,%22lng%22:14.430413246154785},{%22lat%22:50.064191736659104,%22lng%22:14.428396224975586},{%22lat%22:50.06408154212282,%22lng%22:14.426379203796387},{%22lat%22:50.0637234081316,%22lng%22:14.424405097961426},{%22lat%22:50.063447918626565,%22lng%22:14.422473907470703},{%22lat%22:50.06325507503166,%22lng%22:14.42054271697998},{%22lat%22:50.06333772238155,%22lng%22:14.41856861114502},{%22lat%22:50.06350301665415,%22lng%22:14.416637420654297},{%22lat%22:50.064742705543324,%22lng%22:14.415135383605957},{%22lat%22:50.066560857959715,%22lng%22:14.414019584655762},{%22lat%22:50.068241210272475,%22lng%22:14.413118362426758},{%22lat%22:50.07022450118469,%22lng%22:14.412646293640137},{%22lat%22:50.07215262205212,%22lng%22:14.412517547607422},{%22lat%22:50.0740806653974,%22lng%22:14.412088394165039},{%22lat%22:50.075843380045505,%22lng%22:14.412775039672852},{%22lat%22:50.07589846383411,%22lng%22:14.413204193115234}]&estatetype[]=byt&id=414179'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    t = tweepy.API(auth)
    id_start = 2765
    id_ = id_start
    while True:
        url_socket = urllib2.urlopen(url % id_)
        temp = url_socket.read().lower()
        if temp.find('no such exam!!') < 0:
            if temp.find('computer') > 0:
                print(tweet_string % (id_, True))
                # os.system(tweet_string % (id_, True))
                os.system("vlc ~/01.mp3")
            else:
                print(tweet_string % (id_, False))
                # os.system(tweet_string % (id_, False))
            id_ += 1
        else:
            time.sleep(300)
