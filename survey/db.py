import sqlite3

def load_curr_info(db_path, f_name):
    """Extract snippet data from database"""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    command = """SELECT Q1, Q2, Q3, Q4, Q5
                 FROM papers
                 WHERE name='{0}';""".format(f_name)
    cur.execute(command)

    Q1 = 'Unknown'
    Q2 = 'None'
    Q3 = 'Unknown'
    Q4 = 'None'
    Q5 = 'None'
    for row in cur.fetchall():
        Q1 = row[0]
        Q2 = row[1]
        Q3 = row[2]
        Q4 = row[3]
        Q5 = row[4]

    return [Q1, Q2, Q3, Q4, Q5]

def update_info(db_path, f_name, Q1, Q2, Q3, Q4, Q5):

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
            INSERT INTO papers(name, Q1, Q2, Q3, Q4, Q5)
            VALUES(?,?,?,?,?,?) ON CONFLICT(name)
            DO UPDATE SET
            Q1 = '{0}', Q2 = '{1}', Q3 = '{2}', Q4 = '{3}', Q5 = '{4}'""".format(Q1, Q2, Q3, Q4, Q5), (f_name, Q1, Q2, Q3, Q4, Q5))


    conn.commit()
    conn.close()
