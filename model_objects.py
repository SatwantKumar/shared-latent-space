class model_parameters(object):

    def __init__(self, batchSize, numEpochs, firstLayerSize,
                 secondLayerSize, thirdLayerSize, encodedSize,
                 inputSize):
        self.batchSize = batchSize
        self.numEpochs = numEpochs
        self.firstLayerSize = firstLayerSize
        self.secondLayerSize = secondLayerSize
        self.thirdLayerSize = thirdLayerSize
        self.encodedSize = encodedSize
        self.inputSize = inputSize
