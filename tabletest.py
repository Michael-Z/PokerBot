import table
import pokerbot_FFdumb

if __name__ == "__main__":
    filename = "/Users/zhangzhihui/WorkSpace/github/PokerBot/bttt.json"
    table.generateTrainingData1(100,filename)
    #tableQ.generateTrainingData(2,filename,1000,2,3)

#def runNN(data,numEpochs=15,numDenseLayers=1,nDN=1,dropP=0.5,lr=1e-4):
#runNN(datas[3],numEpochs=100,numDenseLayers=4,nDN=256,dropP = 0.5,lr=1e-4)


# fname = sys.argv[1]
# limit = int(sys.argv[2])
# numEpochs = int(sys.argv[3])
# numLayers = int(sys.argv[4])
# numNeurons = int(sys.argv[5])
# dropP = float(sys.argv[6])
# lrate = float(sys.argv[7])
# doSave = bool(int(sys.argv[8]))
# trainOrLoad = int(sys.argv[9])
# savename = sys.argv[10]

#ffdumb.py
#def runNN(data,savename,numEpochs=15,numDenseLayers=1,nDN=1,dropP=0.5,lr=1e-4,doSave=False):
# pokerbot_FFdumb.py *./bttt.json 0 10000 4 256 0.5 le-4 1 1 ./aaa.json

#print("Creating NN structure...")
# Training with 10000 games yields the following observations:
# 4 layers with 256 nDN seems to work well: 80% test acc
# 3 layers with 64 nDN seems to be the min: 70% test acc
# 100+ epochs with lr 1e-4 shows noticeable improvement, but we cap it at 100 for speed
#runNN(datas[3],numEpochs=100,numDenseLayers=4,nDN=256,dropP = 0.5,lr=1e-4)
