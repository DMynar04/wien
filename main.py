import requests

# pull data from link
terraria = requests.get(f"http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v2/?appid=730&key={'66ADA66BA211F045986AFC6C23DCF719'}&steamid={'105600'}")

# assign json to value
terraria_stats = terraria.json()

print(terraria_stats)

