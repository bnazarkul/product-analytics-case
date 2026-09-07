-- Product Analytics Case
-- Synthetic user activity dataset

-- 1. Total unique users
SELECT
    COUNT(DISTINCT user_id) AS total_users
FROM user_activity;


-- 2. Total active users
SELECT
    COUNT(DISTINCT user_id) AS active_users
FROM user_activity
WHERE event_type = 'login';


-- 3. Daily Active Users (DAU)
SELECT
    date,
    COUNT(DISTINCT user_id) AS dau
FROM user_activity
WHERE event_type = 'login'
GROUP BY date
ORDER BY date;


-- 4. Unique payment users
SELECT
    COUNT(DISTINCT user_id) AS payment_users
FROM user_activity
WHERE event_type = 'payment';


-- 5. Conversion from active user to payment user
WITH active_users AS (
    SELECT DISTINCT user_id
    FROM user_activity
    WHERE event_type = 'login'
),
payment_users AS (
    SELECT DISTINCT user_id
    FROM user_activity
    WHERE event_type = 'payment'
)
SELECT
    COUNT(DISTINCT p.user_id) * 100.0
    / COUNT(DISTINCT a.user_id) AS conversion_rate
FROM active_users a
LEFT JOIN payment_users p
    ON a.user_id = p.user_id;


-- 6. Total payment volume
SELECT
    SUM(amount) AS total_payment_volume
FROM user_activity
WHERE event_type = 'payment';


-- 7. Average payment amount
SELECT
    AVG(amount) AS average_payment_amount
FROM user_activity
WHERE event_type = 'payment';


-- 8. User activity by channel
SELECT
    channel,
    COUNT(*) AS event_count,
    COUNT(DISTINCT user_id) AS unique_users
FROM user_activity
GROUP BY channel
ORDER BY event_count DESC;


-- 9. Payment volume by channel
SELECT
    channel,
    COUNT(*) AS payment_count,
    SUM(amount) AS payment_volume,
    AVG(amount) AS average_payment_amount
FROM user_activity
WHERE event_type = 'payment'
GROUP BY channel
ORDER BY payment_volume DESC;


-- 10. Top users by payment volume
SELECT
    user_id,
    COUNT(*) AS payment_count,
    SUM(amount) AS payment_volume
FROM user_activity
WHERE event_type = 'payment'
GROUP BY user_id
ORDER BY payment_volume DESC;


-- 11. User activity frequency
SELECT
    user_id,
    COUNT(*) AS total_events,
    COUNT(DISTINCT date) AS active_days
FROM user_activity
GROUP BY user_id
ORDER BY active_days DESC, total_events DESC;


-- 12. Daily payment dynamics
SELECT
    date,
    COUNT(*) AS payment_count,
    SUM(amount) AS payment_volume
FROM user_activity
WHERE event_type = 'payment'
GROUP BY date
ORDER BY date;
