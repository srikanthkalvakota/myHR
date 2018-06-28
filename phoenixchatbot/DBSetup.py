import sqlite3
from sqlite3 import Error

try:
    conn = sqlite3.connect("PX_DB1")
    print("Preparing PX Database ...")
##    conn.execute("drop table PX_Requirements")
##    conn.execute("drop table PX_Profiles")
##    conn.execute("drop table PX_Panelists")
##    conn.execute("drop table PX_InterviewScheduleDetails")
##    
    conn.execute("CREATE TABLE IF NOT EXISTS PX_Requirements (reqID TEXT, description TEXT, skillset TEXT, status TEXT, createdby TEXT, createdon TEXT, lob TEXT, updatedby TEXT, updatedon TEXT)")
    print("Table PX_Requirements created ...")
    conn.execute("CREATE TABLE IF NOT EXISTS PX_Profiles (profID TEXT, name TEXT, skillset TEXT, emailID TEXT, contactno TEXT)");
    print("Table PX_Profiles created ...")
    conn.execute("CREATE TABLE IF NOT EXISTS PX_Panelists (panelistID  TEXT, name TEXT, emailID TEXT)");
    print("Table PX_Panelists created ...")
    conn.execute("CREATE TABLE IF NOT EXISTS PX_InterviewScheduleDetails (scheduleID TEXT, profID TEXT, panelistID TEXT, reqID TEXT, scheduledate TEXT, status TEXT)");
    print("Table PX_InterviewScheduleDetails created ...")
    conn.commit()
except Error as e:
    print(e)
finally:
    conn.close()

