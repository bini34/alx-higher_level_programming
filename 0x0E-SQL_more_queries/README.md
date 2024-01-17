# Project: 0x0E. SQL - More queries

## Description

This project focuses on advanced SQL queries and database management using MySQL. It covers topics such as user privileges, creating databases and tables, working with constraints, subqueries, joins, and more. The tasks involve creating scripts to perform specific actions and demonstrate understanding of SQL concepts.

## Project Files

1. **0-privileges.sql**: Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (localhost).

2. **1-create_user.sql**: Write a script that creates the MySQL server user `user_0d_1`. This user should have all privileges on your MySQL server, and the password should be set to `user_0d_1_pwd`. If the user `user_0d_1` already exists, your script should not fail.

3. **2-create_read_user.sql**: Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2`. The `user_0d_2` should have only SELECT privilege in the database `hbtn_0d_2`. The password for `user_0d_2` should be set to `user_0d_2_pwd`. If the database `hbtn_0d_2` or the user `user_0d_2` already exists, your script should not fail.

4. **3-force_name.sql**: Write a script that creates the table `force_name` on your MySQL server. The `force_name` table should have columns `id` (INT) and `name` (VARCHAR(256)), where `name` cannot be null.

5. **4-never_empty.sql**: Write a script that creates the table `id_not_null` on your MySQL server. The `id_not_null` table should have columns `id` (INT) with the default value 1 and `name` (VARCHAR(256)).

6. **5-unique_id.sql**: Write a script that creates the table `unique_id` on your MySQL server. The `unique_id` table should have columns `id` (INT) with the default value 1 and must be unique, and `name` (VARCHAR(256)).

7. **6-states.sql**: Write a script that creates the database `hbtn_0d_usa` and the table `states` in the database `hbtn_0d_usa` on your MySQL server. The `states` table should have columns `id` (INT), which is unique, auto-generated, and cannot be null, and `name` (VARCHAR(256)), which cannot be null.

8. **7-cities.sql**: Write a script that creates the database `hbtn_0d_usa` and the table `cities` in the database `hbtn_0d_usa` on your MySQL server. The `cities` table should have columns `id` (INT), which is unique, auto-generated, and cannot be null, `state_id` (INT), which cannot be null and must be a FOREIGN KEY referencing `id` in the `states` table, and `name` (VARCHAR(256)), which cannot be null.

9. **8-cities_of_california_subquery.sql**: Write a script that lists all the cities of California that can be found in the database `hbtn_0d_usa`. Results should be sorted in ascending order by `cities.id`. You are not allowed to use the JOIN keyword.

10. **9-cities_by_state_join.sql**: Write a script that lists all cities contained in the database `hbtn_0d_usa`. Each record should display: `cities.id - cities.name - states.name`. Results must be sorted in ascending order by `cities.id`.

11. **10-genre_id_by_show.sql**: Write a script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked. Each record should display: `tv_shows.title - tv_show_genres.genre_id`. Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`.

12. **11-genre_id_all_shows.sql**: Write a script that lists all shows contained in the database `hbtn_0d_tvshows`. Each record should display: `tv_shows.title - tv_show_genres.genre_id`. Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`. If a show doesn’t have a genre, display NULL.

13. **12-no_genre.sql**: Write a script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked. Each record should display: `tv_shows.title - tv_show_genres.genre_id`. Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`.

14. **13-count_shows_by_genre.sql**: Write a script that lists all genres

 from the database `hbtn_0d_tvshows`. Each record should display: `genres.name - COUNT(tv_shows.id)`. Results must be sorted in descending order by the count of shows.

15. **14-my_genres.sql**: Write a script that uses the `hbtn_0d_tvshows` database to lists all genres of the show Dexter. Results should display: `genres.name`. Results must be sorted in ascending order by `genres.name`.

16. **15-comedy_only.sql**: Write a script that lists all Comedy shows in the database `hbtn_0d_tvshows`. Each record should display: `tv_shows.title`. Results must be sorted in ascending order by `tv_shows.title`.

17. **16-shows_by_genre.sql**: Write a script that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`. Each record should display: `tv_shows.title - genres.name`. Results must be sorted in ascending order by `tv_shows.title` and `genres.name`.

18. **17-not_my_genres.sql**: Write a script that uses the `hbtn_0d_tvshows` database to list all genres not linked to the show Dexter. Results should display: `genres.name`. Results must be sorted in ascending order by `genres.name`.

19. **18-not_a_comedy.sql**: Write a script that lists all shows not listed as Comedy in the database `hbtn_0d_tvshows`. Each record should display: `tv_shows.title`. Results must be sorted in ascending order by `tv_shows.title`.

20. **19-no_comedy.sql**: Write a script that lists all genres in the database `hbtn_0d_tvshows` which are not Comedy. Each record should display: `genres.name`. Results must be sorted in ascending order by `genres.name`.

21. **20-ratings.sql**: Write a script that lists all shows from the database `hbtn_0d_tvshows_rates` and their average rating. Results should be sorted in descending order by the average rating. The rating should be rounded to one decimal place.

22. **21-referenced_by.sql**: Write a script that lists all shows from the database `hbtn_0d_tvshows_rates` and their genres. Results should display: `tv_shows.title - GROUP_CONCAT(genres.name)`. Results must be sorted in ascending order by `tv_shows.title`.

23. **22-average_shows.sql**: Write a script that lists all genres in the database `hbtn_0d_tvshows_rates` and the average rating of shows linked to each genre. Results should display: `genres.name - AVG(rating)`. Results must be sorted in descending order by the average rating. The rating should be rounded to one decimal place.

24. **23-genres_by_ratings.sql**: Write a script that lists all genres in the database `hbtn_0d_tvshows_rates` and the average rating. Results should display: `genres.name - AVG(rating)`. Results must be sorted in descending order by the average rating. The rating should be rounded to one decimal place.

## Environment
This project is designed to be run on a MySQL server. The SQL scripts should be executed on a MySQL database.

## Usage
To test the scripts, you can execute them on a MySQL server. You can use the MySQL command-line tool or a MySQL GUI like MySQL Workbench. Make sure to create a database named `hbtn_0d_usa` before executing the scripts.

**Example:**
```bash
mysql -h localhost -u root -p < 0-privileges.sql
```

Replace `root` with your MySQL username, and you will be prompted to enter the password.

Note: Ensure that you have the necessary privileges to perform the actions specified in the scripts.
