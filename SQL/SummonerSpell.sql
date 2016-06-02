-- create schema
CREATE schema draft1
go

-- create table
CREATE table draft1.SummonerSpell
(
	SummonerSpellID int PRIMARY KEY DEFAULT 0,
	SummonerSpellName char(30) NOT NULL, 
)

exec sp_columns SummonerSpell

-- inset test data
INSERT INTO draft1.SummonerSpell(SummonerSpellID, SummonerSpellName)
	VALUES (1, 'Test SummonerSpell')

-- test query
SELECT *
FROM draft1.SummonerSpell

-- find the host name and user
-- SELECT HOST_NAME() AS HostName,
	-- SUSER_NAME() LoggedInUser

-- set default schema
-- ALTER USER WIT\carbonem1 WITH DEFAULT_SCHEMA = draft1