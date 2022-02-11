import random   # Needed for Pt 4

titles = []
titleLen = []
titleDict = {}
#Part 1 - What are the titles of the videos in your channel?
print("Part 1 - What are the titles of the videos in your channel?\n")
channelIn = input("Enter a video title, one at a time please.\nInput q to stop entering video titles.\n")
while True:
    if channelIn != "q":
        titles.append(channelIn)
        channelIn = input("Another title?\n")
    elif channelIn == "q":
        break
    else:
        channelIn = input("Try again!")
print("All titles in channel:", titles, "\nNumber of titles:", len(titles), "\n")

# Part 2 - How long is each video in your channel?
print("Part 2 - How long is each video in your channel?\n")
vidTime = float(input("Enter length of videos:\n(In the same order as the above list, left to right.)\nInput 0 to stop entering lengths\n"))
while True:
    if vidTime != 0:
        titleLen.append(vidTime)
        vidTime = float(input("Another length?\n"))
    elif vidTime == 0:
        break
    else:
        vidTime = float(input("Try again!"))

print(titleLen)
for video in titles:
                   titleDict[video] = 0
print(titleDict) 
for (video, length) in titleLen:
                   titleDict[video] = titleLen[length]
                   
               
print(titleDict)               

# Part 3 - Let's talk about subscribers!
print("Part 3 - Let's talk about subscribers.")



# Part 4 - Let's compare our channel to our competitor!
print("Part 4 - Let's compare our channel to our competitor!")

