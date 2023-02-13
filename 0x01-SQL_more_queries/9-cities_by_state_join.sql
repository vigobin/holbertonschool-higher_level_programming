-- Lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name, state.id
FROM cities
JOIN states ON cities.state_id = state_id
ORDER BY cities.id ASC;
