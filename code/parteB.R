# For manipulating the datasets
library(dplyr)
library(readr)
# For plotting correlation matrix
library(ggcorrplot)
# Machine Learning library
library(caret)
library(rpart)
library(randomForest)
#1
arbolado <- read_csv("../data/arbolado-mza-dataset.csv")
trainset <- arbolado
arbolado_test <- read_csv("../data/arbolado-mza-dataset-test.csv")


data_train <- arbolado
data_test <- arbolado_test

majorityClassDataframe <-data_train %>% group_by(inclinacion_peligrosa) %>% summarise(total=n())
majorityClassDataframe


indexes <- which(data_train$inclinacion_peligrosa == 0)
eliminatedData <- sample(indexes, length(indexes) - 3579)
# equlibrate the majority class 
new_data_train <- data_train[-eliminatedData,]


# add circ cat to predict for a nominal value instead of a numeric value
data_train_with_circ_cat <- new_data_train %>% mutate(circ_tronco_cm_cat = ifelse(`circ_tronco_cm` <= 50,'bajo',
                                                                            ifelse(`circ_tronco_cm` > 50 & `circ_tronco_cm` <= 100, 'medio',
                                                                                   ifelse(`circ_tronco_cm` > 100 & `circ_tronco_cm` <= 150, 'alto','muy alto'))))

data_test_with_circ_cat <-  data_test %>% mutate(circ_tronco_cm_cat = ifelse(`circ_tronco_cm` <= 50,'bajo',
                                                                                  ifelse(`circ_tronco_cm` > 50 & `circ_tronco_cm` <= 100, 'medio',
                                                                                         ifelse(`circ_tronco_cm` > 100 & `circ_tronco_cm` <= 150, 'alto','muy alto'))))

#eliminate the non important values
data_filtered <- subset(data_train_with_circ_cat, select = -c(ultima_modificacion, long, lat,circ_tronco_cm ,area_seccion, nombre_seccion, seccion))
data_test_filtered <- subset(data_test_with_circ_cat, select = -c(ultima_modificacion, long, lat,circ_tronco_cm ,area_seccion, nombre_seccion, seccion))

#rpart

train_formula<-formula(inclinacion_peligrosa~altura+
                         especie+
                         diametro_tronco
)

# generamos el modelo 
tree_model<-rpart(train_formula,data=data_filtered, method = "class")
tree_model
# obtenemos la predicción
p<-predict(tree_model,data_test_filtered,type='class') 
p

#caret::confusionMatrix(p,as.factor(data_test_filtered$inclinacion_peligrosa))
write.csv(p,"result.csv")



