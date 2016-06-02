-- create schema
CREATE schema draft1
go

-- create table
CREATE table draft1.Rune
(
	RuneID int PRIMARY KEY DEFAULT 0,
	RuneName char(30) NOT NULL, 
)

exec sp_columns Rune

-- inset test data
INSERT INTO draft1.Rune(RuneID, RuneName)
	VALUES (1, 'Test Rune')

-- test query
SELECT *
FROM draft1.Rune

-- find the host name and user
-- SELECT HOST_NAME() AS HostName,
	-- SUSER_NAME() LoggedInUser

-- set default schema
-- ALTER USER WIT\carbonem1 WITH DEFAULT_SCHEMA = draft1