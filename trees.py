from math import log
import operator
import treePlotter


# 计算香农熵
def calcShannonEnt(dataSet):  # 计算信息集的香农熵
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries  # 计算每一信息所占的频率
        shannonEnt -= prob * log(prob, 2)  # 香农熵为信息的期望值
    return shannonEnt


def creatDataSet():
    dataSet = [[1, 0, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'yes'],
               [1, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


# 传入待划分的数据集，axis是要根据哪一项去划分数据集，需要返回的特征的值（传1的话就把为1的那一行的数据返回回来了）
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]  # 把axis前的信息录入到reducedFeatVec中去
            reducedFeatVec.extend(featVec[axis + 1:])  # 把axis后的信息录入到reducedFeatVec中去
            retDataSet.append(reducedFeatVec)
    return retDataSet


# 选择使香农熵变换最大的那个特征
def chooseBestFeatureTopSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1  # 有多少个特征值
    baseEntropy = calcShannonEnt(dataSet)  # 原始数据的香农熵
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):  # 创建唯一的分类标签列表
        featList = [example[i] for example in dataSet]  # 第i列特征所能取得的特征值
        uniqueVals = set(featList)  # 筛查列表中唯一元素，以此作为特征值进行split
        newEntropy = 0.0
        for value in uniqueVals:  # 计算每种信息划分方式的信息熵
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))  # 筛查出的子数据集的大小占总数据集的概率
            newEntropy += prob * calcShannonEnt(subDataSet)  # 计算出信息熵
        infoGain = baseEntropy - newEntropy
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i  # 记录以第几个特征作为划分依据得到的香农熵最好
    return bestFeature


def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(),
                              key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def createTree(dataSet, labels):  # 两个参数分别是数据集和标签列表（即最后一列的数据）
    classList = [example[-1] for example in dataSet]  # 包含了数据集中所有的类别标签
    if classList.count(classList[0]) == len(classList):  # 当列表中所有的类标签都一样时，则直接返回该类标签
        return classList[0]
    if len(dataSet[0]) == 1:  # 当使用完了所有特征，仍然不能将数据集划分成仅包含一个类别的分组
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureTopSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}
    del (labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:  # 遍历当前所选特征包含的所有属性值
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree


myDat, labels = creatDataSet()
print(myDat)
print(labels)
a = chooseBestFeatureTopSplit(myDat)
print(a)
myTree = createTree(myDat, labels)
print(myTree)
print(treePlotter.createPlot())
