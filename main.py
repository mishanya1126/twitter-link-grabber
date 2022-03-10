import requests as r
import threading
import time
import random
from datetime import datetime

def getinottheserver(ds_token, link):
    ses_ds = r.Session()
    ses_ds.headers['authorization'] = ds_token
    resp_ds = ses_ds.post(f"https://discord.com/api/v9/invites/{link}").json()
    if "guild" in resp_ds:
        print(f"{datetime.now().strftime('%H:%M:%S')} --- Added {ds_token} to {link}")
    else:
        print(f"{datetime.now().strftime('%H:%M:%S')} --- Error for {ds_token}")

useragents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 11.4; rv:89.0) Gecko/20100101 Firefox/89.0','Mozilla/5.0 (X11; Linux i686; rv:89.0) Gecko/20100101 Firefox/89.0','Mozilla/5.0 (Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:89.0) Gecko/20100101 Firefox/89.0','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0','Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; Trident/4.0;)','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)','Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.0)','Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2)','Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 6.2; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 Edg/91.0.864.37','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 Edg/91.0.864.37','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 OPR/77.0.4054.64','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 OPR/77.0.4054.64','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 OPR/77.0.4054.64','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 OPR/77.0.4054.64','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 Vivaldi/4.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 Vivaldi/4.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 Vivaldi/4.0','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 Vivaldi/4.0','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36 Vivaldi/4.0','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 YaBrowser/21.5.0 Yowser/2.5 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 YaBrowser/21.5.0 Yowser/2.5 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 YaBrowser/21.5.0 Yowser/2.5 Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.80 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.80 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPod; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.80 Mobile/15E148 Safari/604.1','Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/34.0 Mobile/15E148 Safari/605.1.15','Mozilla/5.0 (iPad; CPU OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/34.0 Mobile/15E148 Safari/605.1.15','Mozilla/5.0 (iPod touch; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) FxiOS/34.0 Mobile/15E148 Safari/605.1.15','Mozilla/5.0 (Android 11; Mobile; rv:68.0) Gecko/68.0 Firefox/89.0','Mozilla/5.0 (Android 11; Mobile; LG-M255; rv:89.0) Gecko/89.0 Firefox/89.0','Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPod touch; CPU iPhone 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1','Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36 EdgA/46.3.4.5155','Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36 EdgA/46.3.4.5155','Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36 EdgA/46.3.4.5155','Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36 EdgA/46.3.4.5155','Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 EdgiOS/46.3.13 Mobile/15E148 Safari/605.1.15','Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Mobile Safari/537.36 Edge/40.15254.603','Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36 OPR/63.3.3216.58675','Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36 OPR/63.3.3216.58675','Mozilla/5.0 (Linux; Android 10; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36 OPR/63.3.3216.58675','Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 YaBrowser/21.5.3.836 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 YaBrowser/21.5.3.836 Mobile/15E148 Safari/605.1','Mozilla/5.0 (iPod touch; CPU iPhone 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 YaBrowser/21.5.3.836 Mobile/15E148 Safari/605.1','Mozilla/5.0 (Linux; arm_64; Android 11; SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 YaBrowser/21.3.4.59 Mobile Safari/537.36']

s = r.Session()
s.headers.update({'User-Agent': random.choice(useragents), 'Origin': 'https://mobile.twitter.com', 'Referer': 'https://mobile.twitter.com/', 'x-twitter-active-user': 'yes', 'x-twitter-auth-type': 'OAuth2Session', 'x-twitter-client-language': 'en', 'content-type': 'application/x-www-form-urlencoded'})

queryId = s.get('https://abs.twimg.com/responsive-web/client-web/main.f3ada2b5.js')

queryIdforSubscribe = queryId.text.split('",operationName:"TweetResultByRestId",operationType:"query",metadata:{featureSwitches:[]}}},fDBV:function(e,t){e.exports={queryId:"')[-1].split('"')[0]
bearertoken = 'Bearer '+queryId.text.split('const r="ACTION_FLUSH",i="ACTION_REFRESH')[-1].split(',l="d_prefs"')[0].split(',s="')[-1].split('"')[0]

#inputs
username = input("Twitter username --> ") #username = "kahirunft"
#end inputs

#setup
auth_ds = open("ds_tokens.txt", "r").readlines()

cookiestr = open("cookies.txt", "r").readline()
csrftoken = cookiestr.split('ct0=')[-1].split(';')[0]
s.headers.update({'authorization': bearertoken, 'cookie': cookiestr, 'x-csrf-token': csrftoken})

user_id_resp = s.get('https://mobile.twitter.com/i/api/graphql/'+queryIdforSubscribe+'/UserByScreenName?variables={"screen_name":"'+username+'","withSafetyModeUserFields":true,"withSuperFollowsUserFields":true}')
user_id = user_id_resp.json()['data']['user']['result']['rest_id']
#end setup

prev_twit = ""
threads = []

while True:
    time.sleep(3)

    resp_twit = s.get('https://twitter.com/i/api/graphql/WZT7sCTrLvSOaWOXLDsWbQ/UserTweets?variables={"userId":"'+user_id+'","count":40,"includePromotedContent":true,"withQuickPromoteEligibilityTweetFields":true,"withSuperFollowsUserFields":true,"withDownvotePerspective":false,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":true,"withVoice":true,"withV2Timeline":true,"__fs_dont_mention_me_view_api_enabled":false,"__fs_interactive_text_enabled":true,"__fs_responsive_web_uc_gql_enabled":false}')


    i = 0
    while True:
        try:
            twit_text = resp_twit.json()['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries'][i]['content']['itemContent']['tweet_results']['result']['legacy']['full_text']
            break
        except:
            i+=1

    if prev_twit != twit_text:
        prev_twit = twit_text
        print(f"{datetime.now().strftime('%H:%M:%S')} --- Found new twit")
    else:
        continue

    if "https://t.co/" in twit_text:
        try:
            ds_link = r.get("https://t.co/" + twit_text.split("https://t.co/")[1][:10]).text.split('href="https://discord.com/invite/')[1][:8]
        except:
            ds_link = "no ds link"
    else:
        ds_link = "no link"


    if ds_link not in ('no ds link','no link'):
        print(f"{datetime.now().strftime('%H:%M:%S')} --- Found server link: {ds_link}")
        for line in auth_ds:
            line = line.replace("\n","")
            threads.append(threading.Thread(target=getinottheserver, args=(line, ds_link)))
            threads[-1].start()

    else:
        print(f"{datetime.now().strftime('%H:%M:%S')} --- No server link found")