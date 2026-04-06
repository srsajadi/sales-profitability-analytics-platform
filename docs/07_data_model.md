# Data Model

## Overview
The model follows a star schema design with one central fact table and multiple dimension tables.

## Fact Table

### FactSales
Grain: One row per sales transaction line

Columns:
- OrderID
- OrderDate
- ProductID
- CustomerID
- RegionID
- ChannelID
- Quantity
- UnitPrice
- UnitCost
- DiscountAmount
- NetRevenue
- TotalCost
- Profit

## Dimension Tables

### DimDate
- Date
- Year
- Month
- Quarter
- FiscalYear
## Date Dimension Design

The model uses a dedicated `DimDate` table with:
- a true date column for time intelligence
- an integer `DateKey` in `YYYYMMDD` format for relationships

The relationship between `DimDate` and `FactSales` is defined on `DateKey`, while `DimDate[Date]` is used to mark the table as the model’s official date table. This supports both warehouse-style modelling and Power BI time intelligence.
### DimProduct
- ProductID
- ProductName
- Category
- Subcategory
- Brand

### DimCustomer
- CustomerID
- CustomerName
- Segment
- Country

### DimRegion
- RegionID
- RegionName
- Country

### DimChannel
- ChannelID
- ChannelName

## Relationships

- DimDate[Date] → FactSales[OrderDate]
- DimProduct[ProductID] → FactSales[ProductID]
- DimCustomer[CustomerID] → FactSales[CustomerID]
- DimRegion[RegionID] → FactSales[RegionID]
- DimChannel[ChannelID] → FactSales[ChannelID]

All relationships are one-to-many and single-direction, enforcing a clean star schema.
## Design Principles
- No snowflake schema
- No bidirectional relationships
- Measures only in fact/measure table
- Controlled relationships (manual)

## Calculation Groups

The model includes a Time Intelligence calculation group to centralise time-based logic.

This allows dynamic transformation of base measures using SELECTEDMEASURE(), reducing duplication and improving maintainability.