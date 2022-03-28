import json

courses = '{"name": "Ramiz", "languages": ["Java","Python"]}'

#Loads method parse json string and returns dictionary
dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])

#first language
print(dict_courses['languages'][0])

#all languages
for i in dict_courses['languages']:
    print(i)


#******  Parse content present in json file
with open('C:\\Users\\Ramiz-Learn\\Desktop\\Coding Practice\\backEndAutomation\\test.json') as f:
    data = json.load(f)
    print(type(data))
    print(data)
    print(data['phoneNumbers'][0]['number'])
    print(data['address']['city'])
    #without indexing
    print(type(data['phoneNumbers']))
    for num in data['phoneNumbers']:
        print(num)
        if num['type'] == "mob":
            print(num['number'])
            assert num['number'] == '7349282382'

#comparing 2 json files
with open('C:\\Users\\Ramiz-Learn\\Desktop\\Coding Practice\\backEndAutomation\\test1.json') as f1:
    data1 = json.load(f1)
    print(data1)
    print(data == data1)
    assert data == data1
