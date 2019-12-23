ind = 1
size = 0
while True:
    try:
        line = input()
        size += len(line)
    except:
        if size <= 140:
            print("TWEET")
        else:
            print("MUTE")
        break
