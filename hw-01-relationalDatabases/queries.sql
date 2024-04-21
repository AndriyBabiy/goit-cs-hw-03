-- Отримати всі завдання певного користувача. Використайте SELECT для отримання завдань конкретного користувача за його user_id.
SELECT * 
FROM postgres.public.tasks t
WHERE user_id = '43';

-- Вибрати завдання за певним статусом. Використайте підзапит для вибору завдань з конкретним статусом, наприклад, 'new'.
SELECT * 
FROM postgres.public.tasks t 
JOIN postgres.public.status s on t.status_id = s.id
WHERE s.name = 'new';

-- Оновити статус конкретного завдання. Змініть статус конкретного завдання на 'in progress' або інший статус.
UPDATE postgres.public.tasks t 
SET status_id = 3
WHERE id = 4;

-- Отримати список користувачів, які не мають жодного завдання. Використайте комбінацію SELECT, WHERE NOT IN і підзапит.
SELECT *
FROM postgres.public.users u
WHERE id NOT IN (SELECT user_id FROM postgres.public.tasks);

-- Додати нове завдання для конкретного користувача. Використайте INSERT для додавання нового завдання.
INSERT INTO postgres.public.tasks (title, description, status_id, user_id)
VALUES ('very difficult task', 'this is a very difficult task that has many steps', 1,41 );

-- Отримати всі завдання, які ще не завершено. Виберіть завдання, чий статус не є 'завершено'.
SELECT *
FROM postgres.public.tasks t
WHERE t.status_id != 3;

-- Видалити конкретне завдання. Використайте DELETE для видалення завдання за його id.
DELETE FROM postgres.public.tasks WHERE id=16;

-- Знайти користувачів з певною електронною поштою. Використайте SELECT із умовою LIKE для фільтрації за електронною поштою.
SELECT *
FROM postgres.public.users u
WHERE u.email LIKE '%@example.com';

-- Оновити ім'я користувача. Змініть ім'я користувача за допомогою UPDATE.
UPDATE postgres.public.users u
SET fullname='Charlie Valenzuela'
WHERE fullname='Charles Valenzuela';

-- Отримати кількість завдань для кожного статусу. Використайте SELECT, COUNT, GROUP BY для групування завдань за статусами.
SELECT s.name, COUNT(*)
FROM postgres.public.tasks t
JOIN postgres.public.status s ON t.status_id = s.id
GROUP BY s.name, s.id
ORDER BY s.id;

-- Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти. 
-- Використайте SELECT з умовою LIKE в поєднанні з JOIN, щоб вибрати завдання, призначені користувачам, чия електронна пошта містить певний домен (наприклад, '%@example.com').
SELECT *
FROM postgres.public.tasks t
JOIN postgres.public.users u ON t.user_id = u.id
WHERE u.email LIKE '%example.com';

-- Отримати список завдань, що не мають опису. Виберіть завдання, у яких відсутній опис.
SELECT *
FROM postgres.public.tasks t
WHERE t.description IS NULL;

-- Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. Використайте INNER JOIN для отримання списку користувачів та їхніх завдань із певним статусом.
SELECT u.fullname, t.id, t.title, t.description, s.name
FROM postgres.public.users u
LEFT JOIN postgres.public.tasks t on u.id = t.user_id
JOIN postgres.public.status s on t.status_id = s.id
WHERE s.name = 'in progress';

-- Отримати користувачів та кількість їхніх завдань. Використайте LEFT JOIN та GROUP BY для вибору користувачів та підрахунку їхніх завдань.
SELECT u.fullname, count(t.id)
FROM postgres.public.users u
LEFT JOIN postgres.public.tasks t on u.id = t.user_id
GROUP BY u.id;