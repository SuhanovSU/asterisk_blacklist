CREATE DATABASE IF NOT EXISTS asterisk;
USE asterisk;
CREATE TABLE blacklist ( id smallint unsigned not null auto_increment, name varchar(20) not null, constraint pk_example primary key (id) );
INSERT INTO blacklist ( id, name ) VALUES ( null, 'Sample data' );
