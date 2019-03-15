import sys
sys.path.insert(0, '/Users/vince/Documents/tools/tool_site/fipi/lib')


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404

from . models import Asset, Portfolio


from django.db import models


import json


from portfolio import *



from django.db import models



def table(request):

    print('table test')


    return render(request,'fipi/table.html',context={})


def fipi(request,portfolioName,grafType):



    portfolioList = getListOfPortfolios()

    assetList = getAssetListOfPortfolio(portfolioName)

    print(assetList)

    myP = Portfolio(assetList)

    list = myP.getAssetList()

    myP.loadPortfolioPriceDataFromDB()

    assetDataVsDates = myP.getAssetDataVsDates_json(grafType)

    portfolioDataVsDates = myP.getDetailedData_json('% Est Profit')


    tableData = myP.summary.to_dict('records')

    context = {'portfolioList':portfolioList,'portfolioName':portfolioName,'portfolioDataVsDates':portfolioDataVsDates,'grafType':grafType,'assetDataVsDates':assetDataVsDates,'tableData':tableData}

    return render(request,'fipi/fipi.html',context)





def test(request):


    assetList = getAssetListOfPortfolio('Regular')

    print(assetList)

    return HttpResponse("<h1>Test</h1>")





def getAssetListOfPortfolio(portfolio):


    assetList = []


    assets = Asset.objects.filter(portfolio__name=portfolio)

    for aAsset in assets:
        asset = {}

        asset['assetID'] = aAsset.assetID
        asset['portfolio'] = aAsset.portfolio.name
        asset['assetType'] = aAsset.assetType
        asset['purchaseDate'] = aAsset.purchaseDate.strftime("%Y-%m-%d")
        asset['purchasePrice'] = aAsset.purchasePrice
        asset['saleDate'] = aAsset.saleDate
        asset['salePrice'] = aAsset.salePrice
        asset['volume'] = aAsset.volume
        asset['percentOwnership'] = aAsset.percentOwnership
        asset['priceFeedRef'] = aAsset.priceFeedRef
        asset['priceFeedType'] = aAsset.priceFeedType
        asset['debtFeedType'] = aAsset.debtFeedType
        asset['debtFeedRef'] = aAsset.debtFeedRef
        asset['thresholds'] = aAsset.thresholds

        assetList.append(asset)


    return assetList



def getListOfPortfolios():


    portfolios = ['Regular','Amelie','CELI']

    return  portfolios




