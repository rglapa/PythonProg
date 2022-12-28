from classification import TensorFlow

class Main:
    def __init__(self) -> None:
        self.newTense = None
    
    def runModel(self):
        self.newTense = TensorFlow()
        self.newTense.setupLayers()
        self.newTense.compandTrain()
        self.newTense.predictionModels()
        self.newTense.useModel()
test = Main()
#test.runModel()