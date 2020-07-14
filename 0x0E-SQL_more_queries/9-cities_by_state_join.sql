-- script that lists all cities contained in the database hbtn_0d_usa
SELECT
	cities.id
AS
	id, cities.name, states.name
AS
	name
FROM
	states, cities
WHERE
	cities.state_id = states.id
ORDER BY
	cities.id
ASC;
