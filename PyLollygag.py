import requests
import time

def getSummonerDetails(id):
    id = str(id)
    URL = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/" + id + "?api_key=9895de8b-d837-4865-9bb2-f6ae87a4b209"

    response = requests.get(URL)
    if response.status_code != 200:
        print("Couldn't get player details. \nError, bad status code: ." + str(response.status_code))
        return

    response = response.json()
    ID = str(response[id]['id'])
    name = str(response[id]['name'])
    profileIconId = response[id]['profileIconId']
    revisionDate = response[id]['revisionDate']

    print("ID: " + ID)
    print("Name: " + name)

    time.sleep(1)

def getSummonerGames(id):
    id = str(id)
    URL = "https://na.api.pvp.net/api/lol/na/v2.2/matchlist/by-summoner/" + id + "?api_key=9895de8b-d837-4865-9bb2-f6ae87a4b209"

    response = requests.get(URL)
    if response.status_code != 200:
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
    
        totalGames = str(response['totalGames'])
        print("Total Games: " + totalGames + "\n")

    time.sleep(1)
               
def main():
    for i in range(1, 1000):
        getSummonerDetails(i)
        getSummonerGames(i)

if __name__ == "__main__":
    main()
