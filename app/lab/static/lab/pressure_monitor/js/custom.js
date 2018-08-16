var title_temperature_plot = "Sample Temperature (C)";
var title_pressure_plot = "Main Chamber Pressure (Torr)";

var tag_pressure_little = "plot1"
var tag_temp_little = "plot2"
var tag_pressure_big = "plot3"
var tag_temp_big = "plot4"

var filepath_little = "https://dl.dropbox.com/s/xd211d2jqm23txj/bakeout_info"
var filepath_big = "https://dl.dropbox.com/s/e9x575b7k4hn6hs/bakeout"

function makeplot_little() {
    Plotly.d3.tsv(filepath_little, function(data) { processData_little(data) });
};

function makeplot_big() {
    Plotly.d3.tsv(filepath_big, function(data) { processData_big(data) });
};

function processData_little(allRows) {

    var x = [], y = [], z=[];

    for (var i=0; i<allRows.length; i++) {
        row = allRows[i];
        var unixTimestamp = row['time'];
        var datetime = new Date(unixTimestamp * 1000 - 2082844729000);
        var formattedTime = new Date(datetime.toString());

        var temp_k = row['temperature'];
        var temp_c = temp_k - 273.15;

        var pressure_raw = row['pressure'];
        var pressure_log = Math.pow(10, pressure_raw - 12);

        x.push( formattedTime );
        y.push( pressure_log );
        z.push( temp_c );
    }
    makePlotly_pressure( x, y, title_pressure_plot, tag_pressure_little);
    makePlotly_temperature( x, z, title_temperature_plot, tag_temp_little);
};

function processData_big(allRows) {

    var x = [], y = [], z=[];

    for (var i=0; i<allRows.length; i++) {
        row = allRows[i];
        var unixTimestamp = row['time'];
        var datetime = new Date(unixTimestamp * 1000 - 2082844729000);
        var formattedTime = new Date(datetime.toString());

        var temp_k = row['temperature'];
        var temp_c = temp_k - 273.15;

        var pressure_raw = row['pressure'];
        var pressure_log = Math.pow(10, pressure_raw - 12);

        x.push( formattedTime );
        y.push( pressure_log );
        z.push( temp_c );
    }
    makePlotly_pressure( x, y, title_pressure_plot, tag_pressure_big);
    makePlotly_temperature( x, z, title_temperature_plot, tag_temp_big);
};

function makePlotly_pressure( x, y, title, tag ){
    var plotDiv = document.getElementById("plot");
    var traces = [{
        x: x,
        y: y,
    }];

    var layout = {
        title: title,
        paper_bgcolor: '#BDBDBD',
        plot_bgcolor: '#BDBDBD',
        yaxis: {
            exponentformat: 'e',
            type: 'log',
            autorange: true,
        }
    };

    Plotly.newPlot(tag, traces, layout);
};

function makePlotly_temperature( x, y, title, tag ){
    var plotDiv = document.getElementById("plot");
    var traces = [{
        x: x,
        y: y,
        line: {
            color: 'rgb(128,0,128)',
            width: 3,

        }
    }];

    var layout = {
        title: title,
        paper_bgcolor: '#BDBDBD',
        plot_bgcolor: '#BDBDBD',
    };

    Plotly.newPlot(tag, traces, layout);
};
makeplot_little();
makeplot_big();
