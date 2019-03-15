#!/usr/bin/env python
"""
@author: Vincent Roy [*]

This module consists of support functions for plotting the results of the models

"""


import plotly.plotly as py
import plotly.graph_objs as go

from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot



init_notebook_mode(connected=True)



def plot_AssetDataVsDates(portfoilio,dataStr):
    """
    This function produces a date vs adjusted close price plot

    Args :
        - portfolio : (dict) of the portfolio stocks
        - dataStr : (string) string of the requested asset data

    Return :
        - plot

    """

    traces = []

    # iterate over each portfolio asset
    for assetID in portfoilio.assets:

        # extract the adjusted close price of the asset and dates
        data = portfoilio.assets[assetID].getAssetDataAndDates(dataStr)

        # Create traces
        trace = go.Scatter(
            x=data['Dates'],
            y=data['Data'],
            mode='lines',
            name=assetID
        )

        traces.append(trace)


    layout = dict(
        title=dataStr,
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label='1m',
                         step='month',
                         stepmode='backward'),
                    dict(count=6,
                         label='6m',
                         step='month',
                         stepmode='backward'),

                    dict(count=1,
                         label='1y',
                         step='year',
                         stepmode='backward'),
                    dict(count=2,
                         label='2y',
                         step='year',
                         stepmode='backward'),
                    dict(step='all')
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type='date',
            title='Time'
        ),
        yaxis=dict(title=dataStr)
    )

    fig = dict(data=traces, layout=layout)

    iplot(fig, filename='basic-line')






