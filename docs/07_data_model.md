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
- Dim tables → FactSales (one-to-many)
- Single direction filtering
- Star schema enforced

## Design Principles
- No snowflake schema
- No bidirectional relationships
- Measures only in fact/measure table
- Controlled relationships (manual)