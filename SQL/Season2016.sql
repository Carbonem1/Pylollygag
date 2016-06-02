-- create schema
CREATE schema draft1
go

-- create table
CREATE table draft1.Season2016
(
	MatchID varchar(25) NOT NULL, 
	Team1PlayerIDs varchar(70) NOT NULL, 
	Team1PerformenceIDs varchar(70) NOT NULL, 
	Team1RoleIDs char(10) NOT NULL, 
	Team2PlayerIDs varchar(70) NOT NULL, 
	Team2PerformenceIDs varchar(70) NOT NULL,
	Team2RoleIDs char(10) NOT NULL, 
	WinningTeam char(1) NOT NULL
)

exec sp_columns Season2016

-- inset test data
INSERT INTO draft1.Season2016(MatchID, Team1PlayerIDs, Team1PerformenceIDs, Team1RoleIDs, Team2PlayerIDs, Team2PerformenceIDs, Team2RoleIDs, WinningTeam)
	VALUES ('1', '1/2/3/4/5', '1/2/3/4/5', '2/5/4/1/3', '6/7/8/9/10', '6/7/8/9/10', '5/3/1/4/2', '1')

-- test query
SELECT *
FROM draft1.Season2016

-- find the host name and user
-- SELECT HOST_NAME() AS HostName,
	-- SUSER_NAME() LoggedInUser

-- set default schema
-- ALTER USER WIT\carbonem1 WITH DEFAULT_SCHEMA = draft1