import math
from node import *
class DecisionTreeLearner:
    attributes = None
    attributsObjectList = None
    def __init__(self,datasetRows, datasetAttributes):
        self.rows = datasetRows
        self.attributes = datasetAttributes
        self.meausureAtribbutes()

    def meausureAtribbutes(self):
        attributeNumber = 0
        lastAttributeNumber = len(self.rows[0]) - 1
        p = 0
        n = 0
        for i in range(len(self.rows)):
            result = self.rows[i][lastAttributeNumber]
            if result == "yes":
                p = p + 1
            if result == "no":
                n = n + 1
        generalImportance = self.importanceFormula(p/(p+n), n/(p+n))
        atributtesList = []
        for attribute in self.attributes:
            if attribute == "play":
                continue
            posibilityExplored = []
            for i in range(len(self.rows)):
                #i la fila y atributte number la columna del dataset
                value = self.rows[i][attributeNumber]
                result = self.rows[i][lastAttributeNumber]
                attrValue = list(filter(lambda attrValue: attrValue.name == value,posibilityExplored))
                if  len(attrValue) == 0:
                    attributeValue = AttributeValue()
                    attributeValue.name = value
                    
                    if result == "yes":
                        attributeValue.p = attributeValue.p + 1
                    if result == "no":
                        attributeValue.n = attributeValue.n + 1
                    posibilityExplored.append(attributeValue)
                else:
                    attrValue = attrValue[0]
                    if result == "yes":
                        attrValue.p = attrValue.p + 1
                    if result == "no":
                        attrValue.n = attrValue.n + 1
            resto = 0
            for attrValue in posibilityExplored:
                nplusp = attrValue.p + attrValue.n
                resto = resto + ((nplusp)/ (p + n)) * self.importanceFormula(attrValue.p/nplusp, attrValue.n/nplusp)
            attributeObject = Attribute()
            attributeObject.ganancia = generalImportance - resto
            attributeObject.name = attribute
            attributeObject.number = attributeNumber
            atributtesList.append(attributeObject)
            posibilityExplored = []
            attributeNumber = attributeNumber + 1
        self.attributsObjectList = atributtesList


    def importanceFormula(self, first,second):
        firstTerm = 0
        secondTerm = 0
        if first >  0:
            firstTerm = - first * math.log(first, 2)
        if second > 0:
            secondTerm = second * math.log(second, 2)

        return   firstTerm - secondTerm 

    def learn(self, examples, attributes, default):
        quantityOfData = len(examples)
        if  quantityOfData == 0:
            return default
        p = 0
        n = 0
        lastAttributeNumber = len(examples[0]) - 1
        for i in range(len(examples)):
            result = examples[i][lastAttributeNumber]
            if result == "yes":
                p = p + 1
            if result == "no":
                n = n + 1
        if p == quantityOfData:
            return "yes"
        elif n == quantityOfData:
            return "no"
        elif len(attributes) == 0:
            if p > n:
                return "yes"
            else:
                return "no"
        else:
            # Sacamos el mejor
            attrGanancia = 0
            attr = None
            for attribute in attributes:
                if attribute.ganancia > attrGanancia:
                    attr = attribute
            attributes.remove(attr) 
            node = Node()  
            node.value = attr.name
            node.children = []
            m = None
            if p > n:
                m = "yes"
            else:
                m = "no"
            posibilityExplored = []
            for i in range(len(examples)):
                #i la fila y atributte number la columna del dataset
                value = examples[i][attr.number]
                result = examples[i][lastAttributeNumber]
                attrValue = list(filter(lambda attrValue: attrValue == value,posibilityExplored))
                if  len(attrValue) == 0:
                    posibilityExplored.append(value)
            for posiblity in posibilityExplored:
                
                sameValues = []
                for n in range(len(examples)):
                #i la fila y atributte number la columna del dataset
                    valueOfDataset = examples[n][attr.number]
                    if posiblity == valueOfDataset:
                        sameValues.append(examples[n])
                rows = sameValues
                sameValues = []
                attrList = self.attributsObjectList
                subTree = self.learn(rows, attrList, m)
                subNode = SubArbol()
                subNode.etiqueta = posiblity
                subNode.value = subTree
                node.children.append(subNode)
            
            
            return node


            
        

    

