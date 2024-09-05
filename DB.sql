-- Fresh setup of the database


-- A table to hold all the users data and metadata
CREATE TABLE users (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    uuid  VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(255) UNIQUE NOT NULL,
    passwrd VARCHAR(255) DEFAULT NULL,
    access ENUM('viewer', 'weather_station', 'admin') DEFAULT 'viewer'
);

-- A table to associate a user with metadata
CREATE TABLE users_metadata (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    uuid VARCHAR(255) UNIQUE NOT NULL,
    active BOOLEAN,
    reset_pass BOOLEAN,
    last_login DATETIME DEFAULT NULL,

    CONSTRAINT fk_uuid_mtd FOREIGN KEY (uuid) REFERENCES users(uuid)
);

-- Weather Data
CREATE TABLE weather_data (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    insert_dttime DATETIME,-- datetime of when the data was inserted
    station_id VARCHAR(255) UNIQUE NOT NULL,-- the user uuid (weather station id)
    
    -- Actual Weather Data
    temperature_celsius FLOAT(5, 2),-- The temperature (in celsius). BEWARE OF ROUNDING (5 digits in total, 2 of them are decimals)
    humidity FLOAT(5, 2),-- The humidity (in percentage). 0.00% up to 100.00%
    wind_speed_ms FLOAT(5, 2),-- The wind speed (in m/s).
    wind_direction_degrees SMALLINT,-- The wind direction (in degrees). 0 to 360 degrees
    bar_pressure_mbars FLOAT(4, 1),-- Barometer pressure (in millibars). Typical atmospheric pressure at sea level is 1.013.2 millibars

    CONSTRAINT fk_uuid_wthdt FOREIGN KEY (station_id) REFERENCES users(uuid)
);

-- Create the admin user
SELECT @admin_uuid:=UUID();
INSERT INTO users (
    uuid,
    username,
    passwrd,
    access
) VALUES (
    @admin_uuid,
    'admin',
    'password',
    'admin'
);

INSERT INTO users_metadata (
    uuid,
    active,
    reset_pass
) VALUES (
    @admin_uuid,
    TRUE,-- active
    TRUE-- reset password
);
