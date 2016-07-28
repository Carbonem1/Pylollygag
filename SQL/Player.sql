-- create schema
CREATE schema draft1
go

-- create table
CREATE table Player
(
	PlayerID int PRIMARY KEY DEFAULT 0,
	PlayerName char(30) NULL, 
	PlayerScore char(10) NULL, 
)

exec sp_columns Player

-- inset test data
INSERT INTO draft1.Player(PlayerID, PlayerName)
	VALUES (1, 'Recklessmike')

-- test query
SELECT *
FROM draft1.Player

-- find the host name and user
SELECT HOST_NAME() AS HostName,
	SUSER_NAME() LoggedInUser
