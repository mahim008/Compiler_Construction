#include<stdio.h>
void check_vowel(char s)
{
    if(s=='a'|'A'|'e'|'E'|'i'|'I'|'o'|'O'|'u'|'U')
        printf("%c is vowel.",s);
    else
        printf("%c is consonant.",s);
}

main()
{
    char c;
    printf("Enter a character to check : ");
    scanf("%c",&c);
    check_vowel(c);
    return 0;
}
