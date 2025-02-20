a = "Life is too short, You need Python"
#print(a[0].isupper())

#print(a.replace(" ", ""))
#print(a)
#print(a.strip())
#b = "a:b:c:d"
#print(b.split(":"))

email = input("email : ") #dongyoon7212@naver.com
#id는 dongyoon7212
email.find("@")# => index번호
email.index("@")
print(email.split("@")[0])
#print(email[:email.find("@")]) #슬라이싱