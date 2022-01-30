#include "lib64.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    int i, j, k, l, nx, ny;
    BMPIMAGE im; // BMP画像の情報が入る変数
    float **inputimageR;
    float **outimageR;
    float **inputimageG;
    float **outimageG;
    float **inputimageB;
    float **outimageB;

    char filename[512];
    printf("Sample Program for Filtering \n");
    printf("Input Image Filename (BMP) = ");
    scanf("%s", filename, 500);
    getchar();

    // BMP画像を指定したファイルから読み込む
    im = Input_BMP(filename);
    if (im == 0)
    {
        printf("No such file as '%s'\n", filename);
        exit(0);
    }

    ny = im->height;
    nx = im->width; // 画像のサイズを読み込んだ画像情報から獲得

    inputimageR = f2d(ny, nx); // ny行 nx列のfloat型の２次元配列を確保
    outimageR = f2d(ny, nx);   // ny行 nx列のfloat型の２次元配列を確保
    inputimageG = f2d(ny, nx); // ny行 nx列のfloat型の２次元配列を確保
    outimageG = f2d(ny, nx);   // ny行 nx列のfloat型の２次元配列を確保
    inputimageB = f2d(ny, nx); // ny行 nx列のfloat型の２次元配列を確保
    outimageB = f2d(ny, nx);   // ny行 nx列のfloat型の２次元配列を確保

    //画像の画素値をfloat型の2次元配列にコピー（処理のため）
    for (i = 0; i < ny; i++)
        for (j = 0; j < nx; j++)
            inputimageR[i][j] = (float)im->red[i][j];
    for (i = 0; i < ny; i++)
        for (j = 0; j < nx; j++)
            inputimageG[i][j] = (float)im->green[i][j];
    for (i = 0; i < ny; i++)
        for (j = 0; j < nx; j++)
            inputimageB[i][j] = (float)im->blue[i][j];
    /////////////////////////////////////////////////////////////////////
    for (i = 0; i < ny; i++)
    {
        for (j = 0; j < nx; j++)
        {
            if (inputimageR[i][j] > 125.0)
            {
                outimageR[i][j] = 255.0;
                outimageG[i][j] = 255.0;
                outimageB[i][j] = 255.0;
            }
            else if (inputimageR[i][j] <= 125.0)
            {
                outimageR[i][j] = 0.0;
                outimageG[i][j] = 0.0;
                outimageB[i][j] = 0.0;
            }
            if (inputimageG[i][j] > 125.0)
            {
                outimageR[i][j] = 255.0;
                outimageG[i][j] = 255.0;
                outimageB[i][j] = 255.0;
            }
            else if (inputimageG[i][j] <= 125.0)
            {
                outimageR[i][j] = 0.0;
                outimageG[i][j] = 0.0;
                outimageB[i][j] = 0.0;
            }
            if (inputimageB[i][j] > 125.0)
            {
                outimageR[i][j] = 255.0;
                outimageG[i][j] = 255.0;
                outimageB[i][j] = 255.0;
            }
            else if (inputimageB[i][j] <= 125.0)
            {
                outimageR[i][j] = 0.0;
                outimageG[i][j] = 0.0;
                outimageB[i][j] = 0.0;
            }
        }
    } /////////////////////////////////////////////////////////////////////////////

    // float型の2次元配列からIMAGE構造体データにコピー（セーブするため）
    //コピーする前に，０以下の値は０に，２５５以上の値は２５５にしている．
    //同じ処理をＲＧＢそれぞれについて繰り返している
    for (i = 0; i < ny; i++)
    {
        for (j = 0; j < nx; j++)
        {
            if (outimageB[i][j] > 255.0)
                outimageB[i][j] = 255.0;
            if (outimageB[i][j] < 0.0)
                outimageB[i][j] = 0.0;
            im->blue[i][j] = (unsigned char)(outimageB[i][j]);
        }
    }

    for (i = 0; i < ny; i++)
    {
        for (j = 0; j < nx; j++)
        {
            if (outimageR[i][j] > 255.0)
                outimageR[i][j] = 255.0;
            if (outimageR[i][j] < 0.0)
                outimageR[i][j] = 0.0;
            im->red[i][j] = (unsigned char)(outimageR[i][j]);
        }
    }
    for (i = 0; i < ny; i++)
    {
        for (j = 0; j < nx; j++)
        {
            if (outimageG[i][j] > 255.0)
                outimageG[i][j] = 255.0;
            if (outimageG[i][j] < 0.0)
                outimageG[i][j] = 0.0;
            im->green[i][j] = (unsigned char)(outimageG[i][j]);
        }
    }
    // BMP画像としてファイルにセーブ
    printf("Output Image Filename (BMP)  = ");
    scanf("%s", filename, 500);
    getchar();
    Output_BMP(im, filename);
}
