-- INSERT INTO client_table (client) VALUES ("Andres");
-- INSERT INTO client_table (client) VALUES ("Sebastian");
-- INSERT INTO client_table (client) VALUES ("Mama");
-- INSERT INTO client_table (client) VALUES ("Papa");


-- INSERT INTO job_table (client_id, job_id, job_name, contact) VALUES (
-- 	(SELECT id FROM client_table WHERE client = "Andres"),
-- 	"1111",
-- 	"JAPC",
-- 	"Pepe");
-- 
-- INSERT INTO PrelimPrint_table 
-- (job_id, 
-- type_of_book, 
-- number_of_copies, 
-- number_of_pages, 
-- number_of_printers, 
-- siding, 
-- paper, 
-- printer, 
-- coil, inserts, number_sheets, number_sheet_per_book, number_rims, number_cartons, coil_size, time_printing)
-- VALUES (
-- 	(SELECT id from job_table WHERE job_id="1111"),
-- 	"Prelim PPM", 
-- 	"24", 
-- 	"79", 
-- 	"2", 
-- 	"2", 
-- 	"Hammermill - Letter", 
-- 	"CANON", "None", "0.0", "948.0", "39.5", "4.74", "0.47400000000000003", "None", "Sat Dec 5 01:01:59 2020");


SELECT * from PrelimPrint_table WHERE job_id = (SELECT id from job_table where client_id = (SELECT id from client_table where client ="Andres")) 
INTERSECT
SELECT * from FinalPrint_table WHERE job_id = (SELECT id from job_table where client_id = (SELECT id from client_table where client ="Andres"))
