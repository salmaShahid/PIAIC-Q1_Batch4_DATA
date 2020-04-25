import csv

with open('AppleStore.csv', encoding='utf-8') as file:
    myData = csv.reader(file)# read the data
    convertedData = list(myData) #convert into list
    # print(convertedData)
    print(convertedData)

    #for taking the average erating of apple data
    totalRating = 0

    for item in convertedData[1:]: #item in listed data [pehle 'id' ko chor kr baaqi saray]
        totalRating +=  float(item[7]) #zero se seven tk krke phr seven wala lena hay
        # print(item[7]) #user rating ka data aye ga
        # print(len(item))

    average_rating = totalRating / len(convertedData) #average nikaalnay k liye
    print(average_rating)

    #to extract the education rows in data (listed)
    educationRows = 0

    for item in convertedData[1:]:
        genre = item[11] #prime-genre wala column
        if genre == "Education" or genre == "Games":
            educationRows = educationRows + 1
        # print(genre)
        # item[4], its a price column
        # if item[4] == "0" and genre == "Education":
            # totalRating +=  float(item[7])
        # print(item[6])
    print(educationRows)

    # for items in convertedData[1:]:
    #
    #     price_categories = items[4]
    #     #to extract price
    #     price = float(items[4])
    #     if price == "0":
    #
    #         if 'free' not in price_categories:
    #             price_categories.append("free")
    #
    #     elif price > 2 and price < 5:
    #         if "cheap" not in price_categories:
    #             price_categories.append("cheap")
    #
    #     elif price > 5 and price < 20:
    #         if "normal" not in price_categories:
    #             price_categories.append("normal")
    #
    #     elif price > 20:
    #         if "expensive" not in price_categories:
    #             price_categories.append("expensive")
    #
    #     print(price_categories)

import json

data = {
    "name": "Salma",
    "city": "Faisalabad",
    "teacher": "Sbahat"
}

with open("data.json", "w") as file:
    json.dump(data, file) #to add or insert data

# with open("data.json", "r") as file:
#     myData = json.load(file) #to load data of json file
#     print(myData['name'])
