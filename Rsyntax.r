#data <- read.csv("C:\\Users\\dell\\Desktop\\data.csv") 
data <- read.csv("/Users/nancyzhang/Documents/claims.csv") 

#with out attach(), you can't fetch a specific column in future!!!
attach(data)

library(MASS)

#u have to run install.packages('tseries') first, or else it will report an error:
# Error in library(tseries) : there is no package called ‘tseries’
library(tseries)

library(forecast)


lnprice = log(claimCost_exGST[1:96])
#lnprice = data     ok
#lnprice = data[:,4]
lnprice



