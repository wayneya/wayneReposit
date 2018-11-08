import time
import re

intdatem=0
intdated=0
inttodatem=0
inttodated=0
intdate=0.01
inttoday=0








print (intdatem,intdated,inttodatem,inttodated)
print (intdate,inttoday)

# date=input('請輸入2018日期(格式:XX/XX)')

while intdate>inttoday:
    
    if intdate!=0.01:
        print ('false,try again')
    date=input('請輸入2018日期(格式:XX/XX)')   
      
    if re.match('^1?1?/1?1?',date):
        print("符合格式")
    else:
        print("不符合格式")
    
    date=date.lstrip('0')
    strdate=" "+str(date) #調整時間格式的空白   print (date)
    print (strdate)
    
    strtoday=time.strftime("%m/%d").lstrip('0') #調整時間格式 去掉開始的0
    strtoday=" "+str(strtoday) #調整時間格式的空白   print (date)
    
    print (strtoday)
    

    a=strtoday.split('/')
    b=date.split('/')
    
    intdatem=int(b[0])
    intdated=int(b[1])
    intdate=intdatem*100+intdated
    inttodatem= int(a[0])
    inttodated= int(a[1])
    inttoday=inttodatem*100+inttodated
    
    
#date=' 2/06'













       # if can't find target particle':
print ("go to last page")
    #else can find target day article:
print ('start')
        






