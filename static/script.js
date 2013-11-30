

arr = []
curSort = ""
function sort(n,z){
    arr.sort(function(a,b){
	return curSort==n?a[n]-b[n]:b[n]-a[n];
    });
    if(curSort == n) curSort = "";
    else curSort = n;
    populate(arr)

    $(".sorting").attr("class","num");
    $("#tab tr:not(.game)").each(function(){
	k = $(this).children("td:eq("+z+")");
	$(k).attr("class",$(k).attr("class")+" sorting");
    });
}

function showGames(n){
    $("tr.player_"+n).toggle();
}


function multi(n){
    if(n == 4) return '<span style="color:blue;font-size:20px;font-weight:bold;">4</span>'
    else if(n == 5) return '<span style="color:red;font-size:30px;font-weight:bold;text-decoration:underline;">5</span>'
    else return n;
}


function populate(d){
    $("#tab tr").not(":eq(0)").remove();
    for(x=0;x<d.length;x++){
	$("#tab").append('<tr><td>'+d[x]["username"]+'<br /><small><a href="javascript:void(0)" onclick="showGames('+x+')">[Show Game Details]</a></td><td class="num">'+d[x]["win"]+'</td><td class="num">'+d[x]["lose"]+'</td><td class="num">'+d[x]["kdr"]+'</td><td class="num">'+d[x]["kills"]+'</td><td class="num">'+d[x]["deaths"]+'</td><td class="num">'+d[x]["assists"]+'</td><td class="num">'+d[x]["minions"]+'</td><td class="num">'+d[x]["gold"]/1000.0+'k</td><td class="num">'+multi(d[x]["multi"])+'</td><td>'+d[x]["last"]+'</td></tr>')
	
	for(y=0;y<d[x].games.length;y++){
	    k = d[x].games[y];
	    
	    $("#tab").append('<tr style="display:none" class="player_'+x+' game '+(k["win"]?"success":"danger")+'"><td colspan="3">&nbsp;</td><td class="num">'+k["kdr"]+'</td><td class="num">'+k["kills"]+'</td><td class="num">'+k["deaths"]+'</td><td class="num">'+k["assists"]+'</td><td class="num">'+k["minions"]+'</td><td class="num">'+k["gold"]/1000.0+'k</td><td class="num">'+multi(k["multi"])+'</td><td>&nbsp;</td></tr>');
	}
    }
}


$(function(){
    $("#names").submit(function(e){
	e.preventDefault ? e.preventDefault() : e.returnValue = false;

	$("#tab tr").not(":eq(0)").remove();
	$("#tab").append('<tr class="warning"><td colspan="11">Loading results... (this may take some time)</td></tr>')

	$.getJSON("/js?players="+$("#players").val().replace(" ","+"),function(d){
	    arr = d;
	    populate(d)
	});
    });
});