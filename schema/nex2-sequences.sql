/* Sequences */

DROP SEQUENCE IF EXISTS ALIAS_SEQ CASCADE;
CREATE SEQUENCE ALIAS_SEQ;
grant usage on ALIAS_SEQ to curator;

DROP SEQUENCE IF EXISTS ARCHIVE_SEQ CASCADE;
CREATE SEQUENCE ARCHIVE_SEQ;
grant usage on ARCHIVE_SEQ to curator;

DROP SEQUENCE IF EXISTS ANNOTATION_SEQ CASCADE;
CREATE SEQUENCE ANNOTATION_SEQ;
grant usage on ANNOTATION_SEQ to curator;

DROP SEQUENCE IF EXISTS CONDITION_SEQ CASCADE;
CREATE SEQUENCE CONDITION_SEQ;
grant usage on CONDITION_SEQ to curator;

DROP SEQUENCE IF EXISTS CURATION_SEQ CASCADE;
CREATE SEQUENCE CURATION_SEQ;
grant usage on CURATION_SEQ to curator;

DROP SEQUENCE IF EXISTS DELETELOG_SEQ CASCADE;
CREATE SEQUENCE DELETELOG_SEQ;
grant usage on DELETELOG_SEQ to curator;

DROP SEQUENCE IF EXISTS DETAIL_SEQ CASCADE;
CREATE SEQUENCE DETAIL_SEQ;
grant usage on DETAIL_SEQ to curator;

DROP SEQUENCE IF EXISTS EXPRESSION_SEQ CASCADE;
CREATE SEQUENCE EXPRESSION_SEQ;
grant usage on EXPRESSION_SEQ to curator;

DROP SEQUENCE IF EXISTS LINK_SEQ CASCADE;
CREATE SEQUENCE LINK_SEQ;
grant usage on LINK_SEQ to curator;

DROP SEQUENCE IF EXISTS NOTE_SEQ CASCADE;
CREATE SEQUENCE NOTE_SEQ;
grant usage on NOTE_SEQ to curator;

DROP SEQUENCE IF EXISTS NTR_SEQ CASCADE;
CREATE SEQUENCE NTR_SEQ;
grant usage on NTR_SEQ to curator;

DROP SEQUENCE IF EXISTS OBJECT_SEQ CASCADE;
CREATE SEQUENCE OBJECT_SEQ;
grant usage on OBJECT_SEQ to curator;

DROP SEQUENCE IF EXISTS RELATION_SEQ CASCADE;
CREATE SEQUENCE RELATION_SEQ;
grant usage on RELATION_SEQ to curator;

DROP SEQUENCE IF EXISTS SGDID_SEQ CASCADE;
CREATE SEQUENCE SGDID_SEQ START 200001;
grant usage on SGDID_SEQ to curator;

DROP SEQUENCE IF EXISTS SUMMARY_SEQ CASCADE;
CREATE SEQUENCE SUMMARY_SEQ;
grant usage on SUMMARY_SEQ to curator;

DROP SEQUENCE IF EXISTS UPDATELOG_SEQ CASCADE;
CREATE SEQUENCE UPDATELOG_SEQ;
grant usage on UPDATELOG_SEQ to curator;

DROP SEQUENCE IF EXISTS URL_SEQ CASCADE;
CREATE SEQUENCE URL_SEQ;
grant usage on URL_SEQ to curator;
