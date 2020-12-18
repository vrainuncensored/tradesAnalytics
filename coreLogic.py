
def categorizeDay() {
    if endingBalance > staringBalance:
        return('winning') 
    else:
        return('losing')
}


def numberOfTrades(){
    typeOfDay = categorizeDay()
    if typeOfDay == 'winning '
}

def averageVolume(date){
    quantity = 0
    for i in Order_History:
        if Order_History[i][Time] == date:
            quantity += Order_History[i][Qty]
    return quantity
}

def numOfCanceledOrders(){
    numOfCanceledOrders = 0
    for i in Order_History:
        if Order_History[i][Status] == 'Canceled':
    numOfCanceledOrders += 1
}

def quantifyOrderTypes() {
    totalMarketOrders = 0
    totalLimitOrders = 0
    for i in Order_History:
        if Order_History[i][Type] == 'MKT':
            totalMarketOrders += 1
        else: 
            totalLimitOrders += 1
}

def isShort() {
    if Order_History[i+1] == ' BUY' && Order_History[i] == 'SOLD':
        return true
}