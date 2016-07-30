#!/usr/bin/python
import mysql.connector
import requests
import pypyodbc
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from Constants import *

# -----Algorithms-----
def algorithmHandler(role, lane, winner, kills, deaths, assists, minionsKilled, totalDamageDealt, totalDamageTaken, visionWardsBoughtInGame, sightWardsBoughtInGame, wardsPlaced, totalTimeCrowdControlDealt, totalHeal, neutralMinionsKilled, neutralMinionsKilledTeamJungle, neutralMinionsKilledEnemyJungle):
    if lane == "BOTTOM" and role == "DUO_CARRY":
        return adcAlgorithm(winner, kills, deaths, assists, minionsKilled, totalDamageDealt)

    if lane == "BOTTOM" and role == "DUO_SUPPORT":
        return supportAlgorithm(winner, kills, deaths, assists, visionWardsBoughtInGame, sightWardsBoughtInGame, wardsPlaced, totalTimeCrowdControlDealt, totalHeal)

    if lane == "MIDDLE":
        return midAlgorithm(winner, kills, deaths, assists, minionsKilled, totalDamageDealt)

    if lane == "TOP":
        return topAlgorithm(winner, kills, deaths, assists, totalDamageDealt, totalDamageTaken)

    if lane == "JUNGLE":
        return jungleAlgorithm(winner, kills, deaths, assists, neutralMinionsKilled, neutralMinionsKilledTeamJungle, neutralMinionsKilledEnemyJungle)

def adcAlgorithm(winner, kills, deaths, assists, minionsKilled, totalDamageDealt):
    if winner:
        winScore = 10
    else:
        winScore = 0

    # convert any strings to integers
    kills = int(kills)
    deaths = int(deaths)
    assists = int(assists)
    minionsKilled = int(minionsKilled)
    totalDamageDealt = int(totalDamageDealt)

    if deaths != 0:
        killDeathAssistScore = (kills + (1/2 * assists)) / deaths
    else:
        killDeathAssistScore = (kills + (1/2 * assists)) + 1
    killDeathAssistScoreWeight = 3
    if killDeathAssistScore > 10:
        killDeathAssistScore = 10
    killDeathAssistScore  = killDeathAssistScore * killDeathAssistScoreWeight

    minionsKilledScore = minionsKilled / 60
    minionsKilledScoreWeight = 5
    if minionsKilledScore > 10:
        minionsKilledScore = 10
    minionsKilledScore = minionsKilledScore * minionsKilledScoreWeight

    totalDamageDealtScore = totalDamageDealt / 20000
    totalDamageDealtScoreWeight = 2
    if totalDamageDealtScore > 10:
        totalDamageDealtScore = 10
    totalDamageDealtScore = totalDamageDealtScore * totalDamageDealtScoreWeight

    score = killDeathAssistScore + minionsKilledScore + totalDamageDealtScore + winScore
    return (round(score, 4), 1)

def supportAlgorithm(winner, kills, deaths, assists, visionWardsBoughtInGame, sightWardsBoughtInGame, wardsPlaced, totalTimeCrowdControlDealt, totalHeal):
    if winner:
        winScore = 10
    else:
        winScore = 0

    # convert any strings to integers
    kills = int(kills)
    deaths = int(deaths)
    assists = int(assists)
    visionWardsBoughtInGame = int(visionWardsBoughtInGame)
    sightWardsBoughtInGame = int(sightWardsBoughtInGame)
    wardsPlaced = int(wardsPlaced)
    totalTimeCrowdControlDealt = int(totalTimeCrowdControlDealt)
    totalHeal = int(totalHeal)

    if deaths != 0:
        killDeathAssistScore = ((1/2 * kills) + assists) / deaths
    else:
        killDeathAssistScore = ((1/2 * kills) + assists) + 1
    killDeathAssistScoreWeight = 3
    if killDeathAssistScore > 10:
        killDeathAssistScore = 10
    killDeathAssistScore  = killDeathAssistScore * killDeathAssistScoreWeight

    visionWardsBoughtInGameScore = visionWardsBoughtInGame / 10
    visionWardsBoughtInGameScoreWeight = 1
    if visionWardsBoughtInGameScore > 10:
        visionWardsBoughtInGameScore = 10
    visionWardsBoughtInGameScore = visionWardsBoughtInGameScore * visionWardsBoughtInGameScoreWeight

    sightWardsBoughtInGameScore = sightWardsBoughtInGame / 10
    sightWardsBoughtInGameScoreWeight = 1
    if sightWardsBoughtInGameScore > 10:
        sightWardsBoughtInGameScore = 10
    sightWardsBoughtInGameScore = sightWardsBoughtInGameScore * sightWardsBoughtInGameScoreWeight

    wardsPlacedScore = wardsPlaced / 20
    wardsPlacedScoreWeight = 1
    if wardsPlacedScore > 10:
        wardsPlacedScore = 10
    wardsPlacedScore = wardsPlacedScore * wardsPlacedScoreWeight

    totalTimeCrowdControlDealtScore = totalTimeCrowdControlDealt / 100
    totalTimeCrowdControlDealtScoreWeight = 2
    if totalTimeCrowdControlDealtScore > 10:
        totalTimeCrowdControlDealtScore = 10
    totalTimeCrowdControlDealtScore = totalTimeCrowdControlDealtScore * totalTimeCrowdControlDealtScoreWeight

    totalHealScore = totalHeal / 100000
    totalHealScoreWeight = 2
    if totalHealScore > 10:
        totalHealScore = 10
    totalHealScore = totalHealScore * totalHealScoreWeight

    score = killDeathAssistScore + visionWardsBoughtInGameScore + sightWardsBoughtInGameScore + wardsPlacedScore + totalTimeCrowdControlDealtScore + totalHealScore
    return (round(score, 4), 2)

def midAlgorithm(winner, kills, deaths, assists, minionsKilled, totalDamageDealt):
    if winner:
        winScore = 10
    else:
        winScore = 0

    # convert any strings to integers
    kills = int(kills)
    deaths = int(deaths)
    assists = int(assists)
    minionsKilled = int(minionsKilled)
    totalDamageDealt = int(totalDamageDealt)

    if deaths != 0:
        killDeathAssistScore = (kills + (1/2 * assists)) / deaths
    else:
        killDeathAssistScore = (kills + (1/2 * assists)) + 1
    killDeathAssistScoreWeight = 3
    if killDeathAssistScore > 10:
        killDeathAssistScore = 10
    killDeathAssistScore  = killDeathAssistScore * killDeathAssistScoreWeight

    minionsKilledScore = minionsKilled / 60
    minionsKilledScoreWeight = 5
    if minionsKilledScore > 10:
        minionsKilledScore = 10
    minionsKilledScore = minionsKilledScore * minionsKilledScoreWeight

    totalDamageDealtScore = totalDamageDealt / 20000
    totalDamageDealtScoreWeight = 2
    if totalDamageDealtScore > 10:
        totalDamageDealtScore = 10
    totalDamageDealtScore = totalDamageDealtScore * totalDamageDealtScoreWeight

    score = killDeathAssistScore + minionsKilledScore + totalDamageDealtScore + winScore
    return (round(score, 4), 3)

def topAlgorithm(winner, kills, deaths, assists, totalDamageDealt, totalDamageTaken):
    if winner:
        winScore = 10
    else:
        winScore = 0

    # convert any strings to integers
    kills = int(kills)
    deaths = int(deaths)
    assists = int(assists)
    totalDamageDealt = int(totalDamageDealt)
    totalDamageTaken = int(totalDamageTaken)

    if deaths != 0:
        killDeathAssistScore = (kills + (1/2 * assists)) / deaths
    else:
        killDeathAssistScore = (kills + (1/2 * assists)) + 1
    killDeathAssistScoreWeight = 4
    if killDeathAssistScore > 10:
        killDeathAssistScore = 10
    killDeathAssistScore  = killDeathAssistScore * killDeathAssistScoreWeight

    totalDamageDealtScore = totalDamageDealt / 20000
    totalDamageDealtScoreWeight = 3
    if totalDamageDealtScore > 10:
        totalDamageDealtScore = 10
    totalDamageDealtScore = totalDamageDealtScore * totalDamageDealtScoreWeight

    totalDamageTakenScore = totalDamageDealt / 20000
    totalDamageTakenScoreWeight = 3
    if totalDamageTakenScore > 10:
        totalDamageTakenScore = 10
    totalDamageTakenScore = totalDamageTakenScore * totalDamageTakenScoreWeight

    score = killDeathAssistScore + totalDamageDealtScore + totalDamageTakenScore + winScore
    return (round(score, 4), 4)

def jungleAlgorithm(winner, kills, deaths, assists, neutralMinionsKilled, neutralMinionsKilledTeamJungle, neutralMinionsKilledEnemyJungle):
    if winner:
        winScore = 10
    else:
        winScore = 0

    # convert any strings to integers
    kills = int(kills)
    deaths = int(deaths)
    assists = int(assists)
    neutralMinionsKilled = int(neutralMinionsKilled)
    neutralMinionsKilledTeamJungle = int(neutralMinionsKilledTeamJungle)
    neutralMinionsKilledEnemyJungle = int(neutralMinionsKilledEnemyJungle)

    if deaths != 0:
        killDeathAssistScore = (kills + (1/2 * assists)) / deaths
    else:
        killDeathAssistScore = (kills + (1/2 * assists)) + 1
    killDeathAssistScoreWeight = 4
    if killDeathAssistScore > 10:
        killDeathAssistScore = 10
    killDeathAssistScore  = killDeathAssistScore * killDeathAssistScoreWeight

    neutralMinionsKilledScore = neutralMinionsKilled / 300
    neutralMinionsKilledScoreWeight = 6
    if neutralMinionsKilledScore > 10:
        neutralMinionsKilledScore = 10
    neutralMinionsKilledScore = neutralMinionsKilledScore * neutralMinionsKilledScoreWeight

    score = killDeathAssistScore + neutralMinionsKilledScore + winScore
    return (round(score, 4), 5)

# -----SQL inserts-----
def insertSummonerRecord(ID, name, score, adcScore, supportScore, midScore, topScore, jungleScore):
    connection = mysql.connector.connect(user = USER, password = PASSWORD, host = HOST, database = DATABASE)

    cursor = connection.cursor(buffered = True)

    addPlayer = ("INSERT INTO Players "
           "(PlayerID, Name, AverageScore, ADCScore, SupportScore, MidScore, TopScore, JungleScore)"
           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
           "ON DUPLICATE KEY UPDATE AverageScore = %s")
    dataPlayer = (ID, name, score, adcScore, supportScore, midScore, topScore, jungleScore, score)
    cursor.execute(addPlayer, dataPlayer)
    connection.commit()

    cursor.close()
    connection.close()

def insertMatchRecord(ID, team1PlayerIds, team1PerformanceIds, team2PlayerIds, team2PerformanceIds, winningTeam, season, queue):

    connection = mysql.connector.connect(user = USER, password = PASSWORD, host = HOST, database = DATABASE)
    cursor = connection.cursor(buffered = True)

    if queue == "TEAM_BUILDER_DRAFT_RANKED_5x5" or "RANKED_SOLO_5x5":
        if PRINT:
            print("inserting match " + str(ID) + "...")
        SQLCommand = ("INSERT INTO AllSeasons "
                    "(MatchID, Team1PlayerIDs, Team1PerformanceIDs, Team2PlayerIDs, Team2PerformanceIDs, WinningTeam) "
                    "VALUES (%s, %s, %s, %s, %s, %s)"
                    "ON DUPLICATE KEY UPDATE MatchID = " + ID)
        dataMatch = [ID, team1PlayerIds, team1PerformanceIds, team2PlayerIds, team2PerformanceIds, winningTeam]
        cursor.execute(SQLCommand, dataMatch)
        connection.commit()

    if season == "SEASON2016":
        if queue == "TEAM_BUILDER_DRAFT_RANKED_5x5" or "RANKED_SOLO_5x5":
            if PRINT:
                print("inserting match " + str(ID) + "...")
            SQLCommand = ("INSERT INTO Season2016 "
                        "(MatchID, Team1PlayerIDs, Team1PerformanceIDs, Team2PlayerIDs, Team2PerformanceIDs, WinningTeam) "
                        "VALUES (%s, %s, %s, %s, %s, %s)"
                        "ON DUPLICATE KEY UPDATE MatchID = " + ID)
            dataMatch = [ID, team1PlayerIds, team1PerformanceIds, team2PlayerIds, team2PerformanceIds, winningTeam]
            cursor.execute(SQLCommand, dataMatch)
            connection.commit()

    if season == "SEASON2015":
        if queue == "TEAM_BUILDER_DRAFT_RANKED_5x5" or "RANKED_SOLO_5x5":
            if PRINT:
                print("inserting match " + str(ID) + "...")
            SQLCommand = ("INSERT INTO Season2015 "
                        "(MatchID, Team1PlayerIDs, Team1PerformanceIDs, Team2PlayerIDs, Team2PerformanceIDs, WinningTeam) "
                        "VALUES (%s, %s, %s, %s, %s, %s)"
                        "ON DUPLICATE KEY UPDATE MatchID = " + ID)
            dataMatch = [ID, team1PlayerIds, team1PerformanceIds, team2PlayerIds, team2PerformanceIds, winningTeam]
            cursor.execute(SQLCommand, dataMatch)
            connection.commit()

    if season == "SEASON2014":
        if queue == "TEAM_BUILDER_DRAFT_RANKED_5x5" or "RANKED_SOLO_5x5":
            if PRINT:
                print("inserting match " + str(ID) + "...")
            SQLCommand = ("INSERT INTO Season2014 "
                        "(MatchID, Team1PlayerIDs, Team1PerformanceIDs, Team2PlayerIDs, Team2PerformanceIDs, WinningTeam) "
                        "VALUES (%s, %s, %s, %s, %s, %s)"
                        "ON DUPLICATE KEY UPDATE MatchID = " + ID)
            dataMatch = [ID, team1PlayerIds, team1PerformanceIds, team2PlayerIds, team2PerformanceIds, winningTeam]
            cursor.execute(SQLCommand, dataMatch)
            connection.commit()

    if season == "SEASON2013":
        if queue == "TEAM_BUILDER_DRAFT_RANKED_5x5" or "RANKED_SOLO_5x5":
            if PRINT:
                print("inserting match " + str(ID) + "...")
            SQLCommand = ("INSERT INTO Season2013 "
                        "(MatchID, Team1PlayerIDs, Team1PerformanceIDs, Team2PlayerIDs, Team2PerformanceIDs, WinningTeam) "
                        "VALUES (%s, %s, %s, %s, %s, %s)"
                        "ON DUPLICATE KEY UPDATE MatchID = " + ID)
            dataMatch = [ID, team1PlayerIds, team1PerformanceIds, team2PlayerIds, team2PerformanceIds, winningTeam]
            cursor.execute(SQLCommand, dataMatch)
            connection.commit()

    if season == "SEASON2012":
        if queue == "TEAM_BUILDER_DRAFT_RANKED_5x5" or "RANKED_SOLO_5x5":
            if PRINT:
                print("inserting match " + str(ID) + "...")
            SQLCommand = ("INSERT INTO Season2012 "
                        "(MatchID, Team1PlayerIDs, Team1PerformanceIDs, Team2PlayerIDs, Team2PerformanceIDs, WinningTeam) "
                        "VALUES (%s, %s, %s, %s, %s, %s)"
                        "ON DUPLICATE KEY UPDATE MatchID = " + ID)
            dataMatch = [ID, team1PlayerIds, team1PerformanceIds, team2PlayerIds, team2PerformanceIds, winningTeam]
            cursor.execute(SQLCommand, dataMatch)
            connection.commit()

    if season == "SEASON2011":
        if queue == "TEAM_BUILDER_DRAFT_RANKED_5x5" or "RANKED_SOLO_5x5":
            if PRINT:
                print("inserting match " + str(ID) + "...")
            SQLCommand = ("INSERT INTO Season2011 "
                        "(MatchID, Team1PlayerIDs, Team1PerformanceIDs, Team2PlayerIDs, Team2PerformanceIDs, WinningTeam) "
                        "VALUES (%s, %s, %s, %s, %s, %s)"
                        "ON DUPLICATE KEY UPDATE MatchID = " + ID)
            dataMatch = [ID, team1PlayerIds, team1PerformanceIds, team2PlayerIds, team2PerformanceIds, winningTeam]
            cursor.execute(SQLCommand, dataMatch)
            connection.commit()

    if season == "SEASON2010":
        if queue == "TEAM_BUILDER_DRAFT_RANKED_5x5" or "RANKED_SOLO_5x5":
            if PRINT:
                print("inserting match " + str(ID) + "...")
            SQLCommand = ("INSERT INTO Season2010 "
                        "(MatchID, Team1PlayerIDs, Team1PerformanceIDs, Team2PlayerIDs, Team2PerformanceIDs, WinningTeam) "
                        "VALUES (%s, %s, %s, %s, %s, %s)"
                        "ON DUPLICATE KEY UPDATE MatchID = " + ID)
            dataMatch = [ID, team1PlayerIds, team1PerformanceIds, team2PlayerIds, team2PerformanceIds, winningTeam]
            cursor.execute(SQLCommand, dataMatch)
            connection.commit()

    cursor.close()
    connection.close()

# -----Get Static Data-----
def getAllStaticData():
    getChampionList()
    getItemList()
    getMasteryList()
    getRuneList()
    getSummonerSpellList()

def getChampionList():
    URL = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion?api_key=" + KEY

    response = requests.get(URL)
    if response.status_code != 200:
        if PRINT:
            print("Couldn't get champion list. \nError, bad status code: ." + str(response.status_code))
        return

    response = response.json()

    if PRINT:
        print("Champions:\n")
    for champion in response['data']:
        id = str(response['data'][champion]['id'])
        title = str(response['data'][champion]['title'])
        name = str(response['data'][champion]['name'])
        key = str(response['data'][champion]['key'])

        if PRINT:
            print("\t" + name + ":\n")
            print("\t\tid: " + id + "\n")
            print("\t\ttitle: " + title + "\n")
            print("\t\tname: " + name + "\n")
            print("\t\tkey: " + key + "\n")

def getItemList():
    URL = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/item?api_key=" + KEY

    response = requests.get(URL)
    if response.status_code != 200:
        if PRINT:
            print("Couldn't get item list. \nError, bad status code: ." + str(response.status_code))
        return

    response = response.json()

    if PRINT:
        print("Items:\n")
    for item in response['data']:
        id = str(response['data'][item]['id'])
        if 'name' in str(response['data'][item]):
            name = str(response['data'][item]['name'])

        if PRINT:
            print("\t" + name + ":\n")
            print("\t\tid: " + id + "\n")
            print("\t\tname: " + name + "\n")

def getMasteryList():
    URL = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/mastery?api_key=" + KEY

    response = requests.get(URL)
    if response.status_code != 200:
        if PRINT:
            print("Couldn't get mastery list. \nError, bad status code: ." + str(response.status_code))
        return

    response = response.json()

    if PRINT:
        print("Masteries:\n")
    for mastery in response['data']:
        id = str(response['data'][mastery]['id'])
        name = str(response['data'][mastery]['name'])
        description = str(response['data'][mastery]['description'])

        if PRINT:
            print("\t" + name + ":\n")
            print("\t\tid: " + id + "\n")
            print("\t\tname: " + name + "\n")
            print("\t\tdescription: " + description + "\n")

def getRuneList():
    URL = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/rune?api_key=" + KEY

    response = requests.get(URL)
    if response.status_code != 200:
        if PRINT:
            print("Couldn't get rune list. \nError, bad status code: ." + str(response.status_code))
        return

    response = response.json()

    if PRINT:
        print("Runes:\n")
    for rune in response['data']:
        id = str(response['data'][rune]['id'])
        name = str(response['data'][rune]['name'])
        description = str(response['data'][rune]['description'])

        if PRINT:
            print("\t" + name + ":\n")
            print("\t\tid: " + id + "\n")
            print("\t\tname: " + name + "\n")
            print("\t\tdescription: " + description + "\n")

def getSummonerSpellList():
    URL = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/summoner-spell?api_key=" + KEY

    response = requests.get(URL)
    if response.status_code != 200:
        if PRINT:
            print("Couldn't get summoner spell list. \nError, bad status code: ." + str(response.status_code))
        return

    response = response.json()

    if PRINT:
        print("Summoner Spells:\n")
    for summonerSpell in response['data']:
        id = str(response['data'][summonerSpell]['id'])
        name = str(response['data'][summonerSpell]['name'])
        description = str(response['data'][summonerSpell]['description'])
        summonerLevel = str(response['data'][summonerSpell]['summonerLevel'])

        if PRINT:
            print("\t" + name + ":\n")
            print("\t\tid: " + id + "\n")
            print("\t\tname: " + name + "\n")
            print("\t\tdescription: " + description + "\n")
            print("\t\tsummonerLevel: " + summonerLevel + "\n")

# -----Get Summoner Data-----
def getSummonerDetails(id, score):
    id = str(id)
    URL = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/" + id + "?api_key=" + KEY

    response = requests.get(URL)
    if response.status_code != 200:
        if PRINT:
            print("Couldn't get player details. \nError, bad status code: ." + str(response.status_code))
        return

    response = response.json()
    ID = str(response[id]['id'])
    name = str(response[id]['name'])
    profileIconId = response[id]['profileIconId']
    revisionDate = response[id]['revisionDate']

    if PRINT:
        print("ID: " + ID)
        print("Name: " + name)
        print("Score: " + score)

    insertSummonerRecord(ID, name, score)

    time.sleep(1)

# -----Get Summoner Data-----
def getSummonerDetailsByName(summonerName):
    summonerName = str(summonerName)
    URL = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/" + summonerName + "?api_key=" + KEY

    response = requests.get(URL)
    if response.status_code != 200:
        if PRINT:
            print("Couldn't get player details by name. \nError, bad status code: ." + str(response.status_code))
        return "BadResponse"

    response = response.json()
    ID = str(response[summonerName]['id'])
    name = str(response[summonerName]['name'])
    profileIconId = response[summonerName]['profileIconId']
    revisionDate = response[summonerName]['revisionDate']

    if PRINT:
        print("ID: " + ID)
        print("Name: " + name)

    time.sleep(1)

    return ID, name

# -----Get Basic Match Data-----
def getSummonerMatches(id):
    summonerScore = 0
    adcScore = 0
    supportScore = 0
    midScore = 0
    topScore = 0
    jungleScore = 0

    id = str(id)
    URL = "https://na.api.pvp.net/api/lol/na/v2.2/matchlist/by-summoner/" + id + "?api_key=" + KEY

    response = requests.get(URL)
    if response.status_code != 200:
        if PRINT:
            print("Couldn't get player's matches. \nError, bad status code: ." + str(response.status_code))
        return

    response = response.json()
    matches = 0


    if response['totalGames'] > 0:
        for match in response['matches']:
            matches += 1
            matchNumber = str(matches)

            region = str(match['region'])
            platformId = str(match['platformId'])
            matchId = str(match['matchId'])
            champion = str(match['champion'])
            queue = str(match['queue'])
            season = str(match['season'])
            timestamp = str(match['timestamp'])
            lane = str(match['lane'])
            role = str(match['role'])

            if PRINT:
                print("Match: " + matchNumber + "\n")
                print("\tregion: " + region + "\n")
                print("\tplatformId: " + platformId + "\n")
                print("\tmatchId: " + matchId + "\n")
                print("\tchampion: " + champion + "\n")
                print("\tqueue: " + queue + "\n")
                print("\tseason: " + season + "\n")
                print("\ttimestamp: " + timestamp + "\n")
                print("\tlane: " + lane + "\n")
                print("\trole: " + role + "\n")

            scores = getMatchDetails(id, matchId, season, queue)
            currentScore = scores[0]
            if str(currentScore) != "None":
                summonerScore += currentScore
            else:
                matches -= 1

            if scores[1] == 1:
                currentADCScore = scores[0]
                if str(currentADCScore) != NULL:
                    adcScore += currentADCSScore

            if scores[1] == 2:
                currentSupportScore = scores[0]
                if str(currentSupportScore) != NULL:
                    supportScore += currentSupportScore

            if scores[1] == 3:
                currentMidScore = scores[0]
                if str(currentMidScore) != NULL:
                    midScore += currentMidScore

            if scores[1] == 4:
                currentTopScore = scores[0]
                if str(currentTopScore) != NULL:
                    topScore += currentTopScore

            if scores[1] == 5:
                currentJungleScore = scores[0]
                if str(currentJungleScore) != NULL:
                    jungleScore += currentJungleScore

        totalGames = str(response['totalGames'])
        if PRINT:
            print("Total Games: " + totalGames + "\n")

    time.sleep(1)

    if response['totalGames'] > 0:
        return ((summonerScore / float(totalGames)), (adcScore / float(totalGames)), (supportScore / float(totalGames)), (midScore / float(totalGames)), (topScore / float(totalGames)), (jungleScore / float(totalGames)))
    else:
        return 0

# -----Get Match Details-----
def getMatchDetails(playerId, id, season, queue):
    id = str(id)
    URL = "https://na.api.pvp.net/api/lol/na/v2.2/match/" + id + "?api_key=" + KEY

    response = requests.get(URL)
    if response.status_code != 200:
        if PRINT:
            print("Couldn't get match details. \nError, bad status code: ." + str(response.status_code))
        return

    response = response.json()

    region = str(response['region'])
    matchType = str(response['matchType'])
    matchCreation = str(response['matchCreation'])

    team1PlayerIds = ""
    team1PerformanceIds = ""
    team2PlayerIds = ""
    team2PerformanceIds = ""

    if PRINT:
        print("\tMatch Details:\n")
        print("\t\tregion: " + region + "\n")
        print("\t\tmatchType: " + matchType + "\n")
        print("\t\tmatchCreation: " + matchCreation + "\n")
        print("\t\tParticipants:\n")
    participants = 0
    for participant in response['participants']:
        participants += 1
        participantNumber = str(participants)
        if PRINT:
            print("\t\t\tParticipant " + participantNumber + ":\n")
            print("\t\t\t\tMasteries:\n")
        masteries = 0
        try:
            for mastery in participant['masteries']:
                masteries += 1
                masteryNumber = str(masteries)

                rank = str(mastery['rank'])
                masteryId = str(mastery['masteryId'])

                if PRINT:
                    print("\t\t\t\t\tMastery " + masteryNumber + ":\n")
                    print("\t\t\t\t\t\trank: " + rank + "\n")
                    print("\t\t\t\t\t\tmasteryId: " + masteryId + "\n")
        except KeyError:
            if PRINT:
                print("\t\t\t\t\tNo masteries found")

        if PRINT:
            print("\t\t\t\tRunes:\n")
        runes = 0
        try:
            for rune in participant['runes']:
                runes += 1
                runeNumber = str(runes)

                rank = str(rune['rank'])
                runeId = str(rune['runeId'])

                if PRINT:
                    print("\t\t\t\t\tRune " + runeNumber + ":\n")
                    print("\t\t\t\t\t\trank: " + rank + "\n")
                    print("\t\t\t\t\t\truneId: " + runeId + "\n")
        except KeyError:
            if PRINT:
                print("\t\t\t\t\tNo runes found")

        unrealKills = str(participant['stats']['unrealKills'])
        item0 = str(participant['stats']['item0'])
        item1 = str(participant['stats']['item1'])
        item2 = str(participant['stats']['item2'])
        item3 = str(participant['stats']['item3'])
        item4 = str(participant['stats']['item4'])
        item5 = str(participant['stats']['item5'])
        item6 = str(participant['stats']['item6'])
        totalDamageTaken = str(participant['stats']['totalDamageTaken'])
        pentaKills = str(participant['stats']['pentaKills'])
        sightWardsBoughtInGame = str(participant['stats']['sightWardsBoughtInGame'])
        winner = str(participant['stats']['winner'])
        magicDamageDealt = str(participant['stats']['magicDamageDealt'])
        wardsKilled = str(participant['stats']['wardsKilled'])
        largestCriticalStrike = str(participant['stats']['largestCriticalStrike'])
        trueDamageDealt = str(participant['stats']['trueDamageDealt'])
        doubleKills = str(participant['stats']['doubleKills'])
        physicalDamageDealt = str(participant['stats']['physicalDamageDealt'])
        tripleKills = str(participant['stats']['tripleKills'])
        deaths = str(participant['stats']['deaths'])
        #firstBloodAssist = str(participant['stats']['firstBloodAssist'])
        magicDamageDealtToChampions = str(participant['stats']['magicDamageDealtToChampions'])
        assists = str(participant['stats']['assists'])
        visionWardsBoughtInGame = str(participant['stats']['visionWardsBoughtInGame'])
        totalTimeCrowdControlDealt = str(participant['stats']['totalTimeCrowdControlDealt'])
        champLevel = str(participant['stats']['champLevel'])
        physicalDamageTaken = str(participant['stats']['physicalDamageTaken'])
        totalDamageDealt = str(participant['stats']['totalDamageDealt'])
        largestKillingSpree = str(participant['stats']['largestKillingSpree'])
        inhibitorKills = str(participant['stats']['inhibitorKills'])
        minionsKilled = str(participant['stats']['minionsKilled'])
        towerKills = str(participant['stats']['towerKills'])
        physicalDamageDealtToChampions = str(participant['stats']['physicalDamageDealtToChampions'])
        quadraKills = str(participant['stats']['quadraKills'])
        goldSpent = str(participant['stats']['goldSpent'])
        totalDamageDealtToChampions = str(participant['stats']['totalDamageDealtToChampions'])
        goldEarned = str(participant['stats']['goldEarned'])
        neutralMinionsKilledTeamJungle = str(participant['stats']['neutralMinionsKilledTeamJungle'])
        #firstBloodKill = str(participant['stats']['firstBloodKill'])
        #firstTowerKill = str(participant['stats']['firstTowerKill'])
        wardsPlaced = str(participant['stats']['wardsPlaced'])
        trueDamageDealtToChampions = str(participant['stats']['trueDamageDealtToChampions'])
        killingSprees = str(participant['stats']['killingSprees'])
        #firstInhibitorKill = str(participant['stats']['firstInhibitorKill'])
        totalScoreRank = str(participant['stats']['totalScoreRank'])
        totalUnitsHealed = str(participant['stats']['totalUnitsHealed'])
        kills = str(participant['stats']['kills'])
        #firstInhibitorAssist = str(participant['stats']['firstInhibitorAssist'])
        totalPlayerScore = str(participant['stats']['totalPlayerScore'])
        neutralMinionsKilledEnemyJungle = str(participant['stats']['neutralMinionsKilledEnemyJungle'])
        magicDamageTaken = str(participant['stats']['magicDamageTaken'])
        largestMultiKill = str(participant['stats']['largestMultiKill'])
        totalHeal = str(participant['stats']['totalHeal'])
        objectivePlayerScore = str(participant['stats']['objectivePlayerScore'])
        #firstTowerAssist = str(participant['stats']['firstTowerAssist'])
        trueDamageTaken = str(participant['stats']['trueDamageTaken'])
        neutralMinionsKilled = str(participant['stats']['neutralMinionsKilled'])
        combatPlayerScore = str(participant['stats']['combatPlayerScore'])

        if PRINT:
            print("\t\t\t\tStats:\n")
            print("\t\t\t\t\tunrealKills: " + unrealKills + "\n")
            print("\t\t\t\t\titem0: " + item0 + "\n")
            print("\t\t\t\t\titem1: " + item1 + "\n")
            print("\t\t\t\t\titem2: " + item2 + "\n")
            print("\t\t\t\t\titem3: " + item3 + "\n")
            print("\t\t\t\t\titem4: " + item4 + "\n")
            print("\t\t\t\t\titem5: " + item5 + "\n")
            print("\t\t\t\t\titem6: " + item6 + "\n")
            print("\t\t\t\t\ttotalDamageTaken: " + totalDamageTaken + "\n")
            print("\t\t\t\t\tpentaKills: " + pentaKills + "\n")
            print("\t\t\t\t\tsightWardsBoughtInGame: " + sightWardsBoughtInGame + "\n")
            print("\t\t\t\t\twinner: " + winner + "\n")
            print("\t\t\t\t\tmagicDamageDealt: " + magicDamageDealt + "\n")
            print("\t\t\t\t\twardsKilled: " + wardsKilled + "\n")
            print("\t\t\t\t\tlargestCriticalStrike: " + largestCriticalStrike + "\n")
            print("\t\t\t\t\ttrueDamageDealt: " + trueDamageDealt + "\n")
            print("\t\t\t\t\tdoubleKills: " + doubleKills + "\n")
            print("\t\t\t\t\tphysicalDamageDealt: " + physicalDamageDealt + "\n")
            print("\t\t\t\t\ttripleKills: " + tripleKills + "\n")
            print("\t\t\t\t\tdeaths: " + deaths + "\n")
            print("\t\t\t\t\tfirstBloodAssist: " + firstBloodAssist + "\n")
            print("\t\t\t\t\tmagicDamageDealtToChampions: " + magicDamageDealtToChampions + "\n")
            print("\t\t\t\t\tassists: " + assists + "\n")
            print("\t\t\t\t\tvisionWardsBoughtInGame: " + visionWardsBoughtInGame + "\n")
            print("\t\t\t\t\ttotalTimeCrowdControlDealt: " + totalTimeCrowdControlDealt + "\n")
            print("\t\t\t\t\tchampLevel: " + champLevel + "\n")
            print("\t\t\t\t\tphysicalDamageTaken: " + physicalDamageTaken + "\n")
            print("\t\t\t\t\ttotalDamageDealt: " + totalDamageDealt + "\n")
            print("\t\t\t\t\tlargestKillingSpree: " + largestKillingSpree + "\n")
            print("\t\t\t\t\tinhibitorKills: " + inhibitorKills + "\n")
            print("\t\t\t\t\tminionsKilled: " + minionsKilled + "\n")
            print("\t\t\t\t\ttowerKills: " + towerKills + "\n")
            print("\t\t\t\t\tphysicalDamageDealtToChampions: " + physicalDamageDealtToChampions + "\n")
            print("\t\t\t\t\tquadraKills: " + quadraKills + "\n")
            print("\t\t\t\t\tgoldSpent: " + goldSpent + "\n")
            print("\t\t\t\t\ttotalDamageDealtToChampions: " + totalDamageDealtToChampions + "\n")
            print("\t\t\t\t\tgoldEarned: " + goldEarned + "\n")
            print("\t\t\t\t\tneutralMinionsKilledTeamJungle: " + neutralMinionsKilledTeamJungle + "\n")
            print("\t\t\t\t\tfirstBloodKill: " + firstBloodKill + "\n")
            print("\t\t\t\t\tfirstTowerKill: " + firstTowerKill + "\n")
            print("\t\t\t\t\twardsPlaced: " + wardsPlaced + "\n")
            print("\t\t\t\t\ttrueDamageDealtToChampions: " + trueDamageDealtToChampions + "\n")
            print("\t\t\t\t\tkillingSprees: " + killingSprees + "\n")
            print("\t\t\t\t\tfirstInhibitorKill: " + firstInhibitorKill + "\n")
            print("\t\t\t\t\ttotalScoreRank: " + totalScoreRank + "\n")
            print("\t\t\t\t\ttotalUnitsHealed: " + totalUnitsHealed + "\n")
            print("\t\t\t\t\tkills: " + kills + "\n")
            print("\t\t\t\t\tfirstInhibitorAssist: " + firstInhibitorAssist + "\n")
            print("\t\t\t\t\ttotalPlayerScore: " + totalPlayerScore + "\n")
            print("\t\t\t\t\tneutralMinionsKilledEnemyJungle: " + neutralMinionsKilledEnemyJungle + "\n")
            print("\t\t\t\t\tmagicDamageTaken: " + magicDamageTaken + "\n")
            print("\t\t\t\t\tlargestMultiKill: " + largestMultiKill + "\n")
            print("\t\t\t\t\ttotalHeal: " + totalHeal + "\n")
            print("\t\t\t\t\tobjectivePlayerScore: " + objectivePlayerScore + "\n")
            print("\t\t\t\t\tfirstTowerAssist: " + firstTowerAssist + "\n")
            print("\t\t\t\t\ttrueDamageTaken: " + trueDamageTaken + "\n")
            print("\t\t\t\t\tneutralMinionsKilled: " + neutralMinionsKilled + "\n")
            print("\t\t\t\t\tcombatPlayerScore: " + combatPlayerScore + "\n")

        if PRINT:
            print("\t\t\t\tTimeline:\n")
        if 'xpDiffPerMinDeltas' in str(participant['timeline']):
            xpDiffPerMinDeltas = str(participant['timeline']['xpDiffPerMinDeltas'])
            if PRINT:
                print("\t\t\t\t\txpDiffPerMinDeltas:\n")
            if 'zeroToTen' in str(participant['timeline']['xpDiffPerMinDeltas']):
                xpDiffPerMinDeltasZeroToTen = str(participant['timeline']['xpDiffPerMinDeltas']['zeroToTen'])
                if PRINT:
                    print("\t\t\t\t\t\txpDiffPerMinDeltasZeroToTen: " + xpDiffPerMinDeltasZeroToTen + "\n")
            if 'tenToTwenty' in str(participant['timeline']['xpDiffPerMinDeltas']):
                xpDiffPerMinDeltasTenToTwenty = str(participant['timeline']['xpDiffPerMinDeltas']['tenToTwenty'])
                if PRINT:
                    print("\t\t\t\t\t\txpDiffPerMinDeltasTenToTwenty: " + xpDiffPerMinDeltasTenToTwenty + "\n")
            if 'twentyToThirty' in str(participant['timeline']['xpDiffPerMinDeltas']):
                xpDiffPerMinDeltasTwentyToThirty = str(participant['timeline']['xpDiffPerMinDeltas']['twentyToThirty'])
                if PRINT:
                    print("\t\t\t\t\t\txpDiffPerMinDeltasTwentyToThirty: " + xpDiffPerMinDeltasTwentyToThirty + "\n")
            if 'thirtyToEnd' in str(participant['timeline']['xpDiffPerMinDeltas']):
                xpDiffPerMinDeltasThirtyToEnd = str(participant['timeline']['xpDiffPerMinDeltas']['thirtyToEnd'])
                if PRINT:
                    print("\t\t\t\t\t\txpDiffPerMinDeltasThirtyToEnd: " + xpDiffPerMinDeltasThirtyToEnd + "\n")

        if 'damageTakenDiffPerMinDeltas' in str(participant['timeline']):
            damageTakenDiffPerMinDeltas = str(participant['timeline']['damageTakenDiffPerMinDeltas'])
            if PRINT:
                print("\t\t\t\t\tdamageTakenDiffPerMinDeltas:\n")
            if 'zeroToTen' in str(participant['timeline']['damageTakenDiffPerMinDeltas']):
                damageTakenDiffPerMinDeltasZeroToTen = str(participant['timeline']['damageTakenDiffPerMinDeltas']['zeroToTen'])
                if PRINT:
                    print("\t\t\t\t\t\tdamageTakenDiffPerMinDeltasZeroToTen: " + damageTakenDiffPerMinDeltasZeroToTen + "\n")
            if 'tenToTwenty' in str(participant['timeline']['damageTakenDiffPerMinDeltas']):
                damageTakenDiffPerMinDeltasTenToTwenty = str(participant['timeline']['damageTakenDiffPerMinDeltas']['tenToTwenty'])
                if PRINT:
                    print("\t\t\t\t\t\tdamageTakenDiffPerMinDeltasTenToTwenty: " + damageTakenDiffPerMinDeltasTenToTwenty + "\n")
            if 'twentyToThirty' in str(participant['timeline']['damageTakenDiffPerMinDeltas']):
                damageTakenDiffPerMinDeltasTwentyToThirty = str(participant['timeline']['damageTakenDiffPerMinDeltas']['twentyToThirty'])
                if PRINT:
                    print("\t\t\t\t\t\tdamageTakenDiffPerMinDeltasTwentyToThirty: " + damageTakenDiffPerMinDeltasTwentyToThirty + "\n")
            if 'thirtyToEnd' in str(participant['timeline']['damageTakenDiffPerMinDeltas']):
                damageTakenDiffPerMinDeltasThirtyToEnd = str(participant['timeline']['damageTakenDiffPerMinDeltas']['thirtyToEnd'])
                if PRINT:
                    print("\t\t\t\t\t\tdamageTakenDiffPerMinDeltasThirtyToEnd: " + damageTakenDiffPerMinDeltasThirtyToEnd + "\n")

        if 'xpPerMinDeltas' in str(participant['timeline']):
            xpPerMinDeltas = str(participant['timeline']['xpPerMinDeltas'])
            if PRINT:
                print("\t\t\t\t\txpPerMinDeltas:\n")
            if 'zeroToTen' in str(participant['timeline']['xpPerMinDeltas']):
                xpPerMinDeltasZeroToTen = str(participant['timeline']['xpPerMinDeltas']['zeroToTen'])
                if PRINT:
                    print("\t\t\t\t\t\txpPerMinDeltasZeroToTen: " + xpPerMinDeltasZeroToTen + "\n")
            if 'tenToTwenty' in str(participant['timeline']['xpPerMinDeltas']):
                xpPerMinDeltasTenToTwenty = str(participant['timeline']['xpPerMinDeltas']['tenToTwenty'])
                if PRINT:
                    print("\t\t\t\t\t\txpPerMinDeltasTenToTwenty: " + xpPerMinDeltasTenToTwenty + "\n")
            if 'twentyToThirty' in str(participant['timeline']['xpPerMinDeltas']):
                xpPerMinDeltasTwentyToThirty = str(participant['timeline']['xpPerMinDeltas']['twentyToThirty'])
                if PRINT:
                    print("\t\t\t\t\t\txpPerMinDeltasTwentyToThirty: " + xpPerMinDeltasTwentyToThirty + "\n")
            if 'thirtyToEnd' in str(participant['timeline']['xpPerMinDeltas']):
                xpPerMinDeltasThirtyToEnd = str(participant['timeline']['xpPerMinDeltas']['thirtyToEnd'])
                if PRINT:
                    print("\t\t\t\t\t\txpPerMinDeltasThirtyToEnd: " + xpPerMinDeltasThirtyToEnd + "\n")

        if 'goldPerMinDeltas' in str(participant['timeline']):
            goldPerMinDeltas = str(participant['timeline']['goldPerMinDeltas'])
            if PRINT:
                print("\t\t\t\t\tgoldPerMinDeltas:\n")
            if 'zeroToTen' in str(participant['timeline']['goldPerMinDeltas']):
                goldPerMinDeltasZeroToTen = str(participant['timeline']['goldPerMinDeltas']['zeroToTen'])
                if PRINT:
                    print("\t\t\t\t\t\tgoldPerMinDeltasZeroToTen: " + goldPerMinDeltasZeroToTen + "\n")
            if 'tenToTwenty' in str(participant['timeline']['goldPerMinDeltas']):
                goldPerMinDeltasTenToTwenty = str(participant['timeline']['goldPerMinDeltas']['tenToTwenty'])
                if PRINT:
                    print("\t\t\t\t\t\tgoldPerMinDeltasTenToTwenty: " + goldPerMinDeltasTenToTwenty + "\n")
            if 'twentyToThirty' in str(participant['timeline']['goldPerMinDeltas']):
                goldPerMinDeltasTwentyToThirty = str(participant['timeline']['goldPerMinDeltas']['twentyToThirty'])
                if PRINT:
                    print("\t\t\t\t\t\tgoldPerMinDeltasTwentyToThirty: " + goldPerMinDeltasTwentyToThirty + "\n")
            if 'thirtyToEnd' in str(participant['timeline']['goldPerMinDeltas']):
                goldPerMinDeltasThirtyToEnd = str(participant['timeline']['goldPerMinDeltas']['thirtyToEnd'])
                if PRINT:
                    print("\t\t\t\t\t\tgoldPerMinDeltasThirtyToEnd: " + goldPerMinDeltasThirtyToEnd + "\n")

        if 'creepsPerMinDeltas' in str(participant['timeline']):
            creepsPerMinDeltas = str(participant['timeline']['creepsPerMinDeltas'])
            if PRINT:
                print("\t\t\t\t\tcreepsPerMinDeltas:\n")
            if 'zeroToTen' in str(participant['timeline']['creepsPerMinDeltas']):
                creepsPerMinDeltasZeroToTen = str(participant['timeline']['creepsPerMinDeltas']['zeroToTen'])
                if PRINT:
                    print("\t\t\t\t\t\tcreepsPerMinDeltasZeroToTen: " + creepsPerMinDeltasZeroToTen + "\n")
            if 'tenToTwenty' in str(participant['timeline']['creepsPerMinDeltas']):
                creepsPerMinDeltasTenToTwenty = str(participant['timeline']['creepsPerMinDeltas']['tenToTwenty'])
                if PRINT:
                    print("\t\t\t\t\t\tcreepsPerMinDeltasTenToTwenty: " + creepsPerMinDeltasTenToTwenty + "\n")
            if 'twentyToThirty' in str(participant['timeline']['creepsPerMinDeltas']):
                creepsPerMinDeltasTwentyToThirty = str(participant['timeline']['creepsPerMinDeltas']['twentyToThirty'])
                if PRINT:
                    print("\t\t\t\t\t\tcreepsPerMinDeltasTwentyToThirty: " + creepsPerMinDeltasTwentyToThirty + "\n")
            if 'thirtyToEnd' in str(participant['timeline']['creepsPerMinDeltas']):
                creepsPerMinDeltasThirtyToEnd = str(participant['timeline']['creepsPerMinDeltas']['thirtyToEnd'])
                if PRINT:
                    print("\t\t\t\t\t\tcreepsPerMinDeltasThirtyToEnd: " + creepsPerMinDeltasThirtyToEnd + "\n")

        if 'csDiffPerMinDeltas' in str(participant['timeline']):
            csDiffPerMinDeltas = str(participant['timeline']['csDiffPerMinDeltas'])
            if PRINT:
                print("\t\t\t\t\tcsDiffPerMinDeltas:\n")
            if 'zeroToTen' in str(participant['timeline']['csDiffPerMinDeltas']):
                csDiffPerMinDeltasZeroToTen = str(participant['timeline']['csDiffPerMinDeltas']['zeroToTen'])
                if PRINT:
                    print("\t\t\t\t\t\tcsDiffPerMinDeltasZeroToTen: " + csDiffPerMinDeltasZeroToTen + "\n")
            if 'tenToTwenty' in str(participant['timeline']['csDiffPerMinDeltas']):
                csDiffPerMinDeltasTenToTwenty = str(participant['timeline']['csDiffPerMinDeltas']['tenToTwenty'])
                if PRINT:
                    print("\t\t\t\t\t\tcsDiffPerMinDeltasTenToTwenty: " + csDiffPerMinDeltasTenToTwenty + "\n")
            if 'twentyToThirty' in str(participant['timeline']['csDiffPerMinDeltas']):
                csDiffPerMinDeltasTwentyToThirty = str(participant['timeline']['csDiffPerMinDeltas']['twentyToThirty'])
                if PRINT:
                    print("\t\t\t\t\t\tcsDiffPerMinDeltasTwentyToThirty: " + csDiffPerMinDeltasTwentyToThirty + "\n")
            if 'thirtyToEnd' in str(participant['timeline']['csDiffPerMinDeltas']):
                csDiffPerMinDeltasThirtyToEnd = str(participant['timeline']['csDiffPerMinDeltas']['thirtyToEnd'])
                if PRINT:
                    print("\t\t\t\t\t\tcsDiffPerMinDeltasThirtyToEnd: " + csDiffPerMinDeltasThirtyToEnd + "\n")

        if 'damageTakenPerMinDeltas' in str(participant['timeline']):
            damageTakenPerMinDeltas = str(participant['timeline']['damageTakenPerMinDeltas'])
            if PRINT:
                print("\t\t\t\t\tdamageTakenPerMinDeltas:\n")
            if 'zeroToTen' in str(participant['timeline']['damageTakenPerMinDeltas']):
                damageTakenPerMinDeltasZeroToTen = str(participant['timeline']['damageTakenPerMinDeltas']['zeroToTen'])
                if PRINT:
                    print("\t\t\t\t\t\tdamageTakenPerMinDeltasZeroToTen: " + damageTakenPerMinDeltasZeroToTen + "\n")
            if 'tenToTwenty' in str(participant['timeline']['damageTakenPerMinDeltas']):
                damageTakenPerMinDeltasTenToTwenty = str(participant['timeline']['damageTakenPerMinDeltas']['tenToTwenty'])
                if PRINT:
                    print("\t\t\t\t\t\tdamageTakenPerMinDeltasTenToTwenty: " + damageTakenPerMinDeltasTenToTwenty + "\n")
            if 'twentyToThirty' in str(participant['timeline']['damageTakenPerMinDeltas']):
                damageTakenPerMinDeltasTwentyToThirty = str(participant['timeline']['damageTakenPerMinDeltas']['twentyToThirty'])
                if PRINT:
                    print("\t\t\t\t\t\tdamageTakenPerMinDeltasTwentyToThirty: " + damageTakenPerMinDeltasTwentyToThirty + "\n")
            if 'thirtyToEnd' in str(participant['timeline']['damageTakenPerMinDeltas']):
                damageTakenPerMinDeltasThirtyToEnd = str(participant['timeline']['damageTakenPerMinDeltas']['thirtyToEnd'])
                if PRINT:
                    print("\t\t\t\t\t\tdamageTakenPerMinDeltasThirtyToEnd: " + damageTakenPerMinDeltasThirtyToEnd + "\n")

        role = str(participant['timeline']['role'])
        lane = str(participant['timeline']['lane'])

        if PRINT:
            print("\t\t\t\trole: " + role + "\n")
            print("\t\t\t\tlane: " + lane + "\n")

        spell1Id = str(participant['spell1Id'])
        spell2Id = str(participant['spell2Id'])
        participantId = str(participant['participantId'])
        championId = str(participant['championId'])
        teamId = str(participant['teamId'])
        highestAchievedSeasonTier = str(participant['highestAchievedSeasonTier'])

        if PRINT:
            print("\t\t\t\tspell1Id: " + spell1Id + "\n")
            print("\t\t\t\tspell2Id: " + spell2Id + "\n")
            print("\t\t\t\tparticipantId: " + participantId + "\n")
            print("\t\t\t\tchampionId: " + championId + "\n")
            print("\t\t\t\tteamId: " + teamId + "\n")
            print("\t\t\t\thighestAchievedSeasonTier: " + highestAchievedSeasonTier + "\n")

        if PRINT:
            print("\t\tParticipantIds:\n")
        for player in response['participantIdentities']:
            currentParticipantId = str(player['participantId'])
            if currentParticipantId == participantId:
                profileIcon = str(player['player']['profileIcon'])
                matchHistoryUri = str(player['player']['matchHistoryUri'])
                summonerName = str(player['player']['summonerName'])
                summonerId = str(player['player']['summonerId'])

                if summonerId == playerId:
                    summonerScore = algorithmHandler(role, lane, winner, kills, deaths, assists, minionsKilled, totalDamageDealt, totalDamageTaken, visionWardsBoughtInGame, sightWardsBoughtInGame, wardsPlaced, totalTimeCrowdControlDealt, totalHeal, neutralMinionsKilled, neutralMinionsKilledTeamJungle, neutralMinionsKilledEnemyJungle)
                if int(teamId) == 100:
                    team1PlayerIds += str(summonerId) + "/"
                    team1PerformanceIds += str(algorithmHandler(role, lane, winner, kills, deaths, assists, minionsKilled, totalDamageDealt, totalDamageTaken, visionWardsBoughtInGame, sightWardsBoughtInGame, wardsPlaced, totalTimeCrowdControlDealt, totalHeal, neutralMinionsKilled, neutralMinionsKilledTeamJungle, neutralMinionsKilledEnemyJungle)) + "/"
                elif int(teamId) == 200:
                    team2PlayerIds += str(summonerId) + "/"
                    team2PerformanceIds += str(algorithmHandler(role, lane, winner, kills, deaths, assists, minionsKilled, totalDamageDealt, totalDamageTaken, visionWardsBoughtInGame, sightWardsBoughtInGame, wardsPlaced, totalTimeCrowdControlDealt, totalHeal, neutralMinionsKilled, neutralMinionsKilledTeamJungle, neutralMinionsKilledEnemyJungle)) + "/"

                if PRINT:
                    print("\t\t\tparticipantId:" + participantId + "\n")
                    print("\t\t\tsummonerName:" + summonerName + "\n")
                    print("\t\t\tsummonerId:" + summonerId + "\n")
                    print("\t\t\tprofileIcon:" + profileIcon + "\n")
                    print("\t\t\tmatchHistoryUri:" + matchHistoryUri + "\n\n")

        if winner == True:
            winningTeam = teamId
        elif teamId == "100":
            winningTeam = "200"
        else:
            winningTeam = "100"

    insertMatchRecord(id, team1PlayerIds, team1PerformanceIds, team2PlayerIds, team2PerformanceIds, winningTeam, season, queue)

    time.sleep(1)

    return summonerScore

def main():
    #getAllStaticData()
    #names = ["huni", "impact", "impactful", "inori", "jensen", "keith", "kfo", "kiwikid", "kirei", "konkwon", "lourlo", "maplestreet8", "mash", "matt", "meteos", "moon", "move", "ninja", "nyjacky", "patoy", "piglet", "pirean", "pobelter", "procxin", "reignover", "remi", "rush", "seraph", "shiphtur", "shrimp", "smittyj", "smoothie", "sneaky", "stixxay", "valkrin", "wildturtle", "xmithie", "yazuki", "yellowstar", "youngbin"]
    names = ["recklessmike"]

    for name in names:
        summonerDetails = getSummonerDetailsByName(name)
        if(summonerDetails != "BadResponse"):
            ID = summonerDetails[0]
            name = summonerDetails[1]
            score = getSummonerMatches(ID)
            insertSummonerRecord(ID, name, score[0], score[1], score[2], score[3], score[4], score[5])

if __name__ == "__main__":
    main()
