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
            if (i == 0 || i == ny - 1 || j == 0 || j == nx - 1)
            {
                outimageR[i][j] = 255.0;
                outimageG[i][j] = 255.0;
                outimageB[i][j] = 255.0;
            }
            else
            {
                float arrR[9];
                arrR[0] = inputimageR[i - 1][j - 1];
                arrR[1] = inputimageR[i - 1][j];
                arrR[2] = inputimageR[i - 1][j + 1];
                arrR[3] = inputimageR[i][j - 1];
                arrR[4] = inputimageR[i][j];
                arrR[5] = inputimageR[i][j + 1];
                arrR[6] = inputimageR[i + 1][j - 1];
                arrR[7] = inputimageR[i + 1][j];
                arrR[8] = inputimageR[i + 1][j + 1];

                float arrG[9];
                arrG[0] = inputimageG[i - 1][j - 1];
                arrG[1] = inputimageG[i - 1][j];
                arrG[2] = inputimageG[i - 1][j + 1];
                arrG[3] = inputimageG[i][j - 1];
                arrG[4] = inputimageG[i][j];
                arrG[5] = inputimageG[i][j + 1];
                arrG[6] = inputimageG[i + 1][j - 1];
                arrG[7] = inputimageG[i + 1][j];
                arrG[8] = inputimageG[i + 1][j + 1];

                float arrB[9]; 
                arrB[0] = inputimageB[i - 1][j - 1];
                arrB[1] = inputimageB[i - 1][j];
                arrB[2] = inputimageB[i - 1][j + 1];
                arrB[3] = inputimageB[i][j - 1];
                arrB[4] = inputimageB[i][j];
                arrB[5] = inputimageB[i][j + 1];
                arrB[6] = inputimageB[i + 1][j - 1];
                arrB[7] = inputimageB[i + 1][j];
                arrB[8] = inputimageB[i + 1][j + 1];

                for (int k = 0; k < 9; ++k)
                {
                    for (int l = k + 1; l < 9; ++l)
                    {
                        if (arrR[k] > arrR[l])
                        {
                            float tmp = arrR[k];
                            arrR[k] = arrR[l];
                            arrR[l] = tmp;
                        }
                    }
                }

                for (int k = 0; k < 9; ++k)
                {
                    for (int l = k + 1; l < 9; ++l)
                    {
                        if (arrG[k] > arrG[l])
                        {
                            float tmp = arrG[k];
                            arrG[k] = arrG[l];
                            arrG[l] = tmp;
                        }
                    }
                }

                for (int k = 0; k < 9; ++k)
                {
                    for (int l = k + 1; l < 9; ++l)
                    {
                        if (arrB[k] > arrB[l])
                        {
                            float tmp = arrB[k];
                            arrB[k] = arrB[l];
                            arrB[l] = tmp;
                        }
                    }
                }

                printf("now is (i,j)=(%d,%d)\n",i,j);
                outimageR[i][j] = arrR[4];
                outimageG[i][j] = arrG[4];
                outimageB[i][j] = arrB[4];

                
            }
        }
    }
    /////////////////////////////////////////////////////////////////////////////

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
