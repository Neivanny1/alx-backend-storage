-- script that creates table users
-- with id,name and email,
-- country, enumeration of countries: US, CO and TN, never null
use holberton;
CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `name` VARCHAR(255),
    `country` ENUM('US', 'CO', 'TN') NOT NULL 
)
