
"""
@author: Vincent Roy [D]

This module implements the portfolio class. The class is responsible for holding and mangaging the assets in a given portfolio

"""


from tinydb import TinyDB
import securities as st
import pandas as pd
import numpy as np
import json





class Portfolio(object):
    """
    This class is the portfolio class. The class is responsible for holding and mangaing the assets in a given portfolio
 

    Attributes :

        - portfolioDBFile (string) name of the database file that contains the attributes of the assets in the portfolio
        - assets (Asset) list of assets
        - summary (DataFrame) summary table of the assets in the portfolio

    """

    def __init__(self,assetList):

        self.assetList = assetList
        self.assets = {}
        self.summary = []
        self.detailed = pd.DataFrame([])

        self.loadPortfolio()




    def loadPortfolio(self):
        """
        This method loads and creates a portfolio of assets from a database on file 

        Args :
            - None

        Return :
            - None
        """



        newAsset = None

        # for each asset in the db
        for asset in self.assetList:




            if asset['assetType'] == 'COMMON':

                # create the asset
                newAsset = st.CommonStock(asset['assetID'],
                                          asset['purchaseDate'],
                                          asset['purchasePrice'],
                                          asset['saleDate'],
                                          asset['salePrice'],
                                          asset['volume'],
                                          asset['percentOwnership'],
                                          asset['priceFeedRef'],
                                          asset['priceFeedType'])

            elif asset['assetType'] == 'PREFFERED':

                # create the asset
                newAsset = st.PreferredStock(asset['assetID'],
                                          asset['purchaseDate'],
                                          asset['purchasePrice'],
                                          asset['saleDate'],
                                          asset['salePrice'],
                                          asset['volume'],
                                          asset['percentOwnership'],
                                          asset['priceFeedRef'],
                                          asset['priceFeedType'])


            # append the new asset to the dict of assets in the portfolio
            self.assets[asset['assetID']] = newAsset



    def upDatePortfolioPriceDataInDB(self):
        """
        This method

        Args :
            - None

        Return :
            - None
        """

        for assetName in self.assets:

            self.assets[assetName].getHistoricalPriceFromSource()



    def loadPortfolioPriceDataFromDB(self):
        """
        This method

        Args :
            - None

        Return :
            - None
        """

        for assetName in self.assets:

            self.assets[assetName].setAssetData()


        self.createSummaryTable()
        self.createDetailedTable()




    def getAssetList(self):
        """
        This method creates a list of the names of the assets in the portfolio 

        Args :
            - None

        Return :
            - (list of strings) lst of the names of the assets in the portfolio
        """

        
        assetList = []

        for assetID in self.assets:
            
            assetList.append(assetID)

        return assetList


    def getGrafParams(self):
        """
        This method creates a list of the parameters that can be graphed 

        Args :
            - None

        Return :
            - (list of strings) lst of the names of the parameters that can be graphed 
        """


        return ['Acquisition', 'Close', 'Market','Est Profit', '% Est Profit']



    def createSummaryTable(self):
        """
        This method creates a summary table of the key attributes of the assets in the portfolio

        Args :
            - None

        Return :
            - None 
        """


        # create an empty dataframe with the column headings (must create a dummy row)
        summary = pd.DataFrame(
            [['Dummy', '00-00-00', np.nan, np.nan,np.nan ,np.nan, np.nan, np.nan, np.nan, np.nan]],
            columns=['Asset ID', 'Purchase date', 'Purchase price', 'Volume','Acquisition', 'Close', 'Market',
                     'Est Profit', '% Est Profit', 'Annual Return'])

        # add the perfprmance vector of each asset to the newly created dataframe
        for asset in self.assets:
            summary = pd.concat([summary, self.assets[asset].perfVector])

        # remove the dummy row
        summary = summary[1:]


        # remove date indexes
        summary = pd.DataFrame(summary.values, columns=summary.columns)

        # create a dataframe with the sum of some of the performace indicators
        total = pd.DataFrame([['Total', '', '', '', summary['Acquisition'].sum(), '', summary['Market'].sum(), summary['Est Profit'].sum(), '', '']],
                            columns=['Asset ID', 'Purchase date', 'Purchase price', 'Volume', 'Acquisition', 'Close', 'Market',
                                     'Est Profit', '% Est Profit', 'Annual Return'])


        # add the sum dataframe to the summary table
        summary = pd.concat([summary, total])

        # round the numerical values of the table
        summary.iloc[:-1, 2:] = summary.iloc[:-1, 2:].astype('float64').round(2)
        summary.iloc[-1, 4] = round(summary.iloc[-1, 4],2)
        summary.iloc[-1, 6:7] = summary.iloc[-1, 6:7].astype('float64').round(2)

        profitCode = []

        for elm in summary['Est Profit']:
            if elm >= 0:
                profitCode.append('POS')
            elif elm <= 0:
                profitCode.append('NEG')



        summary.insert(loc=0, column='Pcode', value=profitCode)


        self.summary = summary



    def createDetailedTable(self):

        # get the market for all the assets for every day
        temp = pd.DataFrame([])
        for assetName in self.assets:
            temp = pd.concat([temp, self.assets[assetName].perfMatrix['Market']], axis=1)
        self.detailed['Market'] = temp.sum(axis=1)

        # get the estimated profit for all the assets for every day
        temp = pd.DataFrame([])
        for assetName in self.assets:
            temp = pd.concat([temp, self.assets[assetName].perfMatrix['Est Profit']], axis=1)
        self.detailed['Est Profit'] = temp.sum(axis=1)

        # get the % estimated profit for all the assets for every day
        temp = pd.DataFrame([])
        for assetName in self.assets:
            temp = pd.concat([temp, self.assets[assetName].perfMatrix['Acquisition']], axis = 1)
        self.detailed['Acquisition'] = temp.sum(axis=1)
        self.detailed['% Est Profit'] = self.detailed['Est Profit'] / self.detailed['Acquisition'] * 100



    def getDetailedData_json(self,dataStr):

        # prepare the date and close
        datesAndData = self.detailed[[dataStr]]

        dates = datesAndData.index
        data = datesAndData[dataStr].values

        datesStr = dates.strftime("%Y-%m-%d").values

        comp = {'Dates': dates, 'DatesStr': datesStr, 'Data': data}

        assetTrace = {}

        assetTrace = {'DatesStr': comp['DatesStr'].tolist(), 'Data': comp['Data'].tolist()}

        portfolioTraces = {}

        portfolioTraces[dataStr] = assetTrace

        result = json.dumps(portfolioTraces)

        return result





    def getAssetDataVsDates_json(self, dataStr):
        """
        This function produces a json of the users selected asset data vs dates for all the assets in the portfolio

        Args :
            - dataStr : (string) string of the requested asset data

        Return :
            - (json) of the adjusted close vs dates for all the assets in the portfolio

        """

        portfolioTraces = {}

        # iterate over each portfolio asset to get the dates and adjusted close
        for assetID in self.assets:

            assetTrace = {}

            # extract the adjusted close price of the asset and dates
            data = self.assets[assetID].getAssetDataAndDates(dataStr)

            assetTrace= {'DatesStr':data['DatesStr'].tolist(),'Data':data['Data'].tolist()}

            portfolioTraces[assetID] = assetTrace


        result = json.dumps(portfolioTraces)

        return result

