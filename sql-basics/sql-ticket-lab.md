# SQL Ticket Database Lab

## Environment
SQLite database: tickets.db
Four fictional support tickets.

## Skills practised
- SELECT and WHERE to retrieve matching records.
- ORDER BY to sort results.
- COUNT(*) to count rows.
- GROUP BY to count tickets by status.
- UPDATE with WHERE to change one ticket.

## Verified results
Before updating ticket 4:
- Total tickets: 4
- Open: 3
- Closed: 1

After changing ticket 4 to Closed:
- Total tickets: 4
- Open: 2
- Closed: 2

I queried ticket 4 separately and confirmed:
(4, 'Email issue', 'Closed')

## Important lesson
WHERE limits which rows an UPDATE changes.
Without WHERE, the update would affect every row.