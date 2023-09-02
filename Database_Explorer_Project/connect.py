import sqlite3
import queries as q

conn = sqlite3.connect('chinook.db')

curs = conn.cursor()

if __name__ == '__main__':
    # db_conn = connect_to_db()

    data = [
        ('New York', 'NY', 8, 1, 1),
        ('Los Angeles', 'CA', 11, 0, 1),
        ('Seattle', 'WA', 7, 1, 0),
        ('San Francisco', 'CA', 5, 0, 0)
    ]

    # results = execute_query(db_conn, q.select_all)
    # print(results[:5])

if __name__ == '__main__':
    print('Drop "Stores" if exists \n')
    curs.execute(q.DROP_STORES)

    print('Creating the "Stores" table \n')
    curs.execute(q.MAKE_STORES)

    print('Adding rows to the "Stores" table')
    for row in data:
        curs.execute(
            f'INSERT INTO Stores (city, state, employees, website, curbside) VALUES {row};')
    conn.commit()

    print('\nVerify that the "Stores" table was created correctly \n')
    print(curs.execute(q.CHECK_STORES).fetchall())

    print("\nHow many rows are in the table? \n")
    print(curs.execute(q.NUM_ROWS).fetchall())

    print("\nHow many stores have a website and curbside pickup? \n")
    print(curs.execute(q.WEBSITE_AND_CURBSIDE).fetchall())

    print("\nHow many stores have more than 10 employees and curbside pickup? \n")
    print(curs.execute(q.TEN_AND_CURBSIDE).fetchall())

    print("\nHow many states have stores? \n")
    print(curs.execute(q.NUM_STATES).fetchall())

    print("\nHow many tracks? \n")
    print(curs.execute(q.NUM_TRACKS).fetchall())

    print("\nHow many Genres? \n")
    print(curs.execute(q.NUM_GENRES).fetchall())

    print("\nWhat is the shortest track? \n")
    print(curs.execute(q.SHORTEST_TRACK).fetchall())

    print("\nWhat is the longest track? \n")
    print(curs.execute(q.LONGEST_TRACK).fetchall())

    print("\nHow many tracks are longer than 5 minutes? \n")
    print(curs.execute(q.LONG_TRACKS).fetchall())

    print("\nWho is the composer with the most tracks? \n")
    print(curs.execute(q.PROLIFIC_COMPOSER).fetchall())

    print("\nHow many composers have more than 10 tracks? \n")
    print(curs.execute(q.MORE_THAN_TEN).fetchall())
