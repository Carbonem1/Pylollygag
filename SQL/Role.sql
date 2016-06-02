-- create schema
CREATE schema draft1
go

-- create table
CREATE table draft1.Role
(
	RoleID int PRIMARY KEY DEFAULT 0,
	RoleName char(10) NOT NULL, 
)

exec sp_columns Role

-- inset test data
INSERT INTO draft1.Role(RoleID, RoleName)
	VALUES (1, 'Top')

-- test query
SELECT *
FROM draft1.Role

-- find the host name and user
-- SELECT HOST_NAME() AS HostName,
	-- SUSER_NAME() LoggedInUser

-- set default schema
-- ALTER USER WIT\carbonem1 WITH DEFAULT_SCHEMA = draft1