 create_folds <- function(dataframe, k) {
  numberOfData = nrow(dataframe)
  numberOfDataOnEachPartition <- ceiling(numberOfData/k)
  datasplit <- split(dataframe,sample(rep(1:k,numberOfDataOnEachPartition)))
  return(datasplit)
}

datasplit <- create_folds(data_train, 9)
datasplit

cross_validation <- function(dataframe, k) {
  numberOfData = nrow(dataframe)
  numberOfDataOnEachPartition <- ceiling(numberOfData/k)
  datasplit <- split(dataframe,sample(rep(1:k,numberOfDataOnEachPartition)))
  # seleccionamos la clase y las variables que nos interesan
  train_formula<-formula(inclinacion_peligrosa~altura+
                           Circ_tronco_cm+
                           Lat+long+
                           Seccion+
                           especie)
  # generamos el modelo 
  tree_model<-rpart(train_formula,data=data_train)
  # obtenemos la predicción
  p<-predict(tree_model,data_val,type='class') 
}
