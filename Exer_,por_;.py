
a = '0, 1, 2 3, 4, 5, 6, 7,'

a = a.replace(',',';')

print(a)

b = ', 1 2 3, 4,5 ,7'

a = a.replace(',',';')

print(b)

c = ', "afsg,mhaj", "abs," 2'

c = ["," ,"afsg,mhaj", "abs,","2"]

s = ";"

s = s.join(c)

print(s)


d = '0.9, 9;2, 2 3, "def;", 12'

d = [ '0.9',' 9;2',' 2 3', 'def;',' 12']

w = ";"

w = w.join(d)

print(w)

e = '0.12, "asd,as", "1,2", 1.2'

e = [ '0.12',' "asd,as"',' "1,2"',' 1.2']

v = ";"

v = v.join(e)

print(v)

f = '0, "ab\"bc;\"de", "asgdte"'

f = [ '0',' "ab\"bc;\"de"',' "asgdte"']

u = ";"

u = u.join(f)

print(u)
