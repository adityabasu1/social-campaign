# Code for tweet collection using snscrape
# Contributor: Basu
# Snscrape development repo used: git+https://github.com/JustAnotherArchivist/snscrape.git 

import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools
import time

# list of strings whose tweets need to be scraped
# Some of the strings have " AND trafficking" appended to them since the campaign used a generic name 
# leading to collection of tweets that are irrelevant to that particular campaign (For example: Look Beneath the Surface)

names = list()
names = ["Look Beneath the Surface AND trafficking", "Blue Blindfold", "Blue Blindfold Campaign", "Blue Heart AND trafficking", "Stop the Traffik", "#STOPTHETRAFFIK", "PACTottawa", "#NoRoomForTrafficking", "#CanYouSeeMe AND trafficking", "#FreedomHappensNow AND trafficking", "DontCreateMoreOrphans", "#WearBlueDay",  "#StopOrphanageTourism", "ChildrenAreNotTouristAttractions AND trafficking",
         "#THINKfamilies", "DontCreateMoreOrphans AND trafficking", "KeepingFamiliesTogether", "#HelpingNotHelping", "#EndOrphanageTourism", "#COUNTALLCHILDREN", "#endslavery AND trafficking", "#FreedomHappensNow AND trafficking", "#EndSlaveryCanada AND trafficking", "#myfreedomday AND trafficking", "#NoRoomForTrafficking", "#Knowthesigns AND trafficking", "#EndHumanTrafficking", "#endtrafficking", "#humantrafficking"]

# scraping from twitter and saving files
for word in names:
    tic = time.time()
    df_city = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(
        word + " since:2000-01-01 until:2021-05-01").get_items(), 50000))
    toc = time.time()
    print("Time taken for", word, ":", toc - tic, "seconds")
    word = word.replace(" ", "")
    save_to = word + ".csv"
    df_city.to_csv(save_to)
