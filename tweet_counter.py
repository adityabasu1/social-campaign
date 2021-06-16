# Code to count number of tweets
# Contributor: Basu

# List of strings whose tweets need to be scraped
# Some of the strings have " AND trafficking" appended to them since the campaign used a generic name 
# leading to collection of tweets that are irrelevant to that particular campaign (For example: Look Beneath the Surface)

names = ["Look Beneath the Surface AND trafficking", "Blue Blindfold", "Blue Blindfold Campaign", "Blue Heart AND trafficking", "Stop the Traffik", "#STOPTHETRAFFIK", "PACTottawa", "#NoRoomForTrafficking", "#CanYouSeeMe AND trafficking", "#FreedomHappensNow AND trafficking", "DontCreateMoreOrphans", "#WearBlueDay",  "#StopOrphanageTourism", "ChildrenAreNotTouristAttractions AND trafficking",
         "#THINKfamilies", "DontCreateMoreOrphans AND trafficking", "KeepingFamiliesTogether", "#HelpingNotHelping", "#EndOrphanageTourism", "#COUNTALLCHILDREN", "#endslavery AND trafficking", "#FreedomHappensNow AND trafficking", "#EndSlaveryCanada AND trafficking", "#myfreedomday AND trafficking", "#NoRoomForTrafficking", "#Knowthesigns AND trafficking", "#EndHumanTrafficking", "#endtrafficking", "#humantrafficking"]

names = [word.replace(" ", "") for word in names]
print(names)

total_tweet_count = 0
for word in names:
    file_tweet_count = 0
    with open(word + ".csv", "r") as f:
        for line in f:
            file_tweet_count += 1
        total_tweet_count += file_tweet_count
        print(word, ":", file_tweet_count, "\n")

print("\nTotal number of tweets:", total_tweet_count)
