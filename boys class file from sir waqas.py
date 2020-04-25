import csv

#by simple way
# f = open("artworks_clean.csv", encoding = "utf-8")
# read = csv.reader(f)
# artwork = list(read)
# print(artwork)

#with one line
artworks = list(csv.reader(open("artworks_clean.csv",
                           encoding = "utf-8")))
# print(artworks)
print(len(artworks))

print(artworks[:3]) #pehle 3 rows

header = artworks[0] #shuru wala
artworks = artworks[1:] #Or pehle wala or baqi saray

def clean_year(str_year):
    if str_year == "":
        return str_year
    else:
        return int(str_year) #return kre ga int me year ko jokay string wala hoga

print(clean_year("1947")) #year 1947

# for i in artworks:
# #     dob = i[3]
# #     doe = i[4]
# #     sub = i[-2]
# #     print(int(sub))
# #     i[3] = clean_year(dob)
# #     i[4] = clean_year(doe)
# #     i[6] = clean_year(sub) # int(sub)
#     i[3] = clean_year(i[3])
#     i[4] = clean_year(i[4])
#     i[6] = int(i[-2]) # clean_year(i[6])
#
#     print(i)


sub_ages = []

for i in artworks:
    dob = i[3]
    sub = i[-2] # i[6]
    if type(dob) == str: # if dob == ""
        sub_ages.append(0)
    else:
        diff = sub - dob
        sub_ages.append(diff)


print(len(sub_ages))

# [0,-7,25,33,92,-2]

final_ages = []

for i in sub_ages:
    if i > 20:
        final_ages.append(i)
    else:  # elif i <= 20
        final_ages.append("unknown")  #agr 20 se choti hay to unknown krdo

print(final_ages)

i = 73
print(str(i)[:-1] + "0s") #73 ko 70 me badal dena

decades = []
for i in final_ages:
    if type(i) == str:
        decades.append(i)
    else:
        decades.append(str(i)[:-1]+"0s")

print(decades)

decades = []

for i in final_ages:
    if type(i) == int:
        dec = str(i)[:-1] + "0s"
        decades.append(dec)
    else:
        decades.append(i)

print(len(decades))

# decades_freq = {"20s":349,"30s":1953,"unknown":489}

# decades_freq = {}
#
# for i in decades:
#     if i in decades_freq:
#         decades_freq[i] += 1
#     else:
#         decades_freq[i] = 1
#
#
# print(decades_freq)
#
# decades_freq = {}
#
# for i in decades:
#     if i not in decades_freq:
#         decades_freq[i] = 1
#     elif i in decades_freq:
#         decades_freq[i] += 1


decades_freq = {}

for i in decades:
    if i not in decades_freq:
        decades_freq[i] = 1
    else:
        decades_freq[i] += 1

print(decades_freq)


for k,v in decades_freq.items():
    print("There are " + str(v) + " artworks submitted by the age of " + k )


for k,v in decades_freq.items():
    print("There are {:,} artworks submitted by the age of {}". format(v,k) )

for k,v in decades_freq.items():
    print(f"There are {v:,} artworks submitted by the age of {k}" )


a = 98647231083
print("there are {:,}".format(a))

a = 98647.2389
print("there are {value:,.2f}".format(value = a))



