import unittest
from Network import Network
from Importer import InputData


class TestNetworkInit(unittest.TestCase):

    def testInit(self):
        
        inputData = InputData()
        network = Network(inputData)
        #For every node define certain number of people with the corresponding working Node
        for dfLand in inputData.dfListOfBundesland:
        #Sanity check if every homeNode and workNode are listed in dfTotalPeople["Kreis"]
            sanityCheck = dfLand.homeNode.isin(inputData.dfTotalPeople.Kreis)
            for ind, sane in enumerate(sanityCheck):
                self.assertTrue(sane, "Sanity Check fails for ..." + dfLand.homeNode[ind])

if __name__ == '__main__':
    unittest.main()