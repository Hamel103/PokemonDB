-- INITIALIZING TABLES
DROP TABLE PokemonAbilities;
DROP TABLE Pokemon;
DROP TABLE Abilities;
DROP TABLE Type;

CREATE TABLE Type (
  type_id INT AUTO_INCREMENT PRIMARY KEY,
  type_name VARCHAR(32)
);

CREATE TABLE Abilities (
  ability_id INT AUTO_INCREMENT PRIMARY KEY,
  ability_name VARCHAR(32)
);

CREATE TABLE Pokemon (
  dex_num INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(32) NOT NULL,
  type_one INT NOT NULL,
  type_two INT NOT NULL,
  ability_id INT NOT NULL,
  FOREIGN KEY (type_one) REFERENCES Type(type_id),
  FOREIGN KEY (type_two) REFERENCES Type(type_id),
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
