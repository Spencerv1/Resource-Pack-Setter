import os
import datetime
from jproperties import Properties

resourcePackDays = [1, 4, 5]

# REMOVE ME!!!! (For testing purposes)
# resourcePackDays.append(3)

today = datetime.datetime.today()
weekday = today.weekday()
packDay = False
link = ""
year = 0

print("Current day of the week: " + str(weekday))

for i in range(2020, 2099):
    if today.year == i:
        year = i

for x in resourcePackDays:
    if weekday == x or today.date() == datetime.date(2021, 8, 12):
        packDay = True
        print("Today is a pack day.")
        break


def replaceServerProps(requirepack):
    print("Revising server.properties...")

    replacements = []
    falseStr = "require-resource-pack=false"
    trueStr = "require-resource-pack=true"
    serverProp = open("server.properties", "r+")

    if requirepack:
        newStr = trueStr
    else:
        newStr = falseStr

    for line in serverProp:
        line = line.strip()

        if falseStr in line or trueStr in line:
            replacements.append(newStr + "\n")
        elif "resource-pack=" in line:
            replacements.append("resource-pack=" + link + "\n")
        else:
            replacements.append(str(line) + "\n")

    serverProp.close()
    os.remove("server.properties")

    serverPropNew = open("server.properties", "a")
    for i in replacements:
        serverPropNew.write(i)
    serverPropNew.close()

if packDay:
    try:
        configs = Properties()
        with open('resources.properties', 'rb') as config_file:
            configs.load(config_file)

        link = str(configs.get("link").data)
        print("Resource pack link obtained from resources.properties: " + link)

        replaceServerProps(True)
    except IOError:
        print("Error: could not find resources.properties file. Please create it.")

else:
    link = ""
    print("Today is not a pack day.")
    replaceServerProps(False)

print("Done.")

