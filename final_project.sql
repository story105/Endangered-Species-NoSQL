CREATE TABLE final_project.Main(
PK int
organism_id int
species_id int
federal_status_id int
unit_id int
state_id int
);

CREATE TABLE final_project.Organism(
organism_id int
organism varchar(50)
);

CREATE TABLE final_project.Species(
species_id int
species varchar(50)
);

CREATE TABLE final_project.Federal_Status(
federal_status_id int
federal_status varchar(50)
);

CREATE TABLE final_project.Unit(
unit_id int
unit varchar(50)
);

CREATE TABLE final_project.USstate(
USstate_id int
USstate varchar(50)
);