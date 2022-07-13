"""
1581. Customer Who Visited but Did Not Make Any Transactions from Leetcode.

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| visit_id    | int     |
| customer_id | int     |
+-------------+---------+
visit_id is the primary key for this table.
This table contains information about the customers who visited the mall.

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| transaction_id | int     |
| visit_id       | int     |
| amount         | int     |
+----------------+---------+
transaction_id is the primary key for this table.
This table contains information about the transactions made during
the visit_id.

***
Write an SQL query to find the IDs of the users
who visited without making any transactions and
the number of times they made these types of visits.

Return the result table sorted in any order.

The query result format is in the following example.
"""

# Write your MySQL query statement below
"""
SELECT DISTINCT customer_id, count(customer_id) AS count_no_trans
FROM visits
WHERE visit_id NOT IN (
	SELECT visit_id FROM transactions
)
GROUP BY customer_id
;
"""
