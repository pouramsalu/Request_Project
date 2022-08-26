

import requests
import json
def request():
    a = requests.get("http://saral.navgurukul.org/api/courses")
    x=a.json()
    # print("No. Courses---ID")
    with open("salu.json","w") as f:
        json.dump(x,f,indent=4)
    with open("salu.json","r") as f:
        data = json.load(f)
    id= [] 
    i = 0
    while i < len(data['availableCourses']):
        print(i+1,":",data['availableCourses'][i]['name'],"---",data['availableCourses'][i]['id'])
        id.append(data['availableCourses'][i]['id'])
        i+=1 
    # print(id)
    user= int(input("**select the serial number:"))-1
    ex=requests.get("http://saral.navgurukul.org/api/courses/"+str(id[user])+"/exercises")
    a=ex.json()
    with open ("url link2.json","w")as k:
        json.dump(a,k,indent=4)
    with open ("url link2.json","r") as k:
        c=json.load(k)
    print(c) 
    j=0
    l=0
    slug=[]
    while j<len(c["data"]):
        print(l+1,c["data"][j]["name"])
        slug.append(c['data'][j]["slug"])
        l=l+1
        j=j+1
    print(slug)
    slugname=int(input("**Enter your slug number:"))-1
    sluglist=requests.get("http://saral.navgurukul.org/api/courses/"+ str(user)+"/exercise/getBySlug?slug=" + slug[slugname])
    b=sluglist.json()
    with open("slunglist.json","w") as k:
        json.dump(b,k,indent=4)
    with open("slunglist.json","r") as k:
        d=json.load(k)
    # print(d)
    # for i in range(len(slug)):
    #     s=input("enter the 'n' for next:")
    #     if s=="n":
    #         i=0
    #         if i<len(slug):
    #             print(slug[i])
    #             print(b["content"])
    #             break
    #         else:
    #             print("your page is not found")
    #             i+=1
    #             print("*")    
    s=d["name"]
    u=d["content"]
    print(s)
    print(u)
request()

# t=int(input("enter the number"))
# for i in range (t):
#     t1=int(input("enter the number"))
 
# def m(arr):
#     sum_neg=0
#     count_pos=0
#     if len(arr)==0:
#         return[]
#     i=0
#     for i in range(arr):
#         if arr[i]>0:
#             count_pos+=1
#         elif arr[i]<0:
#             sum_neg+=arr[i]
#         i+=1
#     return sum_neg,count_pos
# print(m(arr=(1,2,3,4,5,-6,-7,-8,-9)))


# # def m(arr):
#     if len(arr)==0:
#         return[]
#     pos=sum([1 for i in arr if i>0])
#     neg=sum([i for i in arr if i<0])
#     return pos,neg
# print(m(arr=(1,2,3,4,5,-6,-7,-8,-9))

