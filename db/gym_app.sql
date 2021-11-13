DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS activities;
DROP TABLE IF EXISTS instructors;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    premium BOOLEAN,
    active BOOLEAN
);

CREATE TABLE instructors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    bio TEXT
);

CREATE TABLE activities ( 
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255), 
    instructor_id INT REFERENCES instructors(id),
    room VARCHAR(255),
    capacity INT,
    date DATE, 
    time TIME, 
    active BOOLEAN
); 

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY, 
    member_id INT REFERENCES members(id),
    activity_id INT REFERENCES activities(id)
);

-- INSERT INTO instructors (name, bio) VALUES ('Hanna', 'I like the gym');

-- INSERT INTO activities(name, instructor_id, room, capacity, date, time, active)
-- VALUES ('Yoga', 1, 'studio 03', 20, '2021-11-25', '11:00', True);

