setwd("/Users/apple/Desktop/Finance Assignment")

industryData = read.csv(file ="industry8_data.csv", head = TRUE , sep = ",")

setwd("/Users/apple/Desktop/Finance Assignment")

industryData = read.table(file ="industry8_data.csv", header = TRUE , sep = ",", quote="")
industryDataFrame = data.frame(industryData)
returnsMatrix = industryDataFrame[,5:13]

columnList = c(10,12,8)
portfolio3 = matrix(0,nrow(industryDataFrame))
for (i in columnList)
{
  portfolio3 = cbind(portfolio3, industryDataFrame[,i])
}
portfolio3 = portfolio3[,2:4]
colnames(portfolio3) = c("Beer","Finance","Steel")
excessReturnsMatrix = industryDataFrame[,14:22]

## a. Expected Excess Returns - Annualized

eRMeans = apply(excessReturnsMatrix,2,mean)*12

## b. Variance and Correlation - Annualized

rVariances = apply(industryData,2,var)*12
varianceDF = data.frame(name = names(rVariances), 
                        rank= rVariances)

## Correlations
corrMatrix = cor(returnsMatrix)
covMatrix = cov(returnsMatrix)*12

## c. Sharpe Ratio
standardDeviations = apply(returnsMatrix,2,sd)*sqrt(12)
sharpeRatio = eRMeans/standardDeviations

## d. Portfolio Frontier
weight1 = seq(0,1,by=1/1000)
weight2 = 1 - weight1

expectedReturnBeer = mean(returnsMatrix$R_I_Beer)*12   
expectedReturnFin  =  mean(returnsMatrix$R_I_Fin)*12

stdBeer = standardDeviations["R_I_Beer"]
stdFin = standardDeviations["R_I_Fin"]

expectedReturnPortfolio = weight1*expectedReturnBeer + weight2*expectedReturnFin
expecetdVarPortfolio = weight1^2*covMatrix["R_I_Beer","R_I_Beer"] + weight2^2*covMatrix["R_I_Fin","R_I_Fin"] +  2*weight1*weight2*covMatrix["R_I_Beer","R_I_Fin"]

expectedStdPortfolio = sqrt(expecetdVarPortfolio)
par(lwd =0.5, cex=0.5)

plot(expectedStdPortfolio,expectedReturnPortfolio, main="Portfolio Frontier for Beer and Finance", xlab="Portfolio Standard Deviation", ylab="Portfolio Expected Return", ylim = c(min(expectedReturnPortfolio),max(expectedReturnPortfolio)))

#result = data.frame(expectedStdPortfolio,expectedReturnPortfolio)
#result = result[result$expectedStdPortfolio<=0.21,]
#result = result[result$expectedReturnPortfolio<=0.144,]
#plot(result$expectedStdPortfolio,result$expectedReturnPortfolio, main="Portfolio Frontier for Beer and Finance", xlab="Portfolio Standard Deviation", ylab="Portfolio Expected Return")

# e. Capital Market Line for Beer, Finance - Tangency Portfolio
riskFreeRate = 0.001
#sharpeRatioPortfolio = (expectedReturnPortfolio - riskFreeRate)/expectedStdPortfolio

sharpeRatioFunction = function(weight1){

  weight2 = 1-weight1
  
  expectedReturnPortfolio = weight1*expectedReturnBeer + weight2*expectedReturnFin
  expecetdVarPortfolio = weight1^2*covMatrix["R_I_Beer","R_I_Beer"] + weight2^2*covMatrix["R_I_Fin","R_I_Fin"] +  2*weight1*weight2*covMatrix["R_I_Beer","R_I_Fin"]
  
  expectedStdPortfolio = sqrt(expecetdVarPortfolio)
  sharpeRatioPortfolio =  -(expectedReturnPortfolio - riskFreeRate) /expectedStdPortfolio
  
}

optimalSharpe=optim(par=c(0),fn=sharpeRatioFunction,lower=-2,upper=2,method = "L-BFGS-B")

# f. Adding Steel to the above portfolio
## Work on portfolio 3

muVector = seq(0.00,0.3,by=0.0005)
riskFreeRate = 0.001

optimalMarketPortfolio = function(portfolio, rf){
  
  unitVector = t(as.matrix(rep(1,ncol(portfolio))))
  returnVector = as.matrix(apply(portfolio,2,mean)*12)
  riskFreeMatrix = as.matrix(rep(rf,ncol(portfolio)))
  
  covPortfolio = cov(portfolio)*12
  inverseC = solve(covPortfolio)
  
  R=rep(rf,ncol(portfolio))
  A=(t(returnVector)-R) %*% inverseC
  B=as.double((t(returnVector)-R) %*% inverseC %*% t(unitVector))
  
  optimalReturn = (A/B) %*% returnVector
  optimalStd = sqrt((A/B) %*% covPortfolio %*% t(A/B))
  optimalSharpe2 = (optimalReturn - rf) /optimalStd
  
  return(A/B)
  
}


#### MAIN FUNCTION   ####
efficientFrontier = function(portfolio, muVector){
  
  unitVector = t(as.matrix(rep(1,ncol(portfolio))))
  returnVector = as.matrix(apply(portfolio,2,mean)*12)
  
  covPortfolio = cov(portfolio)*12
  inverseC = solve(covPortfolio)
  a1 = unitVector %*% inverseC %*% t(unitVector)
  a2 = t(returnVector) %*% inverseC %*% t(unitVector)
  a3 = unitVector %*% inverseC %*% returnVector
  a4 = t(returnVector) %*% inverseC %*% returnVector
  
  M = rbind(c(a1,a2), c(a3,a4))
  inverseM = solve(M)
 # muVector = seq(0.005,0.5,by=0.0005)
  
  multiplierVec1 = (rbind((unitVector %*% inverseC ), (t(returnVector) %*% inverseC)))
  
  varianceMatrix = NULL
  returnsMatrix2 = NULL
  
  for (mu in muVector){
    
    weight = t(inverseM %*% rbind(1,mu)) %*% multiplierVec1
    varianceMatrix = rbind(varianceMatrix,sqrt(weight %*% covPortfolio %*% t(weight)))
    returnsMatrix2 = rbind(returnsMatrix2,(weight %*% returnVector))
    
  }
  
  return (data.frame("Variance" = varianceMatrix,
                     "Returns"  = returnsMatrix2))
  
}


portfolioOptimal_3 = efficientFrontier(portfolio3,muVector)

