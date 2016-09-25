# This runs from the command line. Reads from and prints to R's working directory
# MUST type "Rscript GeneralAlgorithm-v1.0.R [args]"

# args are, in order, intput file name, beginning year, beginning period, freq, numPeriodsForecasted, output file name
#input file must be first col is dates, second col is vals

#If num args<6, terminate code
args=commandArgs(trailingOnly=TRUE)
if (length(args)<6) {
  stop("Not enough parameters")
}
library(forecast)

#params
numPeriodsForecasted=as.numeric(args[5])
filename= args[1]
outputFileName=args[6]
start=c(as.numeric(args[2]),as.numeric(args[3]))
#read in csv
data=read.csv(filename, header=TRUE, strip.white=TRUE)

series=ts(data[2], start=start, frequency=as.numeric(args[4]))
print("read as ts")
#Forecast
fc=forecast(ets(series), h=numPeriodsForecasted)
#writes "[beg year] [beg period] [numPeriodsInYear]" to file
write(sprintf("%d %d %d", as.numeric(args[2]),as.numeric(args[3]), as.numeric(args[4])),file=outputFileName )
write.table(series,file=outputFileName, sep=",",col.names=FALSE, append=TRUE )
write("-1,-1", file=outputFileName, append=TRUE )
write.table(fc$mean, col.names=FALSE, file=outputFileName, sep=",", append=TRUE)
print("written")
print(outputFileName)