CREATE TABLE [Switches] ( 
	[IventoryID] NVARCHAR(50)  NOT NULL PRIMARY KEY, 
	[TypeOfSwitch] NVARCHAR(50)  NOT NULL,
	[NumberOfPorts] INTEGER NOT NULL,
	[Notes] NVARCHAR(1000),
	[DateRecieved] NVARCHAR(50) NOT NULL,
	[DateSentOut] NVARCHAR(50),
	[Property] INTEGER
); 
CREATE TABLE [Cameras] (  
	[IventoryID] NVARCHAR(50)  NOT NULL PRIMARY KEY, 
	[TypeOfCamera] NVARCHAR(50)  NOT NULL,
	[Notes] NVARCHAR(1000),
	[DateRecieved] NVARCHAR(50) NOT NULL,
	[DateSentOut] NVARCHAR(50),
	[Property] INTEGER  
);     
CREATE TABLE [Routers] (  
	[IventoryID] NVARCHAR(50)  NOT NULL PRIMARY KEY, 
	[ModelNumber] NVARCHAR(50)  NOT NULL,
	[Notes] NVARCHAR(1000),
	[DateRecieved] NVARCHAR(50) NOT NULL,
	[DateSentOut] NVARCHAR(50),
	[Property] INTEGER  
); 
CREATE TABLE [DVRs] (  
	[IventoryID] NVARCHAR(50)  NOT NULL PRIMARY KEY, 
	[Notes] NVARCHAR(1000),
	[DateRecieved] NVARCHAR(50) NOT NULL,
	[DateSentOut] NVARCHAR(50),
	[Property] INTEGER 
);
CREATE TABLE [Phones] ( 
	[IventoryID] NVARCHAR(50)  NOT NULL PRIMARY KEY, 
	[ModelNumber] NVARCHAR(50)  NOT NULL,
	[IMEI] INTEGER NOT NULL,
	[Notes] NVARCHAR(1000),
	[DateRecieved] NVARCHAR(50) NOT NULL,
	[DateSentOut] NVARCHAR(50),
	[PhoneNumber] INTEGER,
	[Assigned User] NVARCHAR(50)
);
CREATE TABLE [Insomniacs] (
	[IventoryID] NVARCHAR(50)  NOT NULL PRIMARY KEY, 
	[Property] INTEGER  NOT NULL,
	[Notes] NVARCHAR(1000),
	[DateRecieved] NVARCHAR(50) NOT NULL,
	[DateSentOut] NVARCHAR(50)
	
);
