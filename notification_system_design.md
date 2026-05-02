# Stage 1

This system is used to manage notifications for students.

Main features:
- Get notifications
- Create notification
- Mark notification as read

### Get Notifications
GET /notifications/{studentId}

Returns notifications of a student.

### Create Notification
POST /notifications

Creates a new notification.

### Mark as Read
PUT /notifications/{id}

Updates read status.

### Real-time system
WebSockets can be used to send notifications instantly.

---

# Stage 2

I would use MySQL because it is simple and structured.

Table: notifications

- id
- studentId
- message
- type
- isRead
- createdAt

Problem:
- Large data → slow queries

Solution:
- Use indexing
- Use pagination

---

# Stage 3

The query is correct but slow.

Reason:
- No index
- Large data

Fix:
Add index on:
(studentId, isRead, createdAt)

Time complexity:
- Without index → O(n)
- With index → O(log n)

Adding index on all columns is not good because it slows inserts.

Query for placement notifications:

SELECT DISTINCT studentId
FROM notifications
WHERE notificationType = 'placement'
AND createdAt >= NOW() - INTERVAL 7 DAY;

---

# Stage 4

Fetching data on every page load increases DB load.

Solutions:

1. Caching → faster but slightly outdated data
2. Pagination → less data load
3. Lazy loading → load only when needed
4. WebSockets → real-time updates

---

# Stage 5

Problems:
- Loop is slow
- No error handling
- No retry

Better approach:
Use queue system

Pseudo code:

function notify_all(student_ids, message):
    for student_id in student_ids:
        save_to_db(student_id, message)
        add_to_queue(student_id, message)

worker():
    while true:
        task = get_task()
        try:
            send_email(task)
        except:
            retry(task)

---

# Stage 6

Priority is based on:
Placement > Result > Event

Notifications are sorted using:
- Priority
- Time

Only top 10 are returned.
