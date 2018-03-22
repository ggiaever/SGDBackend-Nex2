-- Generated by Ora2Pg, the Oracle database Schema converter, version 17.4
-- Copyright 2000-2016 Gilles DAROLD. All rights reserved.
-- DATASOURCE: dbi:Oracle:host=sgd-nex2-db.stanford.edu;sid=SGD

SET client_encoding TO 'UTF8';

\set ON_ERROR_STOP ON

-- Audit & Basic tables

DROP TABLE IF EXISTS nex.deletelog CASCADE;
CREATE TABLE nex.deletelog (
	deletelog_id bigint NOT NULL DEFAULT nextval('deletelog_seq'),
	bud_id integer,
	tab_name varchar(60) NOT NULL,
	primary_key bigint NOT NULL,
	date_created timestamp NOT NULL DEFAULT LOCALTIMESTAMP,
	created_by varchar(12) NOT NULL,
	deleted_row text NOT NULL,
	CONSTRAINT deletelog_pk PRIMARY KEY (deletelog_id)
) ;
COMMENT ON TABLE nex.deletelog IS 'Contains a copy of every deleted row, populated by triggers.';
COMMENT ON COLUMN nex.deletelog.date_created IS 'Date the record was entered into the database.';
COMMENT ON COLUMN nex.deletelog.primary_key IS 'Primary key of the row deleted.';
COMMENT ON COLUMN nex.deletelog.tab_name IS 'Table name.';
COMMENT ON COLUMN nex.deletelog.deletelog_id IS 'Unique identifier (serial number).';
COMMENT ON COLUMN nex.deletelog.created_by IS 'Username of the person who entered the record into the database.';
COMMENT ON COLUMN nex.deletelog.deleted_row IS 'Concatenation of all columns in the row deleted.';
COMMENT ON COLUMN nex.deletelog.bud_id IS 'PK from BUD.DELETE_LOG.DELETE_LOG_NO.';

DROP TABLE IF EXISTS nex.updatelog CASCADE; 
CREATE TABLE nex.updatelog (
	updatelog_id bigint NOT NULL DEFAULT nextval('updatelog_seq'),
	bud_id integer,
	tab_name varchar(60) NOT NULL,
	col_name varchar(60) NOT NULL,
	primary_key bigint NOT NULL,
	date_created timestamp NOT NULL DEFAULT LOCALTIMESTAMP,
	created_by varchar(12) NOT NULL,
	old_value text,
	new_value text,
	CONSTRAINT updatelog_pk PRIMARY KEY (updatelog_id)
) ;
COMMENT ON TABLE nex.updatelog IS 'Contains a copy of every updated column, populated by triggers.';
COMMENT ON COLUMN nex.updatelog.date_created IS 'Date the record was entered into the database.';
COMMENT ON COLUMN nex.updatelog.tab_name IS 'Name of the table updated.';
COMMENT ON COLUMN nex.updatelog.updatelog_id IS 'Unique identifier (serial number).';
COMMENT ON COLUMN nex.updatelog.new_value IS 'Column new value.';
COMMENT ON COLUMN nex.updatelog.created_by IS 'Username of the person who entered the record into the database.';
COMMENT ON COLUMN nex.updatelog.primary_key IS 'Primary key of the row that was updated.';
COMMENT ON COLUMN nex.updatelog.col_name IS 'Name of the column updated.';
COMMENT ON COLUMN nex.updatelog.old_value IS 'Column old value.';
COMMENT ON COLUMN nex.updatelog.bud_id IS 'PK from BUD.UPDATE_LOG.UPDATE_LOG_NO.';

DROP TABLE IF EXISTS nex.dbuser CASCADE; 
CREATE TABLE nex.dbuser (
	dbuser_id bigint NOT NULL DEFAULT nextval('object_seq'),
	username varchar(12) NOT NULL,
	first_name varchar(40) NOT NULL,
	last_name varchar(40) NOT NULL,
	status varchar(40) NOT NULL,
	is_curator boolean NOT NULL,
	email varchar(100) NOT NULL,
	date_created timestamp NOT NULL DEFAULT LOCALTIMESTAMP,
	CONSTRAINT dbuser_pk PRIMARY KEY (dbuser_id)
) ;
COMMENT ON TABLE nex.dbuser IS 'Current or former users with logins to the SGD database.';
COMMENT ON COLUMN nex.dbuser.status IS 'Current state of the database user (Current, Former).';
COMMENT ON COLUMN nex.dbuser.dbuser_id IS 'Unique identifier (serial number).';
COMMENT ON COLUMN nex.dbuser.date_created IS 'Date the record was entered into the database.';
COMMENT ON COLUMN nex.dbuser.last_name IS 'Last name of the database user.';
COMMENT ON COLUMN nex.dbuser.first_name IS 'First name of the database user.';
COMMENT ON COLUMN nex.dbuser.username IS 'Database login name.';
COMMENT ON COLUMN nex.dbuser.email IS 'Stanford (SUNetID) email address of the database user.';
COMMENT ON COLUMN nex.dbuser.is_curator IS 'Whether the user is a curator.';
ALTER TABLE nex.dbuser ADD CONSTRAINT dbuser_uk UNIQUE (username);
ALTER TABLE nex.dbuser ADD CONSTRAINT dbuser_status_ck CHECK (STATUS IN ('Current','Former'));

DROP TABLE IF EXISTS nex.source CASCADE; 
CREATE TABLE nex.source (
	source_id bigint NOT NULL DEFAULT nextval('object_seq'),
	format_name varchar(100) NOT NULL,
	display_name varchar(500) NOT NULL,
	bud_id integer,
	description varchar(500),
	date_created timestamp NOT NULL DEFAULT LOCALTIMESTAMP,
	created_by varchar(12) NOT NULL,
	CONSTRAINT source_pk PRIMARY KEY (source_id)
) ;
COMMENT ON TABLE nex.source IS 'Origin or source of the data.';
COMMENT ON COLUMN nex.source.created_by IS 'Username of the person who entered the record into the database.';
COMMENT ON COLUMN nex.source.source_id IS 'Unique identifier (serial number).';
COMMENT ON COLUMN nex.source.description IS 'Description or comment.';
COMMENT ON COLUMN nex.source.date_created IS 'Date the record was entered into the database.';
COMMENT ON COLUMN nex.source.display_name IS 'Public display name.';
COMMENT ON COLUMN nex.source.bud_id IS 'PK from BUD.CODE.CODE_NO.';
COMMENT ON COLUMN nex.source.format_name IS 'Unique name to create download files.';
ALTER TABLE nex.source ADD CONSTRAINT source_uk UNIQUE (format_name);

DROP TABLE IF EXISTS nex.sgdid CASCADE; 
CREATE TABLE nex.sgdid (
	sgdid_id bigint NOT NULL DEFAULT nextval('object_seq'),
	format_name varchar(100) NOT NULL,
	display_name varchar(500) NOT NULL,
	obj_url varchar(500) NOT NULL,
	source_id bigint NOT NULL,
	bud_id integer,
	subclass varchar(40) NOT NULL,
	sgdid_status varchar(40) NOT NULL,
	description varchar(1000),
	date_created timestamp NOT NULL DEFAULT LOCALTIMESTAMP,
	created_by varchar(12) NOT NULL,
	CONSTRAINT sgdid_pk PRIMARY KEY (sgdid_id)
) ;
COMMENT ON TABLE nex.sgdid IS 'SGD accession identifier for dbentity objects consisting of a letter (S or L) followed by 9 zero-padded numbers (e.g., S000151155).';
COMMENT ON COLUMN nex.sgdid.obj_url IS 'URL of the object (relative for local links or complete for external links).';
COMMENT ON COLUMN nex.sgdid.display_name IS 'Public display name.';
COMMENT ON COLUMN nex.sgdid.bud_id IS 'PK from BUD.DBXREF.DBXREF_NO.';
COMMENT ON COLUMN nex.sgdid.sgdid_id IS 'Unique identifier (serial number).';
COMMENT ON COLUMN nex.sgdid.subclass IS 'Type of dbentity assigned the SGDID (LOCUS, REFERENCE, STRAIN, FILE, PATHWAY, COMPLEX).';
COMMENT ON COLUMN nex.sgdid.date_created IS 'Date the record was entered into the database.';
COMMENT ON COLUMN nex.sgdid.sgdid_status IS 'State of the SGDID (Primary, Secondary, Deleted, Unassigned).';
COMMENT ON COLUMN nex.sgdid.source_id IS 'FK to SOURCE.SOURCE_ID.';
COMMENT ON COLUMN nex.sgdid.created_by IS 'Username of the person who entered the record into the database.';
COMMENT ON COLUMN nex.sgdid.description IS 'Comment about or reason why the SGDID was deleted.';
ALTER TABLE nex.sgdid ADD CONSTRAINT sgdid_uk UNIQUE (format_name);
ALTER TABLE nex.sgdid ADD CONSTRAINT sgdid_subclass_ck CHECK (SUBCLASS IN ('LOCUS','FILE','STRAIN','REFERENCE','PATHWAY','COMPLEX'));
ALTER TABLE nex.sgdid ADD CONSTRAINT sgdid_status_ck CHECK (SGDID_STATUS IN ('Primary','Secondary','Deleted','Unassigned'));
CREATE INDEX sgdid_source_fk_index ON nex.sgdid (source_id);
