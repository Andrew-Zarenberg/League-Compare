
import urllib2
from bs4 import BeautifulSoup


def getStats(a):
    
    url = "http://www.lolking.net/search?region=NA&name=%s"%(a)
    result = urllib2.urlopen(url).read()


    k = BeautifulSoup(result.split("<!-- MATCH HISTORY -->")[1].split("<!-- MASTERIES -->")[0])



    total = {
        "win":0,
        "lose":0,
        "kills":0,
        "deaths":0,
        "assists":0,
        "minions":0,
        "gold":0
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
        t["time"] = cell[2].div.get_text().replace("Game Length","").replace("\n","").lstrip()

        # Kills/Deaths/Assists/Minions
        t["kills"] = int(cell[3].div.find_all("strong")[0].get_text())
        t["deaths"] = int(cell[3].div.find_all("strong")[1].get_text())
        t["assists"] = int(cell[3].div.find_all("strong")[2].get_text())
        t["minions"] = int(cell[4].find_all("strong")[1].get_text())

        gold = cell[4].find_all("strong")[0].get_text()
        t["gold"] = int(float(gold.replace("k",""))*1000)


        total["kills"] += t["kills"]
        total["deaths"] += t["deaths"]
        total["assists"] += t["assists"]
        total["minions"] += t["minions"]
        total["gold"] += t["gold"]
        
        m.append(t)

    # KDR
    if total["deaths"] == 0:
        total["kdr"] = 9001
    else:
        total["kdr"] = "%.2f"%(float(total["kills"])/total["deaths"])
        

    # last game played
    total["last"] = k.find_all("div",{"class":"match_details_cell"})[1].find_all("div")[3].get_text()


    # real username (with correct capitalization)
    total["username"] = k.find_all("div",{"class":"match_details_extended"})[0].find_all("td")[3].get_text()

    total["games"] = m

    return total
        


if __name__ == "__main__":
    p = raw_input("Enter username: ")
    print(str(getStats(p)))
