#ifndef TRAINER_H
#define TRAINER_H

#include "pokemon.h"

void initTrainer(Trainer *t);
void printTrainerStatue(Trainer *t);
void addPokemonToParty(Trainer *t, Pokemon *p);
void removePokemon(Trainer *player, int index);
void buyItem(Trainer *t);
void saveGame(Trainer *t);

#endif