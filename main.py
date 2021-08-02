import csv

f = open('example.csv', 'r')
f2 = open('example2.csv', 'w') #encoding='UTF8'
# rdr = csv.reader(f)
#
# # 행단위 출력
# for line in rdr:
#     print(line)

# ing_id 열값이 null 인 행은 지우기.
# [], (), 숫자 + 쉼표전까지 없애야함.
line = f.read().replace('[%]', ',')
f2.write(line)

f.close()
f2.close()

#
# lines = []
# for line in rdr:
#     if line[1] == "[%]":

