#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 169
# 62252 Gonçalo Seguro
# 62257 Ricardo Avelãs

import dateTime
import constants
import sys


def removeHeader(FileName):
    """
    Skip the header lines from a file.

    Requires: a str with the name of a ".txt" file.
    Ensures: a file read after the 7 first lines.
    
    """
    inFile = FileName 
    for line in range (constants.NUM_HEADER_LINES):
        inFile.readline()
    return inFile


def readDoctorsFile(DoctorsFile):
    """
    Reads a file with a list of doctors into a collection.

    Requires:
    inFile is str with the name of a .txt file containing
    a list of doctors organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list of lists where each list corresponds to a doctor listed in
    the file fileName (with all the info pieces belonging to that doctor),
    following the order provided in the lines of the file.
   
    """
    DoctorsFile = removeHeader(open(sys.argv[1], "r", encoding="utf-8"))

    DoctorsList = []
    for line in DoctorsFile:
        if line.strip():
            InfoDoctors = line.rstrip().split(", ")
            InfoDoctors[2]= dateTime.hourToInt(InfoDoctors[2])*60 + \
        dateTime.minutesToInt(InfoDoctors[2])
            InfoDoctors[4]= dateTime.hourToInt(InfoDoctors[4])*60 + \
        dateTime.minutesToInt(InfoDoctors[4])                          
            InfoDoctors[3]= int(InfoDoctors[3])
            DoctorsList.append(InfoDoctors)
    
    return DoctorsList


def readRequestsFile(RequestsFile):
    """
    Reads a file with the requests made by the mothers into a collection
    Requires:
    inFile is str with the name of a .txt file containing
    a list of requests organized with the standards previously established (omitted here for the sake of readability)
    Ensures:
    A list of lists where each mother is assigned to a doctor depending on her conditions and listed in requestList
    
    """
    RequestsFile = removeHeader(open(sys.argv[3], "r", encoding="utf-8"))       

    requestsList = [] 
    for line in RequestsFile:
        requestData = line.rstrip().split(", ")
        requestsList.append(requestData)        

    return requestsList

def readScheduleFile (ScheduleFile):
    """
    Reads a file with the schedules into a collection
    Requires: 
    inFile is str with the name of a .txt file containing
    a list of schedules organized as in the examples provided in
    the general specification;
    Ensures:
    A list of lists where each schedule marks the time the file fileName (with all the info pieces belonging to that doctor),
    following the order provided in the lines of the file;
    
    """
    ScheduleFile = removeHeader(open(ScheduleFile, "r", encoding="utf-8"))
    
    schedulesList = []
    for line in ScheduleFile:
        schedulesData = line.rstrip().split(", ")
        schedulesData[0]= dateTime.hourToInt(schedulesData[0])*60 + \
        dateTime.minutesToInt(schedulesData[0])
        schedulesList.append(schedulesData)
        
    return schedulesList

def headerCompare(doctorsFileName, requestsFileName, scheduleFileName): 
    """ 
    Compares the str in header that shows what File is and in case that don't it is not equal, launchs an exception 
    Requires: a File with the str in index 6 
    Ensures: compares the 2 srt and if it is different launches the exception 
    
    """ 
    
    docsList = open(doctorsFileName, "r", encoding = "utf-8") 
    requestsList = open(requestsFileName, "r", encoding = "utf-8") 
    schedList = open(scheduleFileName, "r", encoding = "utf-8") 
    
    if docsList.readlines()[constants.SPECIFICATION_HEADER][:-1] != "Doctors:": 
        errormessage = "File head error: scope inconsistency between name and header infile" + doctorsFileName +"." 
        raise IOError(errormessage) 
    if requestsList.readlines()[constants.SPECIFICATION_HEADER][:-1] != "Mothers:": 
        errormessage = "File head error: scope inconsistency between name and header infile" + requestsFileName +"." 
        raise IOError(errormessage) 
    if schedList.readlines()[constants.SPECIFICATION_HEADER][:-1] != "Schedule:": 
        errormessage = "File head error: scope inconsistency between name and header infile" + scheduleFileName +"." 
        raise IOError(errormessage)

    docsList.close() 
    requestsList.close() 
    schedList.close()

    
