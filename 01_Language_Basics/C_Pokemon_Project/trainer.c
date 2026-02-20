#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>
#include "trainer.h"

void initTrainer(Trainer *t){
  printf("트레이너의 이름은?: ");
  scanf("%s", t->trainerName);
  t->money = 10000;
  t->numPokemon = 0;
  t->potionCount = 0;
  t->ballCount = 0;

  for(int i=0; i<6; i++) t->party[i] = NULL;
}

void printTrainerStatus(Trainer *t) {
    printf("\n--- [%s]님의 상태 ---\n", t->trainerName);
    printf("보유 금액: %d원\n", t->money);
    printf("포켓몬 수: %d / 6\n", t->numPokemon);
    printf("--------------------\n");
}

void addPokemonToParty(Trainer *t, Pokemon *p){
  int n = t->numPokemon;
  t->party[n] = (Pokemon *)malloc(sizeof(Pokemon));
  *(t->party[n]) = *p;

  srand(time(NULL));
  t->party[n]->maxHp = p->maxHp + rand() % 51;
  t->party[n]->currentHp = t->party[n]->maxHp;
  t->party[n]->attack = p->attack + rand() % 21;

  printf("%s가 파티에 합류했다!!", t->party[n]->name);
  t->numPokemon++;
}

void removePokemon(Trainer *player, int index) {
    if (index < 0 || index >= player->numPokemon) return;

    // 1. 메모리 해제 (중요! 안 하면 메모리 누수 발생 - 해킹 타겟이 됨)
    free(player->party[index]);

    // 2. 앞으로 당기기
    for (int i = index; i < player->numPokemon - 1; i++) {
        player->party[i] = player->party[i + 1];
    }

    // 3. 마지막 칸 정리
    player->party[player->numPokemon - 1] = NULL;
    player->numPokemon--;
}


void buyItem(Trainer *t){

}

void saveGame(Trainer *t) {
    FILE *fp = fopen("save.dat", "wb"); // 바이너리 쓰기 모드
    if (fp == NULL) {
        printf("저장 실패!\n");
        return;
    }

    // 1. 트레이너 기본 정보 저장
    fwrite(t, sizeof(Trainer), 1, fp);

    // 2. 포켓몬은 포인터(주소)라 따로 저장해야 함! (해킹 포인트!)
    for (int i = 0; i < t->numPokemon; i++) {
        fwrite(t->party[i], sizeof(Pokemon), 1, fp);
    }

    fclose(fp);
    printf("성공적으로 저장되었습니다!\n");
}

void loadGame(Trainer *t) {
    FILE *fp = fopen("save.dat", "rb"); // 바이너리 읽기 모드
    if (fp == NULL) {
        printf("저장된 데이터가 없습니다!\n");
        return;
    }

    // 1. 트레이너 기본 정보 불러오기
    fread(t, sizeof(Trainer), 1, fp);

    // 2. 중요! 저장된 포인터(주소)는 쓰레기값이므로, 
    // 실제 포켓몬 데이터를 읽어올 새 집(malloc)을 지어줘야 합니다.
    for (int i = 0; i < t->numPokemon; i++) {
        // 새 메모리 할당
        t->party[i] = (Pokemon *)malloc(sizeof(Pokemon));
        // 파일에서 포켓몬 알맹이 읽어서 채우기
        fread(t->party[i], sizeof(Pokemon), 1, fp);
    }

    fclose(fp);
    printf("%s 트레이너의 데이터를 불러왔습니다!\n", t->trainerName);
}
