-- INITIALIZING TABLES
DROP TABLE Pokemon;
DROP TABLE Pokedex;
DROP TABLE Abilities;
DROP TABLE Types;

CREATE TABLE Types (
  type_name VARCHAR(10) PRIMARY KEY,
  type_advantages VARCHAR(100),
  type_disadvantages VARCHAR(100)
);

CREATE TABLE Abilities (
  ability_name VARCHAR(32) PRIMARY KEY,
  ability_description VARCHAR(100)
);

CREATE TABLE Pokedex (
  dex_num INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(12) NOT NULL,
);

CREATE TABLE Pokemon (
  dex_num INT NOT NULL,
  name VARCHAR(12) NOT NULL,
  type_one VARCHAR(10) NOT NULL,
  type_two VARCHAR(10),
  ability_name VARCHAR(32) NOT NULL,
  FOREIGN KEY (dex_num) REFERENCES Pokemon(dex_num),
  FOREIGN KEY (name) REFERENCES Pokemon(name),
  FOREIGN KEY (type_one) REFERENCES Types(type_name),
  FOREIGN KEY (type_two) REFERENCES Types(type_name),
  FOREIGN KEY (ability_name) REFERENCES Abilities(ability_name)
  ON UPDATE NO ACTION
  ON DELETE CASCADE
);
