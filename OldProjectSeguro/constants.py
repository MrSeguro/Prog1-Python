#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 169
# 62252 Gonçalo Seguro
# 62257 Ricardo Avelãs

import dateTime
import sys

# Value for weekly pause in the output schedule
WKL_PAUSE = "weekly leave"


# In a file:
# Number of header's lines
NUM_HEADER_LINES = 7
SPECIFICATION_HEADER = 6

# In a doctor's list:
# Index of the element with the doctor's name
DOCT_NAME_IDX = 0

#Index of the element with doctor's experience on the job
DOCT_EXP_IDX = 1

#Index of the element with doctor's previous birth
DOCT_PRVIS_BIRTH_IDX = 2

#Index of the element with doctor's duration of labor
DOCT_DURATION_BIRTH_IDX = 3

#Index of the element with doctor's time without his weekly rest
DOCT_REST_TIME_IDX = 4

#Birth time in minutes
BIRTH_TIME_IDX = 20


# In a mother's list:
# Index of the element with the mother's name
MOTH_NAME_IDX = 0

# Index of the element with the mother's age
MOTH_AGE_IDX = 1

# Index of the element with the mother's level of risk
MOTH_RISK_IDX = 3

# Index of the element with the mother's level of urgency
MOTH_URGCY_IDX = 2


#In a schedule's list:
SCHEDULE_TIME_IDX = 0
SCHEDULE_MOTH_IDX = 1
SCHEDULE_DOCT_IDX = 2

#Closing time of the hospital changed into minutes
CLOSE_TIME_IDX = 1200

#Doctors and schedule's header 
FILE_DOCT_HEADER = f"Organization:\nSmartH\nHour:\n{sys.argv[3][-9:-4]}\nDay:\n{dateTime.PresentDay(sys.argv[3])}\nDoctors:\n"
FILE_SCHED_HEADER = f"Organization:\nSmartH\nHour:\n{sys.argv[3][-9:-4]}\nDay:\n{dateTime.PresentDay(sys.argv[3])}\nSchedule:\n"
