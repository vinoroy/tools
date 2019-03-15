



function valuesVsDatesPlot(data,place,ytitle)
    {


    var traces = [];

    for (var stock in data) {

        stockData = data[stock];

        var aTrace = {
                x: stockData["DatesStr"],
                y: stockData["Data"],
                type: "scatter",
                mode: "lines",
                name: stock};

        traces.push(aTrace);


        }

    console.log(traces)

    var layout = {

        xaxis: {
            title: 'Date',
            autorange: true,
            rangeselector: {buttons: [
                {
                  count: 1,
                  label: '1m',
                  step: 'month',
                  stepmode: 'backward'
                },
                {
                  count: 6,
                  label: '6m',
                  step: 'month',
                  stepmode: 'backward'
                },
                {
                  count: 1,
                  label: '1y',
                  step: 'year',
                  stepmode: 'backward'
                },
                {
                  count: 2,
                  label: '2y',
                  step: 'year',
                  stepmode: 'backward'
                },
                {
                  count: 5,
                  label: '5y',
                  step: 'year',
                  stepmode: 'backward'
                },
                {step: 'all'}
              ]},
            rangeslider: {},
            type: 'date'
      },
      yaxis: {
        title: ytitle,

      },

    };

    Plotly.newPlot(place, traces, layout, {showSendToCloud: true});


    }


