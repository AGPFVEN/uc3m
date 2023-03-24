CREATE TABLE Performer(
    stage_name VARCHAR(50),
    nationality VARCHAR(50) NOT NULL,
    CONSTRAINT pk_stage_name PRIMARY KEY(stage_name)
);

CREATE TABLE Manager(
    first_name VARCHAR(50) NOT NULL,
    second_name VARCHAR(50) NOT NULL,
    phone_number NUMBER(15),
    CONSTRAINT pk_phone_number PRIMARY KEY(phone_number) --Assume this bc two managers can have the same name
);

CREATE TABLE Event(
    performer VARCHAR(50), --stage_name
    date_ DATE,
    manager NUMBER(15) NOT NULL, --phone_number
    municipality VARCHAR(25) NOT NULL,
    address VARCHAR(100) NOT NULL,
    duration_ NUMBER(3) NOT NULL, --limitation assumed
    CONSTRAINT pk_performer_date PRIMARY KEY(performer, date_),
    CONSTRAINT fk_event_performer FOREIGN KEY(performer) REFERENCES Performer(stage_name),
    CONSTRAINT fk_event_manager FOREIGN KEY(manager) REFERENCES Manager(phone_number)
);

CREATE TABLE Musician(
    full_name VARCHAR(50) NOT NULL,
    passport VARCHAR(14),
    birth_date DATE NOT NULL,
    performer VARCHAR(50) NOT NULL,
    role_ VARCHAR(30),
    incorporation_date DATE,
    withdrawal_date DATE,
    CONSTRAINT pk_passport PRIMARY KEY(passport),
    CONSTRAINT fk_musician_performer FOREIGN KEY(performer) REFERENCES Performer(stage_name)
);

CREATE TABLE Tour(
    performer VARCHAR(50),
    name_ VARCHAR(50),
    CONSTRAINT pk_performer_name_ PRIMARY KEY(performer, name_),
    CONSTRAINT fk_tour_performer FOREIGN KEY(performer) REFERENCES Performer(stage_name)
);

CREATE TABLE db_tour_event(
    event_date DATE, --event date
    tour VARCHAR(50), --tour name
    CONSTRAINT pk_event_date_tour PRIMARY KEY(event_date, tour),
    CONSTRAINT fk_db_tour_event_event_date FOREIGN KEY(event_date) REFERENCES Event(date_),
    CONSTRAINT fk_db_tour_event_tour_name_ FOREIGN KEY(tour) REFERENCES Tour(name_)
);

CREATE TABLE Song(/*Assumed Primary key*/
    title VARCHAR(20),
    author1 VARCHAR(12),--Musician pk_passport
    author2 VARCHAR(12),--Musician pk_passport
    CONSTRAINT pk_title_author1 PRIMARY KEY(title, author1),
    CONSTRAINT fk_song_author FOREIGN KEY(author1) REFERENCES Musician(passport),
    CONSTRAINT fk_song_author FOREIGN KEY(author2) REFERENCES Musician(passport)
);

CREATE TABLE Publisher(
    phone_number VARCHAR(25) NOT NULL,
    name_ VARCHAR(30),
    manager NUMBER(15) NOT NULL,
    CONSTRAINT pk_name_ PRIMARY HEY(name_),
    CONSTRAINT fk_publisher_manager FOREIGN KEY(manager) REFERENCES Manager(phone_number)
);

CREATE TABLE Album(
    PAIR VARCHAR(15),
    release_date DATE NOT NULL,
    format_ VARCHAR(10) NOT NULL,
    publisher VARCHAR(30) NOT NULL,
    performer VARCHAR(50) NOT NULL,
    duration_ NUMBER(2) NOT NULL,
    CONSTRAINT pk_PAIR PRIMARY KEY(PAIR),
    CONSTRAINT valid_duration CHECK (duration_ < 90 AND duration_ > 0),
    CONSTRAINT fk_Album_publisher FOREIGN KEY(publisher) REFERENCES Publisher(name_),
    CONSTRAINT fk_Album_performer FOREIGN KEY(performer) REFERENCES Performer(stage_name)
)

CREATE TABLE Studio(
    studio_name VARCHAR(50),
    studio_address VARCHAR(100) NOT NULL,
    CONSTRAINT pk_studio_name PRIMARY KEY(studio_name)
)

CREATE TABLE Track(
    song VARCHAR(20) NOT NULL,
    album VARCHAR(15) NOT NULL,
    duration_ NUMBER(2) NOT NULL,
    number_ NUMBER(3),--Assumed pk
    title VARCHAR(30),--Assumed pk
    performer VARCHAR(50) NOT NULL,
    engineer VARCHAR(30) NOT NULL,
    studio_address VARCHAR(100),
    CONSTRAINT pk_number_title PRIMARY KEY(number_, title),
    CONSTRAINT fk_Track_song FOREIGN KEY(song) REFERENCES Song(title),
    CONSTRAINT fk_Track_album FOREIGN KEY(duration_) REFERENCES Album(PAIR),
    CONSTRAINT fk_Track_performer FOREIGN KEY(performer) REFERENCES Performer(stage_name),
    CONSTRAINT fk_Track_studio_address FOREIGN KEY(studio_address) REFERENCES Studio(studio_address)
)

CREATE TABLE Attendant(
    passport VARCHAR(14), --I made the passport varchar(14) because of an example
    email VARCHAR(50) NOT NULL,
    name_ VARCHAR(50),
    surname1 VARCHAR(50),
    surname2 VARCHAR(50),
    date_of_birth DATE,
    phone_number NUMBER(15),
    portal_adress VARCHAR(100),
    CONSTRAINT pk_passport PRIMARY KEY(passport)
);

CREATE TABLE Attendant_Sheet( --Assumed Primary Key
    attendant VARCHAR(12),
    event VARCHAR(50),
    birth_date DATE NOT NULL,
    date_purchase DATE NOT NULL,
    RFID VARCHAR(120) NOT NULL,
    date_event DATE NOT NULL,
    CONSTRAINT pk_attendant_event PRIMARY KEY(attendant, event),
    CONSTRAINT fk_Attendant_Sheet_attendant FOREIGN KEY(attendant) REFERENCES Attendant(passport),
    CONSTRAINT fk_Attendant_Sheet_event FOREIGN KEY(event) REFERENCES Event(performer),
    CONSTRAINT fk_Attendant_Sheet_birth_date FOREIGN KEY(birth_date) REFERENCES Attendant(date_of_birth),
    CONSTRAINT fk_Attendant_Sheet_date_event FOREIGN KEY(date_event) REFERENCES Event(date_)
);