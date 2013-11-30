import urllib2
from bs4 import BeautifulSoup


def getStats(a):
    
    url = "http://www.lolking.net/search?region=NA&name=%s"%(a)
    result = urllib2.urlopen(url).read()


    k = BeautifulSoup(result.split("<!-- MATCH HISTORY -->")[1].split("<!-- MASTERIES -->")[0])



    total = {
        "time":0,
        "win":0,
        "lose":0,
        "kills":0,
        "deaths":0,
        "assists":0,
        "minions":0,
        "gold":0,
        "damage_dealt":0,
        "damage_received":0,
        "healing":0,
        "multi":0,
        "dead":0,
        "turrets":0
        }

    m = []



    for x in k.find_all("div",{"class":"match_details"}):
        t = {}
        cell = x.find_all("div",{"class":"match_details_cell"})

        # Win/Lose
        if cell[1].div.find_all("div")[1].get_text()=="Win":
            t["win"] = True
            total["win"] += 1
        else:
            t["win"] = False
            total["lose"] += 1
            

        # Game time
        try:
            t["time"] = int(cell[2].div.get_text().split("min")[0].replace("~","").replace("+","").lstrip())
        except:
            t["time"] = 0
        

        # Kills/Deaths/Assists/Minions
        t["kills"] = int(cell[3].div.find_all("strong")[0].get_text())
        t["deaths"] = int(cell[3].div.find_all("strong")[1].get_text())
        t["assists"] = int(cell[3].div.find_all("strong")[2].get_text())
        
        if t["deaths"] == 0:
            t["kdr"] = t["kills"]+t["assists"]
        else:
            t["kdr"] = "%.2f"%(float(t["kills"]+t["assists"])/t["deaths"])
        t["minions"] = int(cell[4].find_all("strong")[1].get_text())

        gold = cell[4].find_all("strong")[0].get_text()
        t["gold"] = int(float(gold.replace("k",""))*1000)


        

        # more stats
        more = k.find_all("div",{"class":"match_details_extended_stats"})[len(m)].find_all("td")

        t["damage_dealt"] = int(more[0].get_text().replace(",",""))
        t["damage_received"] = int(more[1].get_text().replace(",",""))
        t["healing"] = int(more[2].get_text().replace(",",""))
        t["multi"] = int(more[3].get_text().replace(",",""))
        t["dead"] = int(more[4].get_text().replace(",",""))
        t["turrets"] = int(more[5].get_text().replace(",",""))


        total["time"] += t["time"]
        total["kills"] += t["kills"]
        total["deaths"] += t["deaths"]
        total["assists"] += t["assists"]
        total["minions"] += t["minions"]
        total["gold"] += t["gold"]

        total["damage_dealt"] += t["damage_dealt"]
        total["damage_received"] += t["damage_received"]
        total["healing"] += t["healing"]
        total["dead"] += t["dead"]
        total["turrets"] += t["turrets"]

        total["multi"] = max(t["multi"],total["multi"])
        

        

        m.append(t)

    # KDR
    if total["deaths"] == 0:
        total["kdr"] = total["kills"]+total["assists"]
    else:
        total["kdr"] = "%.2f"%(float(total["kills"]+total["assists"])/total["deaths"])
        

    # last game played
    total["last"] = k.find_all("div",{"class":"match_details_cell"})[1].find_all("div")[3].get_text()


    # real username (with correct capitalization)
    total["username"] = k.find_all("div",{"class":"match_details_extended"})[0].find_all("td")[3].get_text()

    total["games"] = m

    return total
        


if __name__ == "__main__":
    p = raw_input("Enter username: ")
    print(str(getStats(p)))
