-- create schema
CREATE schema draft1
go

-- create table
CREATE table draft1.Champion
(
	ChampionID int PRIMARY KEY DEFAULT 0,
	ChampionName char(30) NOT NULL, 
	PrefRole1 varchar(25) NULL, 
	PrefRole2 varchar(25) NULL
)

exec sp_columns Champion

-- inset test data
INSERT INTO draft1.Champion(ChampionID, ChampionName)
	VALUES (1, 'Annie')

-- test query
SELECT *
FROM draft1.Champion

-- find the host name and user
-- SELECT HOST_NAME() AS HostName,
	-- SUSER_NAME() LoggedInUser

-- set default schema
-- ALTER USER WIT\carbonem1 WITH DEFAULT_SCHEMA = draft1