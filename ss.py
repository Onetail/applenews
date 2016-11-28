# coding=UTF-8

import requests
import datetime
import os
import codecs
from bs4 import BeautifulSoup

Time = datetime.datetime.now()

def Top(x):
    if x == 1:
        global Top_max
        global Top_content
        Top_max = 0
        Top_content = ""
        res = requests.get('http://www.appledaily.com.tw/appledaily/hotdaily/')
        res.encoding = 'utf=8'
        soup = BeautifulSoup(res.text,"html.parser")
        print (soup.select('time')[0].text)
        try:
            for i in range(0,30):
               print ("%2d." % int(i+1),soup.select('.aht_title')[i].text,"*",soup.select('.aht_pv_num')[i].text)
               if Top_max < int(soup.select('.aht_pv_num')[i].text):
                   Top_max = int(soup.select('.aht_pv_num')[i].text)
                   Top_content = soup.select('.aht_title')[i].text
        except:
            print("\n")
       
    elif x == 2:
        print('不開放!')
    elif x == 3:
        try:
            print("正在寫入...")
            global Top_max_w
            global Top_content_w
            TT = open("Apple_news.txt","a+")
            Top_max_w = 0
            Top_content_w = ""
            res = requests.get('http://www.appledaily.com.tw/appledaily/hotdaily/')
            res.encoding = 'utf=8'
            soup = BeautifulSoup(res.text,"html.parser")
            TT.write("\n今日top 30:")
            TT.write(soup.select('time')[0].text)
            for i in range(0,30):
                TT.write("\n%2d." %int(i+1)+ soup.select('.aht_title')[i].text+"*"+soup.select('.aht_pv_num')[i].text)
                if Top_max_w < int(soup.select('.aht_pv_num')[i].text):
                    Top_max_w = int(soup.select('.aht_pv_num')[i].text)
                    Top_content_w = soup.select('.aht_title')[i].text
            TT.write("\n\ntop\n")
        except:
            print("\n")
        finally:
            TT.close()
def headline(x):
    if x == 1:
        global headline_max
        global headline_content
        headline_max = 0
        headline_content = ""
        res = requests.get('http://www.appledaily.com.tw/appledaily/hotdaily/headline')
        res.encoding = 'utf=8'
        soup = BeautifulSoup(res.text,"html.parser")
        print (soup.select('time')[0].text)
        try:
            for i in range(0,30):
                print ("%2d." % int(i+1),soup.select('.aht_title')[i].text,"*",soup.select('.aht_pv_num')[i].text)
                if headline_max < int(soup.select('.aht_pv_num')[i].text):
                    headline_max = int(soup.select('.aht_pv_num')[i].text)
                    headline_content = soup.select('.aht_title')[i].text
        except:
            print("\n")
    elif x == 2:
        print('不開放!')
    elif x == 3:
        try:
            print("正在寫入...")
            global headline_max_w
            global headline_content_w
            TT = open("Apple_news.txt","a+")
            headline_max_w = 0
            headline_content_w = ""
            res = requests.get('http://www.appledaily.com.tw/appledaily/hotdaily/headline')
            res.encoding = 'utf=8'
            soup = BeautifulSoup(res.text,"html.parser")
            TT.write("\n要聞news:"+"\n")
            TT.write(soup.select('time')[0].text)
            for i in range(0,30):
                TT.write("\n%2d." % int(i+1) + soup.select('.aht_title')[i].text+"*"+soup.select('.aht_pv_num')[i].text)
                if headline_max_w < int(soup.select('.aht_pv_num')[i].text):
                    headline_max_w = int(soup.select('.aht_pv_num')[i].text)
                    headline_content_w = soup.select('.aht_title')[i].text
        except:
            print("\n")
        finally:
            TT.close()
def entertainment(x):
    if x == 1:
        global entertainment_max
        global entertainment_content
        entertainment_max = 0
        entertainment_content = ""
        res = requests.get('http://www.appledaily.com.tw/appledaily/hotdaily/entertainment')
        res.encoding = 'utf=8'
        soup = BeautifulSoup(res.text,"html.parser")
        print (soup.select('time')[0].text)
        try:
            for i in range(0,30):
                print ("%2d." % int(i+1),soup.select('.aht_title')[i].text,"*",soup.select('.aht_pv_num')[i].text)
                if entertainment_max < int(soup.select('.aht_pv_num')[i].text):
                    entertainment_max = int(soup.select('.aht_pv_num')[i].text)
                    entertainment_content = soup.select('.aht_title')[i].text
        except:
            print("\n")
    elif x == 2:
        print('不開放!')
    elif x == 3:
        try:
            print("正在寫入...")
            global entertainment_max_w
            global entertainment_content_w
            TT = open("Apple_news.txt","a+")
            entertainment_max_w = 0
            entertainment_content_w = ""
            res = requests.get('http://www.appledaily.com.tw/appledaily/hotdaily/entertainment')
            res.encoding = 'utf=8'
            soup = BeautifulSoup(res.text,"html.parser")
            TT.write("\n娛樂news:"+"\n")
            TT.write(soup.select('time')[0].text)
            for i in range(0,30):
                TT.write("\n%2d." % int(i+1) + soup.select('.aht_title')[i].text+"*"+soup.select('.aht_pv_num')[i].text)
                if entertainment_max_w < int(soup.select('.aht_pv_num')[i].text):
                    entertainment_max_w = int(soup.select('.aht_pv_num')[i].text)
                    entertainment_content_w = soup.select('.aht_title')[i].text
        except:
            print("")
        finally:
            TT.close()
def international(x):
    if x == 1:
        global international_max
        global international_content
        international_max = 0
        international_content = ""
        res = requests.get('http://www.appledaily.com.tw/appledaily/hotdaily/international')
        res.encoding = 'utf=8'
        soup = BeautifulSoup(res.text,"html.parser")
        print (soup.select('time')[0].text)
        try:
            for i in range(0,30):
                print ("%2d." % int(i+1),soup.select('.aht_title')[i].text,"*",soup.select('.aht_pv_num')[i].text)
                if international_max < int(soup.select('.aht_pv_num')[i].text):
                    international_max = int(soup.select('.aht_pv_num')[i].text)
                    international_content = soup.select('.aht_title')[i].text
        except:
            print("\n")
    elif x == 2:
        print('不開放!')
    elif x == 3:
        try:
            print("正在寫入...")
            global international_max_w
            global international_content_w
            TT = open("Apple_news.txt","a+")
            international_max_w = 0
            international_content_w = ""
            res = requests.get('http://www.appledaily.com.tw/appledaily/hotdaily/international')
            res.encoding = 'utf=8'
            soup = BeautifulSoup(res.text,"html.parser")
            TT.write("\n國際news:"+"\n")
            TT.write(soup.select('time')[0].text)
            for i in range(0,30):
                TT.write("\n%2d." % int(i+1) + soup.select('.aht_title')[i].text+"*"+soup.select('.aht_pv_num')[i].text)
                if international_max_w < int(soup.select('.aht_pv_num')[i].text):
                    international_max_w = int(soup.select('.aht_pv_num')[i].text)
                    international_content_w = soup.select('.aht_title')[i].text

        except:
            print("\n")
        finally:
            TT.close()
def sports(x):
    if x == 1:
        global sports_max
        global sports_content
        sports_max = 0
        sports_content = ""
        res = requests.get('http://www.appledaily.com.tw/appledaily/hotdaily/sports')
        res.encoding = 'utf=8'
        soup = BeautifulSoup(res.text,"html.parser")
        print (soup.select('time')[0].text)
        try:
            for i in range(0,30):
                print ("%2d." % int(i+1),soup.select('.aht_title')[i].text,"*",soup.select('.aht_pv_num')[i].text)
                if sports_max < int(soup.select('.aht_pv_num')[i].text):
                    sports_max = int(soup.select('.aht_pv_num')[i].text)
                    sports_content = soup.select('.aht_title')[i].text
        except:
            print("\n")
    elif x == 2:
        print('不開放!')
    elif x == 3:
        try:
            print("正在寫入...")
            global sports_max_w
            global sports_content_w
            TT = open("Apple_news.txt","a+")
            sports_max_w = 0
            sports_content_w = ""
            res = requests.get('http://www.appledaily.com.tw/appledaily/hotdaily/sports')
            res.encoding = 'utf=8'
            soup = BeautifulSoup(res.text,"html.parser")
            TT.write("\n體育news:"+"\n")
            TT.write(soup.select('time')[0].text)
            for i in range(0,30):
                TT.write("\n%2d." % int(i+1) + soup.select('.aht_title')[i].text+"*"+soup.select('.aht_pv_num')[i].text)
                if sports_max_w < int(soup.select('.aht_pv_num')[i].text):
                    sports_max_w = int(soup.select('.aht_pv_num')[i].text)
                    sports_content_w = soup.select('.aht_title')[i].text

        except:
            print("\n")
        finally:
            TT.close()
def finance(x):
    if x == 1:
        global finance_max
        global finance_content
        finance_max = 0
        finance_content = ""
        res = requests.get('http://www.appledaily.com.tw/appledaily/hotdaily/finance')
        res.encoding = 'utf=8'
        soup = BeautifulSoup(res.text,"html.parser")
        print (soup.select('time')[0].text)
        try:
            for i in range(0,30):
                print ("%2d." % int(i+1),soup.select('.aht_title')[i].text,"*",soup.select('.aht_pv_num')[i].text)
                if finance_max < int(soup.select('.aht_pv_num')[i].text):
                    finance_max = int(soup.select('.aht_pv_num')[i].text)
                    finance_content = soup.select('.aht_title')[i].text
        except:
            print("\n")
    elif x == 2:
        print('不開放!')
    elif x == 3:
        try:
            print("正在寫入...")
            global finance_max_w
            global finance_content_w
            TT = open("Apple_news.txt","a+")
            finance_max_w = 0
            finance_content_w = ""
            res = requests.get('http://www.appledaily.com.tw/appledaily/hotdaily/finance')
            res.encoding = 'utf=8'
            soup = BeautifulSoup(res.text,"html.parser")
            TT.write("\n財經news:"+"\n")
            TT.write(soup.select('time')[0].text)
            for i in range(0,30):
                TT.write("\n%2d." % int(i+1) + soup.select('.aht_title')[i].text+"*"+soup.select('.aht_pv_num')[i].text)
                if finance_max_w < int(soup.select('.aht_pv_num')[i].text):
                    finance_max_w = int(soup.select('.aht_pv_num')[i].text)
                    finance_content_w = soup.select('.aht_title')[i].text
        except:
            print("\n")
        finally:
            TT.close()
def Main_Pr(x):
    print (Time.year,"/",Time.month,"/",Time.day)
    print ("\n","今日top 30:")
    Top(x)
    print ("\n","要聞news:","\n")
    headline(x)
    print ("\n","娛樂news:","\n")
    entertainment(x)
    print ("\n","國際news:","\n")
    international(x)
    print ("\n","體育news:","\n")
    sports(x)
    print ("\n","財經news:","\n")
    finance(x)
    if x== 1:
        print ("\nTop最佳人氣:",Top_max,"/內容:",Top_content)
        print ("要聞最佳人氣:",headline_max,"/內容:",headline_content)
        print ("娛樂最佳人氣:",entertainment_max,"/內容:",entertainment_content)
        print ("國際最佳人氣:",international_max,"/內容:",international_content)
        print ("體育最佳人氣:",sports_max,"/內容:",sports_content)
        print ("財經最佳人氣:",finance_max,"/內容:",finance_content)
    else:
        print ("\n向來緣淺，奈何情深，既然琴瑟起，何以笙蕭默?")
def Main_Wr(x):
    try:
        if os.path.isfile("Apple_news.txt") == True:
            TT= open("Apple_news.txt","w")
            Tm  = str(Time.year)+"/"+str(Time.month)+"/"+str(Time.day)
            TT.write("\n"+Tm)
        else:
            TT= open("Apple_news.txt","w")
            Tm  = str(Time.year)+"/"+str(Time.month)+"/"+str(Time.day)
            TT.write("\n"+Tm)
        TT= open("Apple_news.txt","a")
        Top(x)
        headline(x)    
        entertainment(x)
        international(x)
        sports(x)
        finance(x)
        
        TT.write("\n\nTop最佳人氣:"+str(Top_max_w)+"/內容:"+Top_content_w)
        TT.write("\n要聞最佳人氣:"+str(headline_max_w)+"/內容:"+headline_content_w)
        TT.write("\n娛樂最佳人氣:"+str(entertainment_max_w)+"/內容:"+entertainment_content_w)
        TT.write("\n國際最佳人氣:"+str(international_max_w)+"/內容:"+international_content_w)
        TT.write("\n體育最佳人氣:"+str(sports_max_w)+"/內容:"+sports_content_w)
        TT.write("\n財經最佳人氣:"+str(finance_max_w)+"/內容:"+finance_content_w)
    except:
        print("Error!")
    finally:
        TT.close()
        print("寫入完成!!")
def Start(s):
    if s == 1:
        Star = input("你想要知道蘋果新聞全部嗎?(Yes or No):\n").upper()
        if Star == "YES" or Star == 'Y':
            Main_Pr(1)
        elif Star == "NO" or Star == 'N':
            Main_Pr(2)
        else:
            print("輸入錯誤!")
            return Start(3)
    elif s==2:
        Main_Wr(3)
    elif s == 3:
        Star = input("蘋果新聞?(Yes or No):\n").upper()
        if Star == "YES" or Star == 'Y':
            Main(True)
        elif Star == "NO" or Star == 'N':
            Main(False)
        else:
            print("輸入錯誤!")
            return Start(3)
def Mode():
    print ("Use the mode:")
    print ("1.Print")
    print ("2.Write in txt")
    m = int(input("choose: "));
    if m == 1:
        Start(1)
    elif m == 2:
        Start(2)
    else: 
        print("\n錯誤! 請重新輸入!")
        Mode()

Mode() 
