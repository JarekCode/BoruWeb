import time, datetime, pymongo, json
# ------- Mongo: Setup -------

idOfDocument = "1"

# Setting up the client
mongoClient = pymongo.MongoClient()

# Specifying the Database = 'mainDatabase'
mongodb = mongoClient.mainDatabase

# --------------------------------------------------------
# Loop
# --------------------------------------------------------
while(True):

    # --------------------------------------------------------
    # Lab Start Date
    # --------------------------------------------------------

    # Take document with the id 1 form mongo db, collection: scheduledJobs
	myQuery = { "_id" : idOfDocument }

    # Store return value in myDocument
	myDocument = mongodb.scheduledJobs.find(myQuery)

    # Reading the document and storing it into retrievedValue
	for x in myDocument:
		retrievedValue = x

    # Parse startDate myDateList[Year, Month, day]
	myDateList = retrievedValue['startDate'].split("-")

    # Year: myDateList[0]
    # Month: myDateList[1]
    # Day: myDateList[2]

    # Setting Schedule Date YYYY MM DD HH MM
	startScheduledDate = datetime.datetime(int(myDateList[0]), int(myDateList[1]), 22, 8, 33)

    # --------------------------------------------------------
    # Lab Finish Date
    # --------------------------------------------------------

	# Parse startDate endDateList[Year, Month, day]
	endDateList = retrievedValue['endDate'].split("-")

	# Year: endDateList[0]
    # Month: endDateList[1]
    # Day: endDateList[2]

	# Setting Schedule Date YYYY MM DD HH MM
	endScheduledDate = datetime.datetime(int(endDateList[0]), int(endDateList[1]), int(endDateList[2]), 8, 34)

	#Getting the current time
	currentTime = datetime.datetime.now()
	#Splitting the current time into variables to compare below
	currentYear = currentTime.year
	currentMonth = currentTime.month
	currentDay = currentTime.day
	currentHour = currentTime.hour
	currentMinute = currentTime.minute
	currentSecond = currentTime.second

	# If the scheduled time is now or has happend
	if((retrievedValue['status'] == 'pending') and (currentYear >= startScheduledDate.year) and (currentMonth >= startScheduledDate.month) and (currentDay >= startScheduledDate.day) and (currentMinute >= startScheduledDate.minute) and (currentSecond >= startScheduledDate.second)):
		print("GO GO GO GO GO")
		# Change status to "running"
		myQuery = { "_id": idOfDocument }
		newValues = { "$set": { "status": "running" } }
		mongodb.scheduledJobs.update_one(myQuery, newValues)

	if((retrievedValue['status'] == 'running') and (currentYear >= endScheduledDate.year) and (currentMonth >= endScheduledDate.month) and (currentDay >= endScheduledDate.day) and (currentMinute >= endScheduledDate.minute) and (currentSecond >= endScheduledDate.second)):
		print("STOPPPPPING")
		# Change status to "running"
		myQuery = { "_id": idOfDocument }
		newValues = { "$set": { "status": "pending" } }
		mongodb.scheduledJobs.update_one(myQuery, newValues)

	print("Waiting...")
	print("----Current Time:", currentTime, "----Scheduled Time:", startScheduledDate)
	

	# DONT MOVE !!!
	time.sleep(5)