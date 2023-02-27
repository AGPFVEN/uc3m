CREATE TABLE Performer(
    stage_name VARCHAR(50),
    nationality VARCHAR(50) NOT NULL,
    CONSTRAINT pk_stage_name PRIMARY KEY(stage_name)
);

CREATE TABLE Attendant(
    passport VARCHAR(12), --I made the passport varchar(12) because of an example but I think it's bad
    email VARCHAR(50) NOT NULL,
    name VARCHAR(50),
    surname1 VARCHAR(50),
    surname2 VARCHAR(50),
    date_of_bith DATE,
    phone NUMBER(15),
    portal_adress VARCHAR(100), --Is this too much?
    CONSTRAINT pk_passport PRIMARY KEY(passport)
    --We need to make a constraint for underage people
);

CREATE TABLE Attendant_Sheet( --Primary Key?
    attendant VARCHAR(12),
    --event --What to do with this ?
    date_of_birth DATE NOT NULL, --This is already in the database, can we do something about it ?
    date_purchase DATE NOT NULL,
    RFID NUMBER(25) NOT NULL, -- Assume: I assumed RFID to this
    date_event DATE NOT NULL
);

--How can we put something in a table and put a reference key of a table that doesn't exist

/*CREATE TABLE event(
    performer VARCHAR(50),
    date_ DATE,
    --tour --we need to put in the design the foreign key
);*/