with open("artifact.txt","r") as f:
    text=f.read()
with open("artifact.txt","w") as f:
    f.write(text +" i have added 1 line ")
print(text)
print(" end of stage 03")