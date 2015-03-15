# Set password to the 'root'
mysqladmin -u root password NEWPASSWORD
mysqladmin -u root -p'oldpassword' password newpass
mysqladmin -u user -p oldpassword password newpass

# backup y restarurar base de datos     #
mysqldump -h localhost -u user -p bd > backup.sql
mysqldump -user -pPASS bd [tables] > filename

# restarurar: el usuario debe estar creado con los privilegios y la bd
mysql -h localhost -u user -p database_name < backup.sql

# Enable remote connections
/etc/mysql/my.cnf
# comment the following line
bind-address = 127.0.0.1
# restart
/etc/init.d/mysql restart

-- Restore root password
$ /etc/init.d/mysql stop
$ mysqld_safe --skip-grant-tables &
$ mysql -u root mysql
mysql> UPDATE user SET Password=PASSWORD('nueva_contraseña') WHERE User='root';
mysql> FLUSH PRIVILEGES;
mysql> \q
$ killall mysqld;
$ /etc/init.d/mysql start

-- Change root password (Windows)
USE mysql
SET Password FOR 'root'@'localhost' = PASSWORD('new_password');
SET Password FOR 'root'@'%' = PASSWORD('new_password');
-- Change root password (Linux)
USE mysql
SET PASSWORD FOR ''@'localhost' = PASSWORD('new_password');
SET PASSWORD FOR ''@'host_name' = PASSWORD('new_password');

-- database create/delete management
CREATE DATABASE database_name DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
DROP DATABASE database_name;

-- user management
SELECT Host, User, Password FROM mysql.user
CREATE USER usuario; -- IDENTIFIED BY 'password'
UPDATE users SET password=PASSWORD('password') WHERE user='usuario';
DROP USER usuario;

-- GRANT tipo_privilegio ON {nombre_tabla | * | *.* | nombre_bd.*} TO usuario;
-- REVOKE tipo_privilegio ON {nombre_tabla | * | *.* | nombre_bd.*} FROM usuario;
GRANT SELECT ON *.* TO usuario;
GRANT ALL ON db.* TO usuario@localhost IDENTIFIED BY 'pass';
GRANT ALL ON bizdex.* TO bizdexuser@localhost IDENTIFIED BY 'bizdexpass';

-- alter table
ALTER TABLE table_name DROP COLUMN column_name;
ALTER TABLE table_name ADD COLUMN column_name varchar (20);
ALTER TABLE table_name CHANGE old_column_name new_column_name varchar (50);
ALTER TABLE table_name MODIFY column_name VARCHAR(3);
ALTER TABLE table_name DROP INDEX column_name;

-- Make a unique column so you get no dupes.
ALTER TABLE table_name ADD UNIQUE (column_name);

-- https://www3.ntu.edu.sg/home/ehchua/programming/sql/SampleDatabases.html
-- Creating Tables
CREATE TABLE Students (
    id bigint UNSIGNED NOT NULL AUTO_INCREMENT,
    name varchar(30) NOT NULL,
    nick varchar(20),
    description TEXT,
    PRIMARY KEY (id),
    FULLTEXT KEY idx_title_description (name, description)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

CREATE TABLE employees (
    emp_no      INT             NOT NULL,  -- UNSIGNED AUTO_INCREMENT??
    birth_date  DATE            NOT NULL,
    first_name  VARCHAR(14)     NOT NULL,
    last_name   VARCHAR(16)     NOT NULL,
    gender      ENUM ('M','F')  NOT NULL,  -- Enumeration of either 'M' or 'F'
    hire_date   DATE            NOT NULL,
    PRIMARY KEY (emp_no)                   -- Index built automatically on primary-key column
                                           -- INDEX (first_name)
                                           -- INDEX (last_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE departments (
    dept_no     CHAR(4)         NOT NULL,  -- in the form of 'dxxx'
    dept_name   VARCHAR(40)     NOT NULL,
    PRIMARY KEY (dept_no),                 -- Index built automatically
    UNIQUE  KEY (dept_name)                -- Build INDEX on this unique-value column
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE dept_emp (
    emp_no      INT         NOT NULL,
    dept_no     CHAR(4)     NOT NULL,
    from_date   DATE        NOT NULL,
    to_date     DATE        NOT NULL,
    KEY         (emp_no),   -- Build INDEX on this non-unique-value column
    KEY         (dept_no),  -- Build INDEX on this non-unique-value column
    FOREIGN KEY (emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE,
           -- Cascade DELETE from parent table 'employee' to this child table
           -- If an emp_no is deleted from parent 'employee', all records
           --  involving this emp_no in this child table are also deleted
           -- ON UPDATE CASCADE??
    FOREIGN KEY (dept_no) REFERENCES departments (dept_no) ON DELETE CASCADE,
           -- ON UPDATE CASCADE??
    PRIMARY KEY (emp_no, dept_no)
           -- Might not be unique?? Need to include from_date
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



int(M)          int(5)
float(M,D)      float(12,3)
double(M,D)     double(20,3)
timestamp(M)    timestamp(8)    -- for YYYYMMDD
                timestamp(12)   -- for YYYYMMDDHHMMSS
char(M)         char(10)        -- Fixed-length strings
varchar(M)      varchar(20)     -- Variable-length strings
blob                            -- large ammount of binary data
text                            -- large string
enum('val1','val2', ...)        -- Values chosen from a list

-- insert basics
INSERT INTO Students VALUES
        ('Smith','John',123456789,'Math','Selleck');
INSERT INTO Students SET
        FirstName='John',
        LastName='Smith',
        StudentID=123456789,
        Major='Math';
INSERT INTO Students
        (StudentID,FirstName,LastName)
        VALUES (123456789,'John','Smith');

-- insert from another table
INSERT INTO Students
        (StudentID, FirstName, LastName)
        SELECT StudentID, FirstName, LastName
        FROM OtherStudentTable;
        WHERE LastName like '%son'

-- Deleteing data from tables
DELETE FROM students WHERE name='Smith';
DELETE FROM students WHERE name like '%Smith%';
DELETE FROM students; -- delte all !!!

UPDATE table SET
        column1=value1,
        column2=value2,
        ...
        columnk=valuek
        [WHERE condition(s)];

-- view table type MyISAM, innodb, ...
SHOW TABLE STATUS WHERE Name = 'table_name'
