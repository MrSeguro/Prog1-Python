#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 169
# 62252 Gonçalo Seguro 
# 62257 Ricardo Avelãs


import constants
import infoFromFiles
import copy
from operator import itemgetter


def mothersCriteria(sortedMoms):
	"""
	Sorts the mothers based on the following criteria: Risk, urgency, age and name,
	by this order
	Requires: A list of mothers with the criteria above
	Ensures: Organized and updated list by the standards above explained 

	"""
	
	OrderRisk = {"high":1, "medium":2, "low":3}
	OrderColor = {"red":1, "yellow":2, "green":3}
	sortedMoms.sort(key=lambda mother : (OrderRisk[mother[constants.MOTH_RISK_IDX]], \
											OrderColor[mother[constants.MOTH_URGCY_IDX]], \
										(-int(mother[constants.MOTH_AGE_IDX])), \
										mother[constants.MOTH_NAME_IDX]))
	
	return sortedMoms

def requestsCriteria (requestsList):
	"""
	 Sorts a list of lists corresponding to the infos of the requests, according to the order provided in the general specification

    Requires: requestsList is a list of lists, each of them containing infos from a request (a mother)

    Ensures: sorting of the requestsList

	"""	
	requestsList = infoFromFiles.readRequestsFile(requestsList)
	
	requestsList.sort(key = lambda mother: mother[constants.MOTH_NAME_IDX].lower())
	requestsList.sort(key = itemgetter(constants.MOTH_RISK_IDX, constants.MOTH_URGCY_IDX, constants.MOTH_AGE_IDX), reverse=True)
	                  	
	return requestsList

def doctorsCriteria(doctorsList):
    """
    Sorts the doctors based on the following criteria: experience on the job, hour planned to finish the childbirth,
    minutes accumulated since the beginning of the day, and the hours and minutes accumulated since the last break
    Requires: A list of the doctors with the criteria above
    Ensures: Organized and updated list of the doctors
    """
   
    doctorsList.sort(key=lambda doctor: (
        doctor[constants.DOCT_PRVIS_BIRTH_IDX],
        -int(doctor[constants.DOCT_EXP_IDX]), #Sort doctors by experience in descending order
        (240 - doctor[constants.DOCT_DURATION_BIRTH_IDX]) * -1, #Sort the doctor who takes the longest time to pause
        (2400 - doctor[constants.DOCT_REST_TIME_IDX]) * -1, #Sort the doctor who takes the longest time to weekly rest
        doctor[constants.DOCT_NAME_IDX] #
    ))

    return doctorsList


def ScheduleCriteria(schedulesList, failedSchedulesListDict=[]):
	"""
	Sorts a list of lists corresponding to the infos of the schedules, according to the order provided in the general specification

	Requires: schedulesList is a list of lists, each of them containing infos from a schedule
	(optional) listOfFailedSchedulesDict is a list of dictionaries, each of them containing the infos from a failed schedule

	Ensures: sorting of the schedulesList, with the inclusion of failed schedules (if any was given)
	"""

	if len(failedSchedulesListDict) < 1: 
		schedulesList.sort(key = lambda s : (s[constants.SCHEDULE_TIME_IDX], s[constants.SCHEDULE_MOTH_IDX].lower()))
	
	else:
		# failed schedules are sorted by themselves by the order of priority of the mothers 
		# The failed schedules have to appear together
		#The name of the first mother must be included if there is a failed schedule
		failedSchedulesListDict.sort(key = lambda s : s["name"].lower())
		failedSchedulesListDict.sort(key = itemgetter("risk", "urgency", "age"), reverse=True)   
		
		#The failed schedules should be ordered according to the mothers' priority

		failedSchedulesList = [[x["time"], x["name"], x["redirect message"]] for x in failedSchedulesListDict]   
				# Lists all failed schedules
				#includes the time, name of the mother, and the message to be displayed

		# gets the first failed sched, appends and sorts it into the list of all schedules
		firstFailedSchedule = copy.copy(failedSchedulesList[0])
		schedulesList.append(firstFailedSchedule)
		schedulesList.sort(key = lambda s : (s[constants.SCHEDULE_TIME_IDX], s[constants.SCHEDULE_MOTH_IDX].lower()))
		if len(failedSchedulesList) > 1:
			for i in range(1, len(failedSchedulesList)):
				schedulesList.insert(schedulesList.index(firstFailedSchedule)+i, copy.failedSchedulesList[i])
		
		return schedulesList

def updateSchedule(doctors, requests, previousSched, nextTime):
	"""
    Update birth assistance schedule assigning the given birth assistance requested
    to the given doctors, taking into account a previous schedule.
	
	Requires:
	doctors is a list of lists with the structure as in the output of
	infoFromFiles.readDoctorsFile concerning the time of previous schedule;
	requests is a list of lists with the structure as in the output of 
	infoFromFile.readRequestsFile concerning the current update time;
	previousSched is a list of lists with the structure as in the output of
	infoFromFiles.readScheduleFile concerning the previous update time;
	Ensures:
	a list of birth assistances, representing the schedule updated at
	the current update time (= previous update time + 30 minutes),
	assigned according to the conditions indicated in the general specification
	of the project (omitted here for the sake of readability).
	"""
	
	presentSchedule = copy.deepcopy(previousSched)
	failedSchedules = []
	doctorsCriteria(doctors)
	mothersCriteria(requests)

	for k in previousSched:
		if k[constants.SCHEDULE_TIME_IDX] <= nextTime:
			presentSchedule.remove(k)

	for mothers in requests:
		High_Risk = True if mothers[constants.MOTH_RISK_IDX] == 3 else False
									
		DoctorFound = False
		j= 0
		while DoctorFound == False and j < len(doctors):
			listdoctor = doctors[j]

			if(listdoctor[constants.DOCT_PRVIS_BIRTH_IDX] != -1) and \
															(listdoctor[constants.DOCT_PRVIS_BIRTH_IDX] + constants.BIRTH_TIME_IDX \
														   <=constants.CLOSE_TIME_IDX) and ((not High_Risk) or \
													 (High_Risk and listdoctor[constants.DOCT_EXP_IDX] >= 2)): 
				DoctorFound = True
				newSchedule = [listdoctor[constants.DOCT_PRVIS_BIRTH_IDX] 
					if listdoctor[ constants.DOCT_PRVIS_BIRTH_IDX] > nextTime else nextTime,
					mothers[constants.MOTH_NAME_IDX],
					listdoctor[constants.DOCT_NAME_IDX],]

				ReachLimit = True if listdoctor[constants.DOCT_DURATION_BIRTH_IDX] >= 240 else False 

				if listdoctor[constants.DOCT_PRVIS_BIRTH_IDX] >= nextTime:
					listdoctor[constants.DOCT_PRVIS_BIRTH_IDX] += constants.BIRTH_TIME_IDX  
					# in case the doctor´s last birth ends after the new time, add to it  
				else:    # else, it will now be the next time plus 20
					listdoctor[constants.DOCT_PRVIS_BIRTH_IDX] = nextTime + constants.BIRTH_TIME_IDX
				listdoctor[constants.DOCT_REST_TIME_IDX] += constants.BIRTH_TIME_IDX
				listdoctor[constants.DOCT_DURATION_BIRTH_IDX] += constants.BIRTH_TIME_IDX
				if listdoctor[constants.DOCT_REST_TIME_IDX] >= 2400:   # In the event that there has been more than 2400 minutes since last rest (40 hours),
																		 #then set the value to -1 (weekly leave).
					listdoctor[constants.DOCT_PRVIS_BIRTH_IDX] = -1
				if listdoctor[constants.DOCT_DURATION_BIRTH_IDX] >= 240 and ReachLimit == False: 
																		# if doctor's amount of minutes is over 240 minutes (4 hours) and it wasnt's already before 
					listdoctor[constants.DOCT_PRVIS_BIRTH_IDX] += 60		#(so it only gives him a single pause in that day)
					

				doctorsCriteria(doctors)

				presentSchedule.append(newSchedule)
			j += 1

		if DoctorFound == False:       
			failedSchedule = {
		"time" : nextTime,
		"name" : mothers[constants.MOTH_NAME_IDX],
		"risk" : mothers[constants.MOTH_RISK_IDX],
		"urgency" : mothers[constants.MOTH_URGCY_IDX],
		"age" : mothers[constants.MOTH_AGE_IDX],
		"redirect message" : "redirected to other network",
		}
			failedSchedules.append(failedSchedule)
			
				
	ScheduleCriteria(presentSchedule, failedSchedules)
	return presentSchedule
	
