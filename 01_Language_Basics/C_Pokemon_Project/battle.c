#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "battle.h"

void startBattle(Trainer *player, Pokemon pokedex[]) {
    // 1. 야생 포켓몬 랜덤 출현 (0~9번 도감 중 하나)
    srand(time(NULL));
    int enemyIdx = rand() % 10;
    
    // 야생 포켓몬은 동적 할당(malloc) 안 하고 그냥 구조체 변수로 만듭니다. (일회용이니까)
    Pokemon wildPokemon = pokedex[enemyIdx];
    wildPokemon.attack += rand() % 21;
    wildPokemon.maxHp += rand() % 51;

    printf("\n앗! 야생의 %s(이)가 나타났다! (HP: %d, 공격력: %d)\n", 
           wildPokemon.name, wildPokemon.currentHp, wildPokemon.attack);

    // 내 첫 번째 포켓몬 꺼내기
    Pokemon *myPokemon = player->party[0];
    printf("가라! %s!\n\n", myPokemon->name);

    // 2. 턴제 전투 루프
    while (wildPokemon.currentHp > 0 && myPokemon->currentHp > 0) {
        printf("--- [나의 턴!] ---\n");
        printf("1. 공격  2. 도망치기\n>> ");
        int choice;
        scanf("%d", &choice);

        if (choice == 2) {
            printf("\n%s(은)는 무사히 도망쳤다!\n", player->trainerName);
            return; // 전투 함수 종료
        }

        // 내가 때림
        printf("\n%s의 공격! 야생의 %s에게 %d의 데미지!\n", myPokemon->name, wildPokemon.name, myPokemon->attack);
        wildPokemon.currentHp -= myPokemon->attack;

        if (wildPokemon.currentHp <= 0) {
            printf("야생의 %s(을)를 쓰러뜨렸다! 전투 승리!\n", wildPokemon.name);
            break;
        }

        // 적이 때림
        printf("야생 %s의 반격! %s에게 %d의 데미지!\n", wildPokemon.name, myPokemon->name, wildPokemon.attack);
        myPokemon->currentHp -= wildPokemon.attack;

        if (myPokemon->currentHp <= 0) {
            printf("\n%s(은)는 쓰러졌다... 눈앞이 깜깜해졌다.\n", myPokemon->name);
            removePokemon(player, 0);
            break;
        }

        printf("\n[현재 HP] %s: %d | 야생 %s: %d\n", myPokemon->name, myPokemon->currentHp, wildPokemon.name, wildPokemon.currentHp);
    }
}