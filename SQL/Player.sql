-- create schema
CREATE schema draft1
go

-- create table
CREATE table draft1.Player
(
	PlayerID int PRIMARY KEY DEFAULT 0,
	PlayerName char(30) NULL, 
	ProfileIconId int NULL, 
	SummonerLevel int NULL
)

exec sp_columns Player

-- inset test data
INSERT INTO draft1.Player(PlayerID, PlayerName, ProfileIconId, SummonerLevel)
	VALUES (1, 'Recklessmike', 1, 30)

-- test query
SELECT *
FROM draft1.Player

-- find the host name and user
SELECT HOST_NAME() AS HostName,
	SUSER_NAME() LoggedInUser

-- set default schema
ALTER USER WIT\carbonem1 WITH DEFAULT_SCHEMA = draft1