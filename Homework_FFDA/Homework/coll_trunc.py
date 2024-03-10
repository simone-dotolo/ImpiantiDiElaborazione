from os import listdir

mercury = './tupling_MercuryErrorLog-200/'
bgl = './tupling_BGLErrorLog-200/'

def collisioni_mercury(fn):

    tupleFileList = [f for f in listdir(fn) if "tuple" in str(f)]

    numberOfCollisions = 0

    for i in range(len(tupleFileList)):
        tupleContent = open(fn + tupleFileList[i]).read().split('\n')

        nodesList = list(set([x.split(' ')[1] for x in tupleContent[:-1]]))

        if(len(nodesList) > 1):
            #print(f"COLLISION: on tuple {i}")
            numberOfCollisions += 1

    print(f"\nTotal number of collisions: {numberOfCollisions}")


def collisioni_bgl(fn):

    tupleFileList = [f for f in listdir(fn) if "tuple" in str(f)]

    numberOfCollisions = 0

    for i in range(len(tupleFileList)):
        tupleContent = open(fn + tupleFileList[i]).read().split('\n')

        nodesList = list(set([x.split(' ')[2].split('-')[0] for x in tupleContent[:-1]]))

        if(len(nodesList) > 1 and 'J18' in nodesList):
            #print(f"COLLISION: on tuple {i}")
            numberOfCollisions += 1

    print(f"\nTotal number of collisions: {numberOfCollisions}")

def troncamenti(fn):
    currentTuple, nextTuple = None, None

    tupleFileList = [f for f in listdir(fn) if "tuple" in str(f)]
    tupleFileList.sort(key=lambda fileName: int(fileName.split('e')[1].split('.')[0]))

    currentTuple = open(fn + tupleFileList[0]).read().split('\n')
    nextTuple = open(fn + tupleFileList[1]).read().split('\n')

    numberOfTrunactions = 0

    for i in range(1, len(tupleFileList)):
        lastNodeOfCurrent = currentTuple[-2].split(' ')[1]
        firstNodeOfNext = nextTuple[0].split(' ')[1]

        if(lastNodeOfCurrent == firstNodeOfNext):
            #print(f"TRUNCATION: {i} VS. {i+1} --- Node: {firstNodeOfNext}")
            numberOfTrunactions += 1

        currentTuple = nextTuple
        if(i+1 < len(tupleFileList)):
            nextTuple = open(fn + tupleFileList[i+1]).read().split('\n')

    print(f"\nTotal number of truncations: {numberOfTrunactions}")

collisioni_mercury(mercury)
troncamenti(mercury)
collisioni_bgl(bgl)
troncamenti(bgl)