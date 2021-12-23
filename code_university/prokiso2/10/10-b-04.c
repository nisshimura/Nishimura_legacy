#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    char *p,k[30],text[30], word[30];
    int i=0,j=0, textlen,wordlen,len;
    printf("Input a sentence : ");
    fgets(text, 30, stdin);
    textlen = strlen(text);
    text[textlen-1]='\0';

    printf("Input a word : ");
    fgets(word, 30, stdin);
    wordlen = strlen(word);
    word[wordlen - 1] = '\0';

    while (text[i]!='\0')
    {

        if (text[i]==word[0])
        {
            for (j=0;j<wordlen-1;j++)
            {
                if (text[i + j] != word[j])
                {
                    break;
                }
                else if (j==wordlen-2)
                {
                    printf("The word (%s) exists",word);
                    return 0;
                }
            }

        }
        i++;
    }
    printf("The word (%s) doesn't exists", word);
}

