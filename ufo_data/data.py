import sqlite3
import csv

DB_FILE = "ufo.db"

def create_table():
    db = sqlite3.connect(DB_FILE)

    #used to traverse db
    c = db.cursor() #facilitate db ops
    c.execute("CREATE TABLE ufo (id date_time TEXT, city TEXT, state_province TEXT, country TEXT, UFO_shape TEXT, len_encounter_secs TEXT, latitude TEXT, longitude TEXT)")
    db.commit() #save changes
    db.close()


def replace():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT * FROM ufo WHERE country IS NULL OR country = '';"
    c.execute(command)
    data = c.fetchall()

    for i in data:
        print(i)
        if "canada" in i[1]:
            country = "ca"
            date_time = i[0]
            latitude = i[-2]
            longitude = i[-1]
            c.execute("UPDATE ufo SET country=? WHERE id=?",(country, date_time))
            print(i)

        if "uk" in i[1]:
            country = "gb"
            date_time = i[0]
            latitude = i[-2]
            longitude = i[-1]
            c.execute("UPDATE ufo SET country=? WHERE id=?",(country, date_time))
            print (i)

    db.commit()
    db.close()

# replace()


# DELETE FROM ufo WHERE country IS NULL OR TRIM(country) = ''


# with open('ufo_sqlite_working.csv','r') as csvinput:
#     with open('ufo_dates.csv', 'w') as csvoutput:
#         writer = csv.writer(csvoutput, lineterminator='\n')
#         reader = csv.reader(csvinput)
#
#         all = []
#         row = next(reader)
#         row.append("mm/dd")
#         row.append("time of day")
#         row.append("month")
#         all.append(row)
#
#         for row in reader:
#             date_time = row[0].split(" ")
#             date = date_time[0].split("/")
#             new_date = date[0] + "/" + date[1]
#             # print(new_date)
#             row.append(new_date)
#             row.append(date_time[1])
#             row.append(date[0])
#             all.append(row)
#
#         writer.writerows(all)

# with open('ufo_dates.csv','r') as csvinput:
#     with open('ufo_dates_clean.csv', 'w') as csvoutput:
#         writer = csv.writer(csvoutput, lineterminator='\n')
#         reader = csv.reader(csvinput)
#
#         all = []
#         row = next(reader)
#         row.append("new mm/dd")
#         all.append(row)
#
#         for row in reader:
#             date = row[8].split("/")
#             if int(date[1]) < 10:
#                 date[1] = "0" + date[1]
#             new_date = date[0] + "/" + date[1]
#             print(new_date)
#             row.append(new_date)
#             all.append(row)
#
#         writer.writerows(all)

with open('ufo_dates.csv','r') as csvinput:
    with open('ufo_year.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        row.append("date")
        all.append(row)

        for row in reader:
            old_date = row[0].split(" ")[0].split("/")
            if int(old_date[0]) < 10:
                old_date[0] = "0" + old_date[0]
            if int(old_date[1]) < 10:
                old_date[1] = "0" + old_date[1]
            date = "/".join(old_date)
            print(date)
            row.append(date)
            all.append(row)

        writer.writerows(all)
