import json


followingDataFile = open('following.json', encoding='utf-8').read()
following= json.loads(followingDataFile)

followingList = []

for user in following["relationships_following"]:
    metaData = user["string_list_data"]
    followingList.append(metaData[0]['value'])

followerDataFile = open('followers_1.json', encoding='utf-8').read()
followers = json.loads(followerDataFile)

followerList = []

for user in followers["relationships_follower"]:
    metaData = user["string_list_data"]
    followerList.append(metaData[0]['value'])

fakeFriends = []

for user in followingList:
    if user not in followerList:
        print(user)
        fakeFriends.append(user)

# print(fakeFriends)
