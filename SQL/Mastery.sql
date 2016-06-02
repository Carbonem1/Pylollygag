-- create schema
CREATE schema draft1
go

-- create table
CREATE table draft1.Mastery
(
	MasteryID int PRIMARY KEY DEFAULT 0,
	MasteryName char(30) NOT NULL, 
)

exec sp_columns Mastery

-- inset test data
INSERT INTO draft1.Mastery(MasteryID, MasteryName)
	VALUES (1, 'Test Mastery')

-- test query
SELECT *
FROM draft1.Mastery

-- find the host name and user
-- SELECT HOST_NAME() AS HostName,
	-- SUSER_NAME() LoggedInUser

-- set default schema
-- ALTER USER WIT\carbonem1 WITH DEFAULT_SCHEMA = draft1