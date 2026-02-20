#include<stdio.h>
#include <windows.h>
#include "battle.h"

int main(){
  SetConsoleOutputCP(65001);
  int new_game, game_continue = 1;
  Trainer player;
  Pokemon pokedex[10];
  
  printf("===============================\n");
  printf("     KnockOn Pokemon Game\n\n");
  printf("     press enter to start\n");
  printf("===============================");
  printf("===============================\n");
  printf("     1. 새로하기   2. 이어하기\n>> ");

  scanf("%d", &new_game);
  if(new_game == 1){
    loadPokedex(pokedex);
    initTrainer(&player);

    printf("===============================\n어느 포켓몬을 선택하시겠습니까?\n");
    printf("    1. 파이리 2. 이상해씨 3. 꼬부기\n>> ");

    int choice;
    scanf("%d", &choice);

    addPokemonToParty(&player, &pokedex[choice-1]);
  } else if (new_game == 2) {
    loadPokedex(pokedex); // 도감 정보는 공통으로 필요하니 로드
    loadGame(&player);    // 세이브 파일 읽기
  }

  while(game_continue){
    printf("===============================\n");
    printf("모험을 진행하시겠습니까?\n1. 네 2. 저장 3. 상점 4. 포켓몬센터 5. 포켓몬 도감\n>> ");
    int menu;
    scanf("%d", &menu);

    switch (menu) {
        case 1:
            // ⚔️ 전투 로직 (battle.c의 함수 호출 예정)
            printf("야생 포켓몬을 탐색합니다...\n");
            startBattle(&player, pokedex); 
            break;
        case 2:
            // 💾 저장 로직
            printf("게임을 저장합니다.\n");
            saveGame(&player);
            break;
        case 3:
            // 🏪 상점 로직
            printf("상점에 입장합니다.\n");
            break;
        case 4:
            // ❤️ 포켓몬센터 로직
            printf("포켓몬을 회복시킵니다.\n");
            break;
        case 5:
            // 📚 도감 로직 (아까 만든 printPokedex 호출)
            printPokedex(pokedex);
            break;
        default:
            printf("잘못된 입력입니다.\n");
            break;
    }
    if(!player.numPokemon){
      printf("싸울 포켓몬이 없습니다!\nGame Over...");
      game_continue = 0;
    }
  }
  return 0;
}