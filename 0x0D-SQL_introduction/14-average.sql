-- Script that computes the score average of all records in the table second_table
ALTER TABLE second_table ADD average FLOAT;
num = SELECT AVG(score) FROM second_table;
INSERT INTO second_table (average) VALUES (num);
