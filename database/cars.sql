CREATE TABLE cars(
                        car_id serial PRIMARY KEY,
                        model VARCHAR (255) UNIQUE NOT NULL,
                        year INT NOT NULL,
                        details TEXT NOT NULL
);

INSERT INTO cars (model, year, details) values ('Toyota', 2009, 'details');
INSERT INTO cars (model, year, details) values ('BMW', 1997, 'details');
INSERT INTO cars (model, year, details) values ('Skoda', 2017, 'details');
INSERT INTO cars (model, year, details) values ('Subaru', 1999, 'details');
INSERT INTO cars (model, year, details) values ('Mercedes', 2010, 'details');