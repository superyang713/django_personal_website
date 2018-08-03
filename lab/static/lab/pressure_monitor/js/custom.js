var dmcp = [];
var dmct = [];
// Functions and Main
$(function() {
    // Load data
    function LoadData(allText) {
        var allTextLines = allText.split(/\r\n|\n/);
        var data = [];
        for (var i=0; i<allTextLines.length-1; i++) {
            data[i] = allTextLines[i].split("\t");
            data[i][0] = data[i][0]*1000-2082844729000;
            data[i][1] -= 12;
            dmct.push([data[i][0],data[i][2]-273.15]);
        }
        dmcp = data;
        return data;
    }

    // Get data for zoomed plots
    function getData(x1, x2, data) {
        maxl = dmcp.length-1; // maxlength
        for (var i = 0; i < maxl; i++) {
            if(data[i][0] > x1) break;
        }
        i--;
        for (var j = i; j < maxl; j++) {
            if(data[j][0] > x2) break;
        }
        return data.slice(i,j+1);
    }

    //<=======MAIN=======>
    // Plot options
    var options = {
        legend: {
            show: false
        },
        series: {
            lines: {
                show: true
            },
            points: {
                show: false
            }
        },
        xaxis: {
            mode: "time",
            timezone: "browser"
        },
        yaxis: {
            tickFormatter: function(val) {return Math.pow(10,val).toExponential(3)},
        },
        selection: {
            mode: "xy"
        }
    };

    var options2 = {
        legend: {
            show: false
        },
        series: {
            lines: {
                show: true
            },
            points: {
                show: false
            }
        },
        xaxis: {
            mode: "time",
            timezone: "browser"
        },
        colors: ["#FF7070"],
        selection: {
            mode: "xy"
        }
    };

    // Load files and initial plots
    $.ajax({
        type: "GET",
        url: "https://dl.dropbox.com/s/xd211d2jqm23txj/bakeout_info",
        dataType: "text",
        success: function(data) {
            $.plot("#dmcp", [LoadData(data)], options);$.plot("#dmct", [dmct], options2);
        }
    });

    // Zoom for plot1
    $("#dmcp").bind("plotselected", function (event, ranges) {

    // clamp the zooming to prevent eternal zoom
        if (ranges.xaxis.to - ranges.xaxis.from < 0.00001) {
            ranges.xaxis.to = ranges.xaxis.from + 0.00001;
        }

        if (ranges.yaxis.to - ranges.yaxis.from < 0.00001) {
            ranges.yaxis.to = ranges.yaxis.from + 0.00001;
        }

    // do the zooming
    $.plot("#dmcp", [getData(ranges.xaxis.from, ranges.xaxis.to,dmcp)],
        $.extend(true, {}, options, {
            xaxis: { min: ranges.xaxis.from, max: ranges.xaxis.to },
            yaxis: { min: ranges.yaxis.from, max: ranges.yaxis.to }
        }));
    });

    //	Zoom out
    $("#dmcp").dblclick(function () {
        $.plot("#dmcp", [dmcp], options);
    });

    // Zoom for plot2
    $("#dmct").bind("plotselected", function (event, ranges) {
        if (ranges.xaxis.to - ranges.xaxis.from < 0.00001) {
            ranges.xaxis.to = ranges.xaxis.from + 0.00001;
        }

        if (ranges.yaxis.to - ranges.yaxis.from < 0.00001) {
            ranges.yaxis.to = ranges.yaxis.from + 0.00001;
        }

    // do the zooming
    $.plot("#dmct", [getData(ranges.xaxis.from, ranges.xaxis.to,dmct)],
        $.extend(true, {}, options2, {
            xaxis: { min: ranges.xaxis.from, max: ranges.xaxis.to },
            yaxis: { min: ranges.yaxis.from, max: ranges.yaxis.to }
        }));
    });

    //	Zoom out
    $("#dmct").dblclick(function () {
        $.plot("#dmct", [dmct], options2);
    });
});
