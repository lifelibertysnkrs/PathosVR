import requests
import json
import os
def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)
        f.close

shock_to_description = {'27' : 'US Credit Spread Widen 1% probability' , 
'1' : 'US Equity Market Down 1% probability' , 
'2' : '1% probability movement of European Credit Spread Widening' , 
'3' : '1% probability movement of US dollar weakening' , 
'4' : 'Rising Euro Inflation 1% probability' , 
'5' : 'US Int Rates Up 1% probability' , 
'6' : 'Oil price drops which causes short-end of the inflation curve to drop. The short end of the nominal curve is held unchanged since nominal rates in the short end are already very low. Due to the new round of quantitative easing agency mortgage rate spreads' , 
'7' : 'Credit & liquidity crisis in Asia and Russia. Dramatic treasury market rally. Shocks for DxS Factors are spreads.' , 
'8' : '1% probability movement of MSCI World Market Down' , 
'9' : '1% probability Gold Down movement' , 
'10' : 'Oil price is kept unchanged. The 10yr inflation rate drops 200 bps. The 10yr nominal rate drops to historical lows while short-term nominal rates are held constant. Agency mortgage rate spreads tighten.' , 
'11' : 'Credit & liquidity crisis stemming from the collapse of Long Term Capital Management. Simultaneous increase in Treasury rates and credit spreads with significant jump in implied volatility. Shocks for DxS Factors are percentages of spread.' , 
'12' : 'Europe Int Rates Up 1% probability' , 
'13' : '1% probability VIX Up movement' , 
'14' : '1% probability Downward movement in Europe Equity Market' , 
'15' : 'Japan Equity Market Down 1% probability' , 
'16' : 'Treasury sell-off. Shocks for DxS Factors are spreads.' , 
'17' : 'Treasury sell-off. Shocks for DxS Factors are percentages of spread.' , 
'18' : 'Credit & liquidity crisis stemming from the collapse of Long Term Capital Management. Simultaneous increase in Treasury rates and credit spreads with significant jump in implied volatility. Shocks for DxS Factors are spreads.' , 
'19' : 'Significant decrease in interest rates coupled with market volatility in the wake of the World Trade Center catastrophe. Shocks for DxS Factors are spreads.' , 
'20' : 'Credit & liquidity crisis in Asia and Russia. Dramatic treasury market rally. Shocks for DxS Factors are percentages of spread.' , 
'21' : 'Rising US Inflation 1% probability' , 
'22' : 'Significant decrease in interest rates coupled with market volatility in the wake of the World Trade Center catastrophe. Shocks for DxS Factors are percentages of spread.' , 
'23' : 'Japan Int Rates Up 1% probability' , 
'24' : 'Rising Japan Inflation 1% probability' , 
'25' : '1% probablity oil down movement' , 
'26' : 'Short-term nominal rates increase dramatically, mortgage rate spreads widen, S&P is unchanged. Shocks for the other actors in the risk model were derived using their historical correlations within the constrained factors.'
}

description_to_shock = {'US Credit Spread Widen 1% probability' : 'MS_USCRDUP' , 
'US Equity Market Down 1% probability' : 'MS_US' , 
'1% probability movement of European Credit Spread Widening' : 'MS_EUCRDUP' , 
'1% probability movement of US dollar weakening' : 'MS_USD_DN' , 
'Rising Euro Inflation 1% probability' : 'MS_EUCPIUP' , 
'US Int Rates Up 1% probability' : 'MS_USYC_UP' , 
'Oil price drops which causes short-end of the inflation curve to drop. The short end of the nominal curve is held unchanged since nominal rates in the short end are already very low. Due to the new round of quantitative easing agency mortgage rate spreads' : 'RAPID_DF' , 
'Credit & liquidity crisis in Asia and Russia. Dramatic treasury market rally. Shocks for DxS Factors are spreads.' : 'F98_ABS' , 
'1% probability movement of MSCI World Market Down' : 'MS_WORLD' , 
'1% probability Gold Down movement' : 'MSGOLD_dn' , 
'Oil price is kept unchanged. The 10yr inflation rate drops 200 bps. The 10yr nominal rate drops to historical lows while short-term nominal rates are held constant. Agency mortgage rate spreads tighten.' : 'SLOW_DF' , 
'Credit & liquidity crisis stemming from the collapse of Long Term Capital Management. Simultaneous increase in Treasury rates and credit spreads with significant jump in implied volatility. Shocks for DxS Factors are percentages of spread.' : 'PEAK1998' , 
'Europe Int Rates Up 1% probability' : 'MS_EUYC_UP' , 
'1% probability VIX Up movement' : 'MSVIX_up' , 
'1% probability Downward movement in Europe Equity Market' : 'MS_EURO' , 
'Japan Equity Market Down 1% probability' : 'MS_JAPAN' , 
'Treasury sell-off. Shocks for DxS Factors are spreads.' : 'S03_ABS' , 
'Treasury sell-off. Shocks for DxS Factors are percentages of spread.' : 'SUMMER03' , 
'Credit & liquidity crisis stemming from the collapse of Long Term Capital Management. Simultaneous increase in Treasury rates and credit spreads with significant jump in implied volatility. Shocks for DxS Factors are spreads.' : 'P98_ABS' , 
'Significant decrease in interest rates coupled with market volatility in the wake of the World Trade Center catastrophe. Shocks for DxS Factors are spreads.' : 'S11_ABS' , 
'Credit & liquidity crisis in Asia and Russia. Dramatic treasury market rally. Shocks for DxS Factors are percentages of spread.' : 'FAL1998' , 
'Rising US Inflation 1% probability' : 'MS_USCPIUP' , 
'Significant decrease in interest rates coupled with market volatility in the wake of the World Trade Center catastrophe. Shocks for DxS Factors are percentages of spread.' : 'SEP11' , 
'Japan Int Rates Up 1% probability' : 'MS_JPYC_UP' , 
'Rising Japan Inflation 1% probability' : 'MS_JPCPIUP' , 
'1% probablity oil down movement' : 'MSOIL_dn' , 
'Short-term nominal rates increase dramatically, mortgage rate spreads widen, S&P is unchanged. Shocks for the other actors in the risk model were derived using their historical correlations within the constrained factors.' : 'INFLATION'
}

for s in range(1,27):
    print str(s) + " : " + shock_to_description[str(s)]
print "\n"
shock_select = raw_input("Choose a shock> ");

stock = raw_input("Choose 4 stocks and seperate by commas> ");
stock = stock.replace(" ", "").split(",")

#stock = ['BLK', 'AAPL', 'IXN', 'MALOX']



shock_description = shock_to_description[shock_select]
shock = description_to_shock[shock_description]

filename = stock[1]+"-"+stock[2]+"-"+stock[3]+"-"+stock[0]+shock+'data.txt'
data = open(filename, 'w')


skipFields = "analyticsMap,exposures,holdings,request ,success ,timerLogs,weightAsFraction,request,factorVolatilities,stressMap,vsCommands"
vals = []
for w1 in range(0,101,20):
    for w2 in range(0,101-w1,w1+20):
        for w3 in range(0,101-w1-w2,w2+20):
            w4 = 100-w3-w2-w1
            w = [float(w1),float(w2),float(w3),float(w4)]
            position = stock[0] + "~" + str(w[0]) + '|'+stock[1] + "~" + str(w[1]) + '|' +stock[2] + "~" + str(w[2]) + '|' +stock[3] + "~" + str(w[3]) + '|'


            portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/portfolio-analysis", params={'positions' : position, "skipFields":skipFields, "calculatePerformance" : False,
"calculateStressTests" :  True})


            scenarios = json.loads(portfolioAnalysisRequest.text)

            scenario = scenarios['resultMap']['PORTFOLIOS'][0]['portfolios'][0]['riskData']['scenarios']
            for s in scenario:
                if s['title'] == shock:
                    print str(w1)+','+str(w2)+','+str(w3)+','+str(w4)+','+str(s['scenarioValue'])
                    data.write(str(w1)+','+str(w2)+','+str(w3)+','+str(s['scenarioValue']) + "\n")
                    vals.append(s['scenarioValue'])


data.close()

open("headerinfo-"+filename, "w").write(shock + "," +'0'  + "," +'0'+ "," +'0' + open(filename).read())
open("partialformat-"+filename, "w").write(stock[0]+ "," + stock[1] + "," + stock[2]+ "," + stock[3]+ '\n' + open("headerinfo-"+filename).read())
open("FORMATTED-"+filename, "w").write( str(max(vals)+.001)+ "," + str(min(vals)+.001) + ",1,1" +'\n'+ open("partialformat-"+filename).read())
#line_pre_adder(filename, stock[0]+ "," + stock[1] + "," + stock[2]+ "," + stock[3])
#line_prepender(filename, str(maxval)+ "," + str(minval) + "," + ",1,1")

os.rename("FORMATTED-"+filename, filename.replace('.txt', '.csv'))







                    
