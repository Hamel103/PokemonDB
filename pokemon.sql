# INITIALIZING TABLES

DROP TABLE PokemonMoves;
DROP TABLE PokemonAbilities;

DROP TABLE Pokemon;
DROP TABLE Moves;
DROP TABLE Abilities;


CREATE TABLE Pokemon (
  pokemon_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  pokemon_name VARCHAR(32) NOT NULL,
  pokemon_typeone INT NOT NULL,
  pokemon_typetwo INT
);

CREATE TABLE Moves (
  moves_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  moves_name VARCHAR(32) NOT NULL,
  moves_type VARCHAR(32) NOT NULL,
  moves_uses VARCHAR(32),
  moves_damage INT,
  moves_accuracy INT
);

CREATE TABLE PokemonMoves (
  pokemon_id INT NOT NULL,
  moves_id INT NOT NULL,
  FOREIGN KEY (pokemon_id) REFERENCES Pokemon(pokemon_id),
  FOREIGN KEY (moves_id) REFERENCES Moves(moves_id)
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
  FOREIGN KEY (pokemon_id) REFERENCES Pokemon(pokemon_id)
  FOREIGN KEY (abilities_id) REFERENCES Abilities(abilities_id)
  ON UPDATE NO ACTION
  ON DELETE CASCADE
);
