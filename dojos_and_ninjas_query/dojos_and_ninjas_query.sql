-- INSERT INTO Dojos (name)
-- VALUES ("Yorkshire"),("Fancy Campus"),("Oregon");

-- SET SQL_SAFE_UPDATES = 0;
-- DELETE FROM Dojos;


-- SELECT * FROM Dojos;

-- INSERT INTO ninjas (first_name, last_name, age, dojo_id)
-- VALUES ("DuHaney","Ross",72,3),("Jennifer","Kate",27,3),("DuBessius","Lanes",104,3)
-- 		("Bob","Boouts",54,5),("Jen","Katherine-Jean",21,5),("Lennis","DuBopski",10,5)
-- 		("Luwis","Adante",86,6),("Ty","BostonClay",18,6),("Marcellus","Tarentino",1000,6)


-- SELECT * FROM Dojos
-- LEFT JOIN ninjas ON dojos.id = dojo_id
-- WHERE dojos.id = 4


-- SELECT * FROM Dojos
-- LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
-- 	WHERE dojod.id = (SELECT dojo_id FROM ninjas ORDER BY dojo_id DESC LIMIT 1);


SELECT * FROM Dojos
WHERE Dojos.id = (SELECT dojo_id FROM ninjas ORDER BY dojo_id DESC LIMIT 1)
