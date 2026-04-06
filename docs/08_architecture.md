# Architecture

## Overview
The solution follows a layered architecture separating data ingestion, transformation, modelling, and presentation.

## Layers

### 1. Data Source Layer
Raw transactional data (CSV / generated data)

### 2. Transformation Layer
Power Query (M):
- Data cleaning
- Type handling
- Derived columns

### 3. Data Model Layer
Power BI Model:
- Star schema
- Fact + Dimensions
- Relationships

### 4. Semantic Layer
DAX Measures:
- KPIs
- Time intelligence
- Business logic

### 5. Presentation Layer
Power BI Reports:
- Executive dashboard
- Sales analysis
- Profitability analysis

### 6. Deployment Layer
Power BI Service:
- Publishing reports
- Sharing dashboards
- Managing access

## Future Architecture (Extension)
Source → ETL (ADF / dbt) → Data Warehouse → Semantic Model → Power BI

## Design Principles
- Separation of concerns
- Reusable logic
- Scalable architecture
- Business-driven modelling