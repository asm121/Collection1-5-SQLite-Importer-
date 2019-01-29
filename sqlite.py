'''
Austin Martin
Python program to import data into SQLite Database



'''

import sqlite3
from sqlite3 import Error
import glob





def updater(complete):
    print(str(complete) + " credentials have been analyzed")




def add_datas(db_file):

    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        print("Connection to the database worked")
        c = conn.cursor()
    except Error as e:
        print(e)

    #Adding the data into the table
    sum=0
    domainList = []
    pwList = []
    counter = 0
    # -----------------------------------------------------------------------------------------------------------------------
    # Change these when switching directories
    dir = 'Collection  #1_NEW combo semi private_EU combo.tar'
    filesInDir = glob.glob("E:\\Breaches\\Uncompressed Data\\Collection 1\\" + dir + "\\*.txt")
    # ---------------------------------------------Some Functions------------------------------------------------------------
    for x in filesInDir:

        with open(filesInDir[sum], encoding="utf8") as FileObj:
            print("Starting import of " + str(filesInDir[sum]))
            try:
                for lines in FileObj:

                    # removing the username from the domain name
                    combo = lines
                    # getting the domain name
                    if (":" not in combo):
                        domain = combo.split(';')[0]

                    else:
                        domain = combo.split(':')[0]

                    # Converting the domain to lowercase
                        # removing double at sign with single at sign
                    domain = domain.replace("@@", "@")
                    domain = domain.lower()

                    #removing www. from domain
                    if ("www." in domain):
                        domain = domain.split('www.')[1]

                    # getting the password



                    try:
                        if (":" not in combo):
                            pw = combo.split(';')[1]
                        else:
                            pw = combo.split(':')[1]

                    except:
                        if (":" not in combo):
                            if(" " not in combo):
                                pw = combo.split(';')[1]

                            elif (" " in combo):
                                pw = combo.split(' ')[1]

                            else:
                                pw = combo.split(':')[1]




                    #domainList.append(domain)
                    pw = pw[:-1]
                    #pwList.append(pw)

                    # print (domain)
                    # print(pw)

                    # Counter to update user on the status
                    counter = counter + 1
                    if ((counter % 1000000) == 0):
                        updater(counter)

                    #Actually inserting the data into the table
                    try:
                        file=filesInDir[sum].rsplit('Collection 1')[1]
                        c.execute('''INSERT INTO data(user,pass,file) VALUES(?,?,?)''',(domain,pw,file))


                    except Exception as e:
                        if(lines != ""):
                            print("Error inserting into db")
                            print(str(e))

            except Exception as e:
                print("Parsing Error... Moving On")
                print("Error on: " + str(file))
                print("Error line: " + str(lines))
                print(str(e))

        print("Done importing files of " + str(filesInDir[sum]))
        sum=sum+1


    print("Done importing all files in " + "directory")

    print("Database Files Have Been Committed")
    conn.commit()
    c.close()
    conn.close()
    print("Database Closed")

    print()

#-----------------------------------------End of Functions--------------------------------------------------------------



if __name__=='__main__':
    add_datas("E:\sqlite-tools-win32-x86-3260000\password.db")
