#include<stdio.h>

void TOH(int n,char S,char A, char D){
    if (n == 1) {
        printf("Move disk 1 from %c to %c\n", S, D);
        return;
    }
        TOH(n-1,S,D,A);
        printf("Move disk %d from %c to %c\n", n, S, D);
        TOH(n-1,A,S,D);

}

int main(){
    int n;
    printf("enter the number of disks:");
    scanf("%d",&n);
    TOH(n,'A','B','C');
    
    return 0;
}