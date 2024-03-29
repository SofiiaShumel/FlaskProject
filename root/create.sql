CREATE TABLE Users (
	username VARCHAR(30) PRIMARY KEY,
	password VARCHAR(15) NOT NULL,
	first_name VARCHAR(30),
	second_name VARCHAR(30)
);

CREATE TABLE Messenger (
	messenger_id INTEGER PRIMARY KEY,
	messenger_name VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE User_messengers(
	user_messenger_id serial PRIMARY KEY,
	username VARCHAR(30) NOT NULL,
	messenger INTEGER NOT NULL,
	CONSTRAINT messenger_username_fk FOREIGN KEY (username)
		REFERENCES Users (username) MATCH SIMPLE 
		ON UPDATE NO ACTION ON DELETE NO ACTION,
	CONSTRAINT user_messenger_fk FOREIGN KEY (messenger)
		REFERENCES Messenger (messenger_id) MATCH SIMPLE 
		ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE Message (
	messege_id SERIAL PRIMARY KEY,
	recipient VARCHAR(30) NOT NULL,
	sender VARCHAR(30) NOT NULL,
	date_sent  TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	messenger INTEGER,
	content VARCHAR(500) NOT NULL,
	catagory VARCHAR(30),
	
	CONSTRAINT recipient_message_fk FOREIGN KEY (recipient)
		REFERENCES Users (username) MATCH SIMPLE 
		ON UPDATE NO ACTION ON DELETE NO ACTION,
	CONSTRAINT sender_message_fk FOREIGN KEY (sender)
		REFERENCES Users (username) MATCH SIMPLE 
		ON UPDATE NO ACTION ON DELETE NO ACTION,
	CONSTRAINT messenger_message_fk FOREIGN KEY (messenger)
	REFERENCES Messenger (messenger_id) MATCH SIMPLE 
		ON UPDATE NO ACTION ON DELETE NO ACTION,
		CONSTRAINT catagory_fk FOREIGN KEY (catagory)
	REFERENCES Catagory (catagory_name) MATCH SIMPLE 
		ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE Clicks(
	click_id SERIAL PRIMARY KEY,
	date_click TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	message INTEGER NOT NULL,
	CONSTRAINT click_fk FOREIGN KEY (message)
		REFERENCES Message (messege_id) MATCH SIMPLE 
		ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE Catagory(
	catagory_name VARCHAR(30) PRIMARY KEY,
	population INTEGER
);








