

from flask import Flask, render_template, request, redirect

import player
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")



def index2():
    r = ""
    p = []

    if "players" in request.args:
        for x in request.args.get("players").split(","):
            p.append(player.getStats(x.lstrip()))
            

    r += """
<table class="table table-bordered table-striped">
<tr>
  <th>Username</th>
  <th class="num">Wins</th>
  <th class="num">Losses</th>
  <th class="num">Kills</th>
  <th class="num">Deaths</th>
  <th class="num">Assists</th>
  <th class="num">Minions</th>
  <th class="num">Gold</th>
</tr>"""



    for x in p:
        r += """
<tr>
  <th class="player">%(username)s</th>
  <td class="num">%(win)d</td>
  <td class="num">%(lose)d</td>
  <td class="num">%(kills)d</td>
  <td class="num">%(deaths)d</td>
  <td class="num">%(assists)d</td>
  <td class="num">%(minions)d</td>
  <td class="num">%(gold)d</td>
</tr>"""%(x)

    r += '</table>'

    return render_template("index.html",d=r)



@app.route("/js")
def js():
    r = "["

    p = []
    if "players" in request.args:
        for x in request.args.get("players").split(","):
            p.append(json.dumps(player.getStats(x.lstrip())))

    r += ",".join(p)+"]"

    return r



if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0",port=5000)
