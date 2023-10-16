with open("artifacts.txt","r") as f:
    text = f.read()

with open("artifacts.txt","w") as f:
    text= f.write(text + "updated text file at Stage_03")

print(text)
print('Stage_03 is executed successfully')
