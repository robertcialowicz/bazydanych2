USE [Northwind]
GO
ALTER TABLE [Order Details] DROP CONSTRAINT IF EXISTS pk_order_details
ALTER TABLE [Order Details] DROP CONSTRAINT IF EXISTS uk_order_details
ALTER TABLE [Order Details] DROP COLUMN IF EXISTS orderdetailid
ALTER TABLE [Order Details] ADD orderdetailid INTEGER IDENTITY(1,1) NOT NULL
GO
ALTER TABLE [Order Details] ADD CONSTRAINT pk_order_details PRIMARY KEY (orderdetailid)
ALTER TABLE [Order Details] ADD CONSTRAINT uk_order_details UNIQUE (orderid, productid)