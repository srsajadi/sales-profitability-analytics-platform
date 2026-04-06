# Calculation Groups — Time Intelligence

## Overview
A Time Intelligence calculation group has been introduced to centralise and standardise time-based calculations across the semantic model.

This replaces the need for multiple individual time-based measures (e.g. Revenue LY, Revenue YoY, Revenue YTD), reducing duplication and improving maintainability.

---

## Motivation

Previously, time intelligence was implemented using separate measures:
- Revenue LY
- Revenue YoY
- Revenue YoY %
- Revenue MTD
- Revenue YTD

This approach leads to:
- measure proliferation
- duplicated logic
- increased maintenance overhead

The calculation group provides a reusable abstraction layer that applies time logic dynamically to any base measure.

---

## Implementation Details

### Calculation Group Name
Time Intelligence

### Column
Time Calculation

### Precedence
1

### Required Model Setting
DiscourageImplicitMeasures = true

This ensures that all calculations operate on explicit measures only, which is required for calculation groups.

---

## Calculation Items

| Name     | Description |
|----------|-------------|
| Current  | Base measure without modification |
| PY       | Same period in previous year |
| YoY      | Absolute difference between current and PY |
| YoY %    | Percentage change vs PY |
| MTD      | Month-to-date aggregation |
| YTD      | Year-to-date aggregation |
| PM       | Previous month |
| MoM      | Absolute change vs previous month |
| MoM %    | Percentage change vs previous month |

---

## Example Usage

### Matrix Visual

- Rows: DimDate[YearMonth]
- Columns: Time Intelligence[Time Calculation]
- Values: Total Revenue

This produces a multi-column view of the same base measure under different time contexts.

---

### Slicer Usage

The calculation group column can be used as a slicer to dynamically switch time context across visuals.

Example:
- Selecting "YTD" applies YTD logic to all measures in the visual.

---

## Benefits

- Reduces number of required measures
- Centralises time intelligence logic
- Improves model readability
- Enables dynamic analysis via slicers
- Aligns with enterprise semantic model practices

---

## Notes and Limitations

- Calculation groups only work with explicit measures
- Implicit aggregations (auto SUM, COUNT) are not supported
- Requires a valid and marked Date table (DimDate)
- Depends on correct date relationships

---

## Refactoring Plan

The following measures can be deprecated or retained for reference:

Candidate for removal:
- Revenue LY
- Revenue YoY
- Revenue YoY %
- Revenue MTD
- Revenue YTD

Recommended approach:
- Keep base measures (e.g. Total Revenue)
- Use calculation group for all time-based variations

---

## Future Enhancements

- Add Rolling 3M / 6M / 12M calculations
- Add QTD and PYTD calculations
- Introduce dynamic format strings for % vs currency
- Extend calculation groups for other domains (e.g. scenario analysis)