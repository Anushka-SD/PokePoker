-- SQLBook: Code
SHOW DATABASEs;

CREATE TABLE IF NOT EXISTS pokemon (
    PokeId INT,
    name VARCHAR(50),
    Health_Points INT,
    Attack_Points INT,
    Category VARCHAR(20)
);

DROP TABLE owns;
DROP TABLE users;

CREATE TABLE IF NOT EXISTS users (
    userId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    no_of_cards INT DEFAULT 4,
    COINS INT DEFAULT 0,
    points INT DEFAULT 0,
    Played_matches INT,
    won_matches INT
);

INSERT INTO users (username, no_of_cards, COINS, points, Played_matches, won_matches) VALUES
('Ana', 4, 200, 500, 10, 8),
('Vedi', 4, 400, 600, 12, 9),
('Shri', 4, 300, 700, 15, 11),
('Rish', 4, 100, 400, 8, 6);
CREATE TABLE owns (
    userId INT NOT NULL,
    pokeId INT NOT NULL PRIMARY KEY,
    matches_left INT DEFAULT 3,
    FOREIGN KEY (userId) REFERENCES users(userId),
    FOREIGN KEY (pokeId) REFERENCES pokemon(PokeId)
);


INSERT INTO pokemon (PokeId, name, Health_Points, Attack_Points, Category) VALUES
(1, 'Weedle', 50, 10, 'grass'),
(2, 'Caterpie', 50, 20, 'grass'),
(3, 'Bulbasaur', 60, 20, 'grass'),
(4, 'Venusaur', 140, 50, 'grass'),
(5, 'Beedrill I', 90, 65, 'grass'),
(6, 'Metapod', 70, 40, 'grass'),
(7, 'Crobat I', 90, 30, 'grass'),
(8, 'Celebi & Venusaur-GX', 270, 50, 'grass'),
(9, 'Lotad', 60, 60, 'grass'),
(10, 'Deerling', 60, 20, 'grass'),
(11, 'Cherrim', 80, 40, 'grass'),
(12, 'Kakuna', 80, 20, 'grass'),
(13, 'Ludicolo', 140, 70, 'grass'),
(14, 'Alolan Exeggutor', 160, 80, 'grass'),
(15, 'Tangela', 80, 30, 'grass'),
(16, 'Venusaur & Snivy-GX', 270, 160, 'grass'),
(17, 'Celebi V', 190, 60, 'grass'),
(18, 'Bellsprout', 50, 10, 'grass'),
(19, 'Oddish', 50, 20, 'grass'),
(20, 'Chikorita', 60, 10, 'grass'),
(21, 'Azumarill', 90, 30, 'Water'),
(22, 'Blastoise', 130, 20, 'Water'),
(23, 'Articuno', 70, 30, 'Water'),
(24, 'Oshawott', 60, 30, 'Water'),
(25, 'Kingdra', 90, 30, 'Water'),
(26, 'Swampert', 110, 60, 'Water'),
(27, 'Crawdaunt', 90, 50, 'Water'),
(28, 'Manaphy', 70, 20, 'Water'),
(29, 'Seadra', 90, 10, 'Water'),
(30, 'Horsea', 60, 10, 'Water'),
(31, 'Gyarados', 130, 30, 'Water'),
(32, 'Froslass', 80, 50, 'Water'),
(33, 'Psyduck', 80, 10, 'Water'),
(34, 'Vaporeon', 70, 20, 'Water'),
(35, 'Mudkip', 50, 10, 'Water'),
(36, 'Buizel', 60, 30, 'Water'),
(37, 'Kyogre', 80, 40, 'Water'),
(38, 'Mamoswine', 140, 40, 'Water'),
(39, 'Lapras', 120, 20, 'Water'),
(40, 'Omastar', 100, 10, 'Water'),
(41, 'Dialga', 100, 20, 'metal'),
(42, 'Deoxys', 200, 150, 'metal'),
(43, 'Dialga-EX', 180, 60, 'metal'),
(44, 'Forretress', 90, 30, 'metal'),
(45, 'Probopass', 110, 30, 'metal'),
(46, 'Bastiodon GL', 90, 30, 'metal'),
(47, 'Magneton', 60, 30, 'metal'),
(48, 'Dark Scizor', 70, 30, 'metal'),
(49, 'Shieldon', 80, 20, 'metal'),
(50, 'Jolteon', 70, 40, 'metal'),
(51, 'Dugtrio', 80, 30, 'metal'),
(52, 'Metagross', 130, 70, 'metal'),
(53, 'Aggron', 90, 50, 'metal'),
(54, 'Magnemite', 40, 50, 'metal'),
(55, 'Jirachi', 60, 20, 'metal'),
(56, 'Magnezone', 120, 50, 'metal'),
(57, 'Klink', 50, 10, 'metal'),
(58, 'Scizor', 90, 50, 'metal'),
(59, 'Klefki', 60, 30, 'metal'),
(60, 'Registeel ex', 90, 10, 'metal'),
(61, 'Arcanine', 110, 50, 'fire'),
(62, 'Moltres', 90, 90, 'fire'),
(63, 'Chimchar', 50, 10, 'fire'),
(64, 'Blaziken FB', 110, 80, 'fire'),
(65, 'Heat Rotom', 90, 80, 'fire'),
(66, 'Ponyta', 60, 10, 'fire'),
(67, 'Charmeleon', 80, 30, 'fire'),
(68, 'Blaziken', 130, 40, 'fire'),
(69, 'Ninetales', 90, 60, 'fire'),
(70, 'Magmar', 80, 60, 'fire'),
(71, 'Charizard', 150, 30, 'fire'),
(72, 'Ho-Oh', 80, 20, 'fire'),
(73, 'Torchic', 60, 10, 'fire'),
(74, 'Victini', 60, 30, 'fire'),
(75, 'Growlithe', 80, 30, 'fire'),
(76, 'Rapidash', 100, 60, 'fire'),
(77, 'Entei', 80, 60, 'fire'),
(78, 'Flareon', 70, 10, 'fire'),
(79, 'Scorbunny', 60, 30, 'fire'),
(80, 'Charmander', 60, 20, 'fire'),
(81, 'Ampharos', 130, 70, 'lightning'),
(82, 'Zebstrika', 90, 40, 'lightning'),
(83, 'Dark Ampharos', 120, 30, 'lightning'),
(84, 'Lig_Magneton', 80, 30, 'lightning'),
(85, 'Dragonite I', 100, 30, 'lightning'),
(86, 'Elekid', 40, 50, 'lightning'),
(87, 'Pikachu', 60, 20, 'lightning'),
(88, 'Tynamo', 40, 10, 'lightning'),
(89, 'Luxray', 120, 30, 'lightning'),
(90, 'Chinchou', 70, 10, 'lightning'),
(91, 'Dark Electrode', 70, 30, 'lightning'),
(92, 'Electivire', 100, 60, 'lightning'),
(93, 'Electabuzz', 60, 20, 'lightning'),
(94, 'Plusle', 60, 20, 'lightning'),
(95, 'Raichu', 90, 30, 'lightning'),
(96, 'Electivire FB', 90, 40, 'lightning'),
(97, 'Pachirisu', 70, 20, 'lightning'),
(98, 'Manectric', 70, 10, 'lightning'),
(99, 'Minun', 70, 30, 'lightning'),
(100, 'Electrode', 70, 30, 'lightning'),
(101, 'psy_Jirachi', 110, 70, 'psychic'),
(102, 'Alakazam', 80, 30, 'psychic'),
(103, 'Dusknoir', 120, 60, 'psychic'),
(104, 'Lugia', 80, 20, 'psychic'),
(105, 'Cresselia', 80, 50, 'psychic'),
(106, 'Espeon I', 70, 30, 'psychic'),
(107, 'Gardevoir', 120, 60, 'psychic'),
(108, 'Gengar', 100, 40, 'psychic'),
(109, 'Gallade E4', 80, 20, 'psychic'),
(110, 'Mewtwo', 70, 20, 'psychic'),
(111, 'Mew', 70, 40, 'psychic'),
(112, 'Dark Espeon', 60, 10, 'psychic'),
(113, 'Celebi', 70, 40, 'psychic'),
(114, 'Haunter', 50, 10, 'psychic'),
(115, 'Hypno', 80, 60, 'psychic'),
(116, 'Dark Hypno', 70, 40, 'psychic'),
(117, 'Gastly', 50, 10, 'psychic'),
(118, 'psy_Metagross', 130, 60, 'psychic'),
(119, 'Kadabra', 60, 50, 'psychic'),
(120, 'Togetic', 80, 30, 'psychic');

SELECT * FROM pokemon

SELECT * FROM attackingpower;

SELECT * FROM users;



SELECT routine_name
FROM information_schema.routines
WHERE routine_type = 'PROCEDURE';

SELECT * FROM users;




DROP TABLE battle;

CREATE TABLE battle (
    matchId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user1_points INT DEFAULT 0,
    user2_points INT DEFAULT 0,
    user1_id INT NOT NULL UNIQUE,
    user2_id INT NOT NULL UNIQUE,
    winner VARCHAR(20) NOT NULL
);



DELIMITER //
CREATE PROCEDURE availablepoke()
BEGIN
    SELECT PokeId, name FROM pokemon WHERE PokeId NOT IN (SELECT pokeId FROM owns);
END //
DELIMITER ;

CALL availablepoke();

DELIMITER //

--IF NOT EXISTS
CREATE PROCEDURE PurchaseCard(IN p_userId INT, IN p_pokeName VARCHAR(50))
BEGIN
    DECLARE card_cost INT;
    DECLARE user_coins INT;
    DECLARE p_pokeId INT;
    
    -- Get the cost of the card (assuming each Pokémon costs 100 coins)
    SET card_cost = 100;
    
    -- Get the user's current coins
    SELECT COINS INTO user_coins FROM users WHERE userId = p_userId;

    SELECT pokeId INTO p_pokeId FROM pokemon WHERE name=p_pokeName;
    
    -- Check if the user has enough coins to purchase the card
    IF user_coins >= card_cost THEN
        -- Deduct the card cost from the user's coins
        UPDATE users SET COINS = user_coins - card_cost WHERE userId = p_userId;
        UPDATE users SET no_of_cards = no_of_cards + 1 WHERE userId = p_userId;
        
        INSERT INTO owns (userId, pokeId, matches_left)
        VALUES (p_userId, p_pokeId, 3);
      
        SELECT 'Card purchased successfully.' AS message;
    ELSE
        SELECT 'Insufficient coins to purchase the card.' AS message;
    END IF;
END //

DELIMITER ;

CALL PurchaseCard(1, "Raichu");

UPDATE users SET COINS = 400 WHERE userId = 1;

SELECT * FROM users;
SELECT * FROM owns;

DELIMITER //
CREATE PROCEDURE create_user(
       IN p_username VARCHAR(20)
     )
     BEGIN
         DECLARE user_exists INT;
   
         -- Check if the user already exists
         SELECT COUNT(*) INTO user_exists FROM users WHERE username = p_username;
    
         IF user_exists = 0 THEN
             -- User does not exist, so create a new user
             INSERT INTO users (username) VALUES (p_username);
    
             -- Get the ID of the newly created user
             SET @user_id = LAST_INSERT_ID();
    
             -- Assign four random Pokemon to the new user
             SET @counter = 0;
             WHILE @counter < 4 DO
                 -- Get a random Pokemon ID
                 SET @random_pokemon_id = (SELECT PokeId FROM pokemon ORDER BY RAND() LIMIT 1);
    
                 -- Check if the user already owns this Pokemon
                 SET @already_owned = (SELECT COUNT(*) FROM owns WHERE userId = @user_id AND pokeId = @random_pokemon_id);
    
                 IF @already_owned = 0 THEN
                     -- User does not already own this Pokemon, so assign it
                     INSERT INTO owns (userId, pokeId) VALUES (@user_id, @random_pokemon_id);
                     SET @counter = @counter + 1;
                 END IF;
             END WHILE;
         END IF;
     END //
DELIMITER ;

CALL create_user("Isha");

DELIMITER //
CREATE PROCEDURE GetUserCards(IN user_id INT)
BEGIN
    -- Declare variables
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_card_id INT;
    DECLARE user_card_name VARCHAR(50);
    
    -- Cursor for fetching user's cards
    DECLARE cur CURSOR FOR
    SELECT pokemon.PokeId, pokemon.name
    FROM owns
    INNER JOIN pokemon ON owns.pokeId = pokemon.PokeId
    WHERE owns.userId = user_id;
    
    -- Declare continue handler for cursor
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Create temporary table to store user's cards
    CREATE TEMPORARY TABLE temp_user_cards (
        PokeId INT,
        name VARCHAR(50)
    );

    -- Open the cursor
    OPEN cur;

    -- Fetch cards and insert into temporary table
    read_loop: LOOP
        FETCH cur INTO user_card_id, user_card_name;
        IF done THEN
            LEAVE read_loop;
        END IF;
        INSERT INTO temp_user_cards (PokeId, name) VALUES (user_card_id, user_card_name);
    END LOOP;

    -- Close the cursor
    CLOSE cur;

    -- Select the user's cards from the temporary table
    SELECT * FROM temp_user_cards;

    -- Drop the temporary table
    DROP TEMPORARY TABLE IF EXISTS temp_user_cards;
END //
DELIMITER ;


-- DELIMITER //
-- CREATE PROCEDURE GetUserCards(IN user_id INT)
-- BEGIN
--     -- Select the user's cards directly
--     SELECT pokemon.PokeId, pokemon.name
--     FROM owns
--     INNER JOIN pokemon ON owns.pokeId = pokemon.PokeId
--     WHERE owns.userId = user_id;
-- END //
-- DELIMITER ;

CALL GetUserCards(1);

DROP TABLE temp_user_cards;


DELIMITER //
CREATE PROCEDURE GetRank(IN p_userId INT)
BEGIN
    DECLARE user_rank INT;
    
    -- Get the rank of the user
    SELECT COUNT(*) + 1 INTO user_rank
    FROM users
    WHERE points > (SELECT points FROM users WHERE userId = p_userId);
    
    -- If no one has more points than the user, their rank is 1
    IF user_rank IS NULL THEN
        SET user_rank = 1;
    END IF;
    
    -- Display the rank
    SELECT user_rank;
END //
DELIMITER ;

CALL GetRank(2);

SELECT * FROM users;

-- DROP TABLE users;
-- DROP TABLE owns;
DROP PROCEDURE `GetAllRanks`;

DELIMITER //

CREATE PROCEDURE GetAllRanks()
BEGIN
    -- Display the ranks of all users ordered by points in descending order
    SELECT 
        username,
        points,
        (SELECT COUNT(*) + 1 FROM users AS u WHERE u.points > nu.points) AS user_rank
    FROM users AS nu
    ORDER BY points DESC;
END //



DELIMITER ;

CALL GetAllRanks();

SELECT * FROM pokemon;
