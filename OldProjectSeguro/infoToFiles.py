#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 169
# 62252 Gonçalo Seguro 
# 62257 Ricardo Avelãs

import constants
import dateTime


def writeScheduleFile(sched, header, fileName):
    """
    Writes a collection of scheduled birth assistances into a file.

    Requires:
    sched is a list with the structure as in the output of
    planning.updateSchedule representing the cruises assigned;
    header is a string with a header, as in the examples provided in 
    the general specification (omitted here for the sake of readability);
    fileName is a str with the name of a .txt file.
    Ensures:
    writing of file named fileName representing the birth assistances in schedule,
    one per line, as organized in the examples provided
    in the general specification (omitted here for the sake of readability); 
    the lines in this file keeps the ordering top to bottom of 
    the assistances as ordered head to tail in sched.
    """
    finalString = header
    data = ""

    for k in sched:
        k[constants.SCHEDULE_TIME_IDX] = dateTime.TimeToStr(k[constants.SCHEDULE_TIME_IDX]) 
        data += f"{k[constants.SCHEDULE_TIME_IDX]}, {k[constants.SCHEDULE_MOTH_IDX]}, {k[constants.SCHEDULE_DOCT_IDX]}\n"
    
    finalString = finalString + data

    with open (fileName, "w", encoding="utf-8") as f:
        f.write(finalString)
        

def writeDoctorsFile(doctors, header, fileName):
    """
    Writes the collection of doctors already upadted into a file
    Requires:
    doctors is a list with the structure as in the output of
    planning.updateSchedule representing the doctors assigned;
    header is a string with a header, as in the examples provided in 
    the general specification (omitted here for the sake of readability);
    fileName is a str with the name of a .txt file.

    """
    finalString = header
    data = ""

    for k in doctors:
        data = f"{k[constants.DOCT_NAME_IDX]}, {k[constants.DOCT_EXP_IDX]}, \
{dateTime.TimeToStr(k[constants.DOCT_PRVIS_BIRTH_IDX]) if k[constants.DOCT_PRVIS_BIRTH_IDX] != -1 else constants.WKL_PAUSE}, \
{k[constants.DOCT_DURATION_BIRTH_IDX]}, {dateTime.TimeToStr(k[constants.DOCT_REST_TIME_IDX])}\n" 
        finalString += data
   
    with open (fileName, "w", encoding="utf-8") as f:
        f.write(finalString)


def timeUpdated(timeFile):
    """
    Gives the time already updated in all the previous files 
    Requires: 
    timeFile is a str with the name of a .txt file. and the 
    Ensures:
    timeFile will be updated
    """
    timeFile = dateTime.addHalfHour(open(timeFile, encoding="utf-8"))
