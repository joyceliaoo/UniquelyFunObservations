import sqlite3

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

replace()


# DELETE FROM ufo WHERE country IS NULL OR TRIM(country) = ''
