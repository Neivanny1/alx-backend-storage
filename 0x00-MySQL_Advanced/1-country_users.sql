-- script that creates table users
-- with id,name and email,
-- country, enumeration of countries: US, CO and TN, never null
use holberton;
CREATE TABLE IF NOT EXISTS `users` (
    `id` INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` VARCHAR(255),
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `country` ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
