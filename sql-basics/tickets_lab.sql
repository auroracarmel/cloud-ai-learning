-- Sample data for a beginner SQL lab.
CREATE TABLE tickets (id INTEGER, issue TEXT, status TEXT);

INSERT INTO tickets (id, issue, status)
VALUES (1, 'Password rest', 'Open');

INSERT INTO tickets (id, issue, status)
VALUES (2, 'printer offline', 'closed');

SELECT * FROM tickets;
SELECT issue FROM tickets WHERE status = 'Open';
SELECT issue FROM tickets WHERE status = 'closed';