# INITIALIZING TABLES

DROP TABLE PokemonAbilities;

DROP TABLE Pokemon;
DROP TABLE Abilities;
DROP TABLE Type;

CREATE TABLE Type (
  type_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  type_name VARCHAR(32) NOT NULL
);

CREATE TABLE Pokemon (
  pokemon_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  pokemon_name VARCHAR(32) NOT NULL,
  pokemon_typeone INT NOT NULL,
  pokemon_typetwo INT,
  pokemon_ability INT,
  FOREIGN KEY (pokemon_typeone) REFERENCES Type(type_id),
  FOREIGN KEY (pokemon_typetwo) REFERENCES Type(type_id)
  FOREIGN KEY (pokemon_ability) REFERENCES Abilities(ability_id)
  ON UPDATE NO ACTION
  ON DELETE CASCADE
);

CREATE TABLE Abilities (
  abilities_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  abilities_name VARCHAR(32)
);

CREATE TABLE PokemonAbilities (
  pokemon_id INT NOT NULL,
  abilities_id INT NOT NULL,
  FOREIGN KEY (pokemon_id) REFERENCES Pokemon(pokemon_id),
  FOREIGN KEY (abilities_id) REFERENCES Abilities(abilities_id)
  ON UPDATE NO ACTION
  ON DELETE CASCADE
);
