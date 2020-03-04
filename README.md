# Home_security_automation
This program sends email of the list of the names of the persons who are in the video and unknown, if any unknown appears in the video.
Working procedure:
This program captures a live video and processes it frame by frame.This program compares faces based on 128-d vector of each face.
Before that we have to store some known face encodings.While processing a video in each frame ,we have to identify the each face and we
have to compare with the stored encodings. If any match occurs we label it and we add it to the file.If it doesn't match with any 
known encodings we label it with unknown tag.
Applications:
1.It can be used in Employee attendance marking in Organisations.
2.It can be used in Organisation's areas where only particular members are allowed.
