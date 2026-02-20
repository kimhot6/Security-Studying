#ifndef POKEMON_H
#define POKEMON_H

typedef struct Pokemon{
    char name[20];
    char nickname[20];
    char type[10];  // 불, 물, 풀
    int attack;
    int maxHp;
    int currentHp;
} Pokemon;

typedef struct Trainer{
    char trainerName[20];
    Pokemon *party[6];  // 최대 6마리
    int numPokemon;
    int money;
    int potionCount;
    int ballCount;
} Trainer;

void loadPokedex(Pokemon *p);

void printPokedex(Pokemon *p);

#endif