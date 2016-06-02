-- create schema
CREATE schema draft1
go

-- create table
CREATE table draft1.Item
(
	ItemID int PRIMARY KEY DEFAULT 0,
	ItemName char(30) NOT NULL, 
)

exec sp_columns Item

-- inset test data
INSERT INTO draft1.Item(ItemID, ItemName)
	VALUES (1, 'Healing Potion')

-- test query
SELECT *
FROM draft1.Item

-- find the host name and user
-- SELECT HOST_NAME() AS HostName,
	-- SUSER_NAME() LoggedInUser

-- set default schema
-- ALTER USER WIT\carbonem1 WITH DEFAULT_SCHEMA = draft1