import sqlite3
from sqlite3 import Error

try:
    conn = sqlite3.connect("PX_DB_Demo")
    print("Preparing PX Database ...")
 ##   conn.execute("drop table PX_Requirements")
   ## conn.execute("drop table PX_Profiles")
    ##conn.execute("drop table PX_Panelists")
    ##conn.execute("drop table PX_InterviewScheduleDetails")
    
    conn.execute("CREATE TABLE IF NOT EXISTS PX_Requirements (reqID TEXT, description TEXT, skillset TEXT, position TEXT, status TEXT, createdby TEXT, createdon TEXT, lob TEXT, updatedby TEXT, updatedon TEXT)")
    print("Table PX_Requirements created ...")
    conn.execute("CREATE TABLE IF NOT EXISTS PX_Profiles (profID TEXT, name TEXT, skillset TEXT, exp int, emailID TEXT, contactno TEXT)");
    print("Table PX_Profiles created ...")
    conn.execute("CREATE TABLE IF NOT EXISTS PX_Panelists (panelistID  TEXT, name TEXT, emailID TEXT)");
    print("Table PX_Panelists created ...")
    conn.execute("CREATE TABLE IF NOT EXISTS PX_InterviewScheduleDetails (scheduleID TEXT, profID TEXT, panelistID TEXT, reqID TEXT, scheduledate TEXT, status TEXT)");
    print("Table PX_InterviewScheduleDetails created ...")
    conn.commit()
    
    
    ## Load data into Requirements table
    
    for i in range(0,10):
        conn.execute("INSERT INTO PX_Requirements VALUES('JB201807{0}', 'JPMC Requirement', 'Java', '601', 'Open', 'HResource1', '2018-06-18', 'CCB', '', '')".format(i))

    for i in range(0,10):
        conn.execute("INSERT INTO PX_Requirements VALUES('JB201803{0}', 'JPMC Requirement', 'Java', '602', 'InBMOApproval', 'HResource2', '2018-04-12', 'CIB', '', '')".format(i))

    for i in range(0,10):
        conn.execute("INSERT INTO PX_Requirements VALUES('JB201806{0}', 'JPMC Requirement', 'Java', '603', 'Approved', 'HResource2', '2018-03-15', 'AM', '', '')".format(i))

    for i in range(0,10):
        conn.execute("INSERT INTO PX_Requirements VALUES('JB201805{0}', 'JPMC Requirement', 'Net', '502', 'OfferAccepted', 'HResource3', '2018-01-13', 'OPT', '', '')".format(i))

    for i in range(0,10):
        conn.execute("INSERT INTO PX_Requirements VALUES('JB201804{0}', 'JPMC Requirement', 'Net', '601', 'OfferInProgress', 'HResource4', '2018-06-18', 'CCB', '', '')".format(i))

    for i in range(0,10):
        conn.execute("INSERT INTO PX_Requirements VALUES('JB201802{0}', 'JPMC Requirement', 'PEGA', '601', 'Joined', 'HResource5', '2018-03-03', 'CCB', '', '')".format(i))
     
    ## Load data into Profiles table
    for i in range(0, 10):
        conn.execute("INSERT INTO PX_Profiles VALUES('PFL201800{0}', 'Person000{0}', 'Java', 6, 'prf00{0}@mail.com', '9999988888')".format(i))
        
    for i in range(0, 10):
        conn.execute("INSERT INTO PX_Profiles VALUES('PFL201801{0}', 'Person100{0}', 'Java', 10, 'prf01{0}@mail.com', '9999987777')".format(i))
        
    for i in range(0, 10):
        conn.execute("INSERT INTO PX_Profiles VALUES('PFL201802{0}', 'Person200{0}', 'Java', 15, 'prf02{0}@mail.com', '9999986677')".format(i))
        
    for i in range(0, 10):
        conn.execute("INSERT INTO PX_Profiles VALUES('PFL201803{0}', 'Person300{0}', 'Net', 4, 'prf03{0}@mail.com', '9999988445')".format(i))
    
    for i in range(0, 10):
        conn.execute("INSERT INTO PX_Profiles VALUES('PFL201804{0}', 'Person400{0}', 'Net', 7, 'prf04{0}@mail.com', '9999988468')".format(i))
        
    for i in range(0, 10):
        conn.execute("INSERT INTO PX_Profiles VALUES('PFL201805{0}', 'Person500{0}', 'PEGA', 8, 'prf05{0}@mail.com', '9999986726')".format(i))
    
    ## Load data into Panelist table
    for i in range(0, 10):
        conn.execute("INSERT INTO PX_Panelists VALUES('PNL201800{0}', 'Panelist000{0}', 'panel00{0}@mail.com')".format(i))
        
    ## Load data into InterviewScheduleDeatils table
    for i in range(0, 10):
        conn.execute("INSERT INTO PX_InterviewScheduleDetails VALUES('SCH201800{0}', 'PFL201800{0}', 'PNL201800{0}', 'JB201807{0}', '20180628', 'OPEN')".format(i))

    conn.commit()
     
     
except Error as e:
    print(e)
finally:
    conn.close()
