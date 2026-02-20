#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "pokemon.h"


void loadPokedex(Pokemon *pokedex){
  FILE *fp = fopen("pokemon.txt", "r");
  if (!fp){
    printf("파일 열기 실패! pokemon.txt가 있는지 확인해봐\n");
    return;
  }
  for (int i = 0; i < 10; i++){
    fscanf(fp, "%s %s %d %d",
      pokedex[i].name,
      pokedex[i].type,
      &pokedex[i].maxHp,
      &pokedex[i].attack);
    pokedex[i].currentHp = pokedex[i].maxHp;
    strcpy(pokedex[i].nickname, "야생");
  }
  fclose(fp);
  printf("도감 로딩 완료!\n");
}

void printPokedex(Pokemon *p){
  for (int i = 0; i < 10; i++){
    printf("%s %s타입 체력: %d 공격력: %d\n", p->name, p->type, p->maxHp, p->attack);
  }
}
