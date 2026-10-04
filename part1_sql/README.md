# Part 1 SQL

## Query 4: Resellers with no orders

The `LEFT JOIN` identifies resellers who have no matching order rows.

For the zero-order reseller `RS024` (Ahmedabad Reseller 6):

- `COUNT(*) = 1`
- `COUNT(order_id) = 0`

`COUNT(*)` counts the unmatched row created by the `LEFT JOIN`, so it returns `1`.

`COUNT(order_id)` counts only non-NULL order IDs. Since RS024 has no matching order, it returns `0`.

Therefore, `COUNT(order_id)` is used to correctly identify the zero-order case.