

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
    $("#tab tr").each(function(){
	k = $(this).children("td:eq("+z+")");
	$(k).attr("class",$(k).attr("class")+" sorting");
    });
}


function populate(d){
    $("#tab tr").not(":eq(0)").remove();
    for(x=0;x<d.length;x++){
	$("#tab").append('<tr><td>'+d[x]["username"]+'</td><td class="num">'+d[x]["win"]+'</td><td class="num">'+d[x]["lose"]+'</td><td class="num">'+d[x]["kdr"]+'</td><td class="num">'+d[x]["kills"]+'</td><td class="num">'+d[x]["deaths"]+'</td><td class="num">'+d[x]["assists"]+'</td><td class="num">'+d[x]["minions"]+'</td><td class="num">'+d[x]["gold"]+'</td><td>'+d[x]["last"]+'</td></tr>')
    }
}


$(function(){
    $("#names").submit(function(e){
	e.preventDefault ? e.preventDefault() : e.returnValue = false;

	$("#tab tr").not(":eq(0)").remove();
	$("#tab").append('<tr class="warning"><td colspan="10">Loading results... (this may take some time)</td></tr>')

	$.getJSON("/js?players="+$("#players").val().replace(" ","+"),function(d){
	    arr = d;
	    populate(d)
	});
    });
});