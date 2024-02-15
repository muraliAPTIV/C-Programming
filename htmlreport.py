contents = open("C:\\Flashing\\Smoke_test\\SITS_TC_Result.txt","r")
with open("SITS_TC_Test.html", "w") as e:
    for lines in contents.readlines():
        e.write("<pre>" + lines + "</pre> <br>\n")