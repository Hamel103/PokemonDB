-- INITIALIZING TABLES
DROP TABLE PokemonAbilities;
DROP TABLE Pokemon;
DROP TABLE Abilities;
DROP TABLE Types;

CREATE TABLE Types (
  type_id INT AUTO_INCREMENT PRIMARY KEY,
  type_name VARCHAR(10)
);

CREATE TABLE Abilities (
  ability_id INT AUTO_INCREMENT PRIMARY KEY,
  ability_name VARCHAR(32)
);

CREATE TABLE Pokemon (
  dex_num INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(12) NOT NULL,
  type_one VARCHAR(10) NOT NULL,
  type_two VARCHAR(10) NOT NULL,
  ability_name VARCHAR(32) NOT NULL,
  FOREIGN KEY (type_one) REFERENCES Types(type_name),
  FOREIGN KEY (type_two) REFERENCES Types(type_name),
  FOREIGN KEY (ability_id) REFERENCES Abilities(ability_id)
  ON UPDATE NO ACTION
  ON DELETE CASCADE
);

CREATE TABLE PokemonAbilities (
  dex_num INT NOT NULL,
  ability_id INT NOT NULL,
  FOREIGN KEY (dex_num) REFERENCES Pokemon(dex_num),
  FOREIGN KEY (ability_id) REFERENCES Abilities(ability_id)
  ON UPDATE NO ACTION
  ON DELETE CASCADE
);
