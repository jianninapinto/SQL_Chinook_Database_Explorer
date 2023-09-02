# Create a new table in the database called "Stores"
# | city          | state | employees | website | curbside |
# |---------------|-------|-----------|---------|----------|
# | New York      | NY    | 8         | 1       | 1        |
# | Los Angeles   | CA    | 11        | 0       | 1        |
# | Seattle       | WA    | 7         | 1       | 0        |
# | San Francisco | CA    | 5         | 0       | 0        |

# Drop the table so that we can run
# connect.py without side effects from previous
# times that we executed the script.
DROP_STORES = '''
DROP TABLE IF EXISTS Stores;
'''

MAKE_STORES = '''
CREATE TABLE IF NOT EXISTS Stores
(city char(200),
state char(2),
employees int,
website int,
curbside int);
'''

# Verify that the table was created correctly
CHECK_STORES = '''
SELECT * FROM Stores;
'''

# How many rows are in the table?
NUM_ROWS = '''
SELECT COUNT(*) FROM Stores;
'''

# How many Stores have a website and curbside pickup?
WEBSITE_AND_CURBSIDE = '''
SELECT COUNT(*) FROM Stores
WHERE website > 0 AND curbside > 0
'''
# Another way of writing this query:
WEBSITE_AND_CURBSIDE = '''
SELECT COUNT(*) FROM Stores
WHERE website AND curbside
'''

# How many stores have more than 10 employees and curbside pickup?
TEN_AND_CURBSIDE = '''
SELECT COUNT(*) FROM Stores
WHERE employees > 10 AND curbside;
'''

# How many states have stores?
NUM_STATES = '''
SELECT COUNT(DISTINCT state) FROM Stores;
'''

# How many tracks?
NUM_TRACKS = '''
SELECT COUNT(*) FROM tracks;
'''

# How many Genres?
NUM_GENRES = '''
SELECT COUNT(*) FROM genres;
'''

# What is the shortest track?
SHORTEST_TRACK = '''
SELECT Name, Milliseconds FROM tracks
ORDER BY Milliseconds
LIMIT 1;
'''

# What is the longest track?
LONGEST_TRACK = '''
SELECT Name, Milliseconds FROM tracks
ORDER BY Milliseconds DESC
LIMIT 1;
'''

# How many tracks are longer than 5 minutes?
LONG_TRACKS = '''
SELECT COUNT(*) FROM tracks
WHERE Milliseconds > 300000;
'''

# Who is the composer with the most tracks?
# IF *NULL* is an acceptable answer
PROLIFIC_COMPOSER_NULL = '''
SELECT  Composer, COUNT(*) as num_tracks FROM TRACKS
GROUP BY Composer
ORDER BY num_tracks DESC
LIMIT 1;
'''

# Who is the composer with the most tracks?
# IF *NULL* is not an acceptable answer
# WHERE can be used BEFORE a GROUP BY, but not after
# after a GROUP BY we use HAVING
PROLIFIC_COMPOSER = '''
SELECT Composer, COUNT(*) as num_tracks FROM TRACKS
WHERE Composer IS NOT NULL
GROUP BY Composer
ORDER BY num_tracks DESC
LIMIT 1;
'''

# How many composers have more than 10 tracks?
MORE_THAN_TEN = '''
SELECT COUNT(*) FROM
(SELECT COMPOSER, COUNT(*) as num_tracks FROM TRACKS
WHERE Composer IS NOT NULL
GROUP BY Composer
HAVING num_tracks > 10);
'''
