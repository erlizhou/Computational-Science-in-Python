balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def payMinimumPerMonth1(balance, annualInterestRate, monthlyPaymentRate, month):
   minMonthPayment = monthlyPaymentRate * balance
   monthUnpaidBalance = balance - minMonthPayment
   updateBalance = monthUnpaidBalance + annualInterestRate * monthUnpaidBalance / 12
   print "Month: " + str(month)
   print "Minimum monthly payment: " + str(round(minMonthPayment, 2))
   print "Remaining balance: " + str(round(updateBalance, 2))
   return updateBalance

totalPaid = 0
for i in range(1,13):
  totalPaid += monthlyPaymentRate * balance
  balance = payMinimumPerMonth1(balance, annualInterestRate, monthlyPaymentRate, i)

print "Total paid: " + str(round(totalPaid, 2))
print "Remaining balance: " + str(round(balance, 2))

balance = 3329
annualInterestRate = 0.2

def payMinimumPerMonth2(balance, minMonthPayment, annualInterestRate):
   monthInterestRate = annualInterestRate / 12.0
   monthUnpaidBalance = balance - minMonthPayment
   updateBalance = monthUnpaidBalance + monthInterestRate * monthUnpaidBalance
   return updateBalance

minMonthPayment = 10
while True:
	stored = balance
	for i in range(1,13):
		balance = payMinimumPerMonth2(balance, minMonthPayment, annualInterestRate)

	if balance < 0:
		break
	else:
		balance = stored
		minMonthPayment += 10

print "Lowest Payment: " + str(minMonthPayment)

balance = 320000
annualInterestRate = 0.2

def payMinimumPerMonth3(balance, mediumMonthPayment, annualInterestRate):
   monthInterestRate = annualInterestRate / 12
   monthUnpaidBalance = balance - mediumMonthPayment
   updateBalance = monthUnpaidBalance + monthInterestRate * monthUnpaidBalance
   return updateBalance

minMonthPayment = balance / 12.0
maxMonthPayment = (balance * ((1 + annualInterestRate / 12) ** 12)) / 12.0

while True:
	mediumMonthPayment = (minMonthPayment + maxMonthPayment) / 2
	stored = balance
	for i in range(1,13):
		balance = payMinimumPerMonth3(balance, mediumMonthPayment, annualInterestRate)

	if balance < 0:
		if (mediumMonthPayment - minMonthPayment <= 0.01):
			break
		else:
			maxMonthPayment = mediumMonthPayment
			balance = stored
	else:
		balance = stored
		minMonthPayment = mediumMonthPayment

print "Lowest Payment: " + str(round(mediumMonthPayment, 2))
