/*----------------------------------------------------------------------

 Gray Image Library and BMP Image Library

  ---------------------------------------------------------------------- */

#include <stdio.h>
#include <math.h>
//#include <malloc.h>
#include <stdlib.h>
#include <string.h>

    /* The image header data structure      */
    struct header
{
  int ny, nx;             /* Rows and columns in the image */
	int oi, oj;             /* Origin */
};

/*      The IMAGE data structure        */
struct image {
		struct header *info;            /* Pointer to header */
		unsigned char **data;           /* Pixel values */
};

typedef struct image * IMAGE;

int    PBM_SE_ORIGIN_COL=0, PBM_SE_ORIGIN_ROW=0;

IMAGE Input_PBM (char *fn);
IMAGE Generate_PBM (char *fn, int height, int width);
IMAGE Output_PBM (IMAGE image, char *filename);
void get_num_pbm (FILE *f, char *b, int *bi, int *res);
void pbm_getln (FILE *f, char *b);
void pbm_param (char *s);
struct image  *newimage (int ny, int nx);
void freeimage (struct image  *z);
void sys_abort (int val, char *mess);
void CopyVarImage (IMAGE *a, IMAGE *b);
float ** f2d (int ny, int nx);


struct bmpimage {
  short infosize, bits;
  int offset, width, height, xreso, yreso;
  unsigned char **red, **green, **blue;
};

typedef struct bmpimage * BMPIMAGE;

BMPIMAGE Input_BMP(char *fn);
BMPIMAGE Generate_BMP(char *fn,int ny, int nx);
BMPIMAGE Output_BMP (BMPIMAGE image, char *filename);
struct bmpimage  *new_bmpimage (  short infosize, short bits, int offset, int width, int height, int xreso, int yreso);
void free_bmpimage (struct bmpimage  *z);
//void copy_bmpimage (BMP_IMAGE *a, BMP_IMAGE b);
//void CopyVarBmpImage (BMPIMAGE *a, BMPIMAGE *b);

int usedcolor(short bits, int color);
int read32(FILE * bmp,
            BMPIMAGE im,
           unsigned char *red, 
           unsigned char *green, 
           unsigned char *blue);
int read4(FILE * bmp,
            BMPIMAGE im,
           unsigned char *red, 
           unsigned char *green, 
           unsigned char *blue);

IMAGE Input_PBM (char *fn)
{
	int i,j,k,n,m,bi, b;
	unsigned char ucval;
	int val;
	int here;
	char buf1[256];
	FILE *f;
	IMAGE im;

	strcpy (buf1, fn);
	f = fopen (buf1, "r");
	if (f==NULL)
	{
	  printf ("Can't open the PBM file named '%s'\n", buf1);
	  return 0;
	}

	pbm_getln (f, buf1);
	if (buf1[0] == 'P')
	{
	  switch (buf1[1])
	  {
case '1':       k=1; break;
case '2':       k=2; break;
case '3':       k=3; break;
case '4':       k=4; break;
case '5':       k=5; break;
case '6':       k=6; break;
default:        printf ("Not a PBM/PGM/PPM file.\n");
		return 0;
	  }
	}
	bi = 2;

	get_num_pbm (f, buf1, &bi, &m);         /* Number of columns */
	get_num_pbm (f, buf1, &bi, &n);         /* Number of rows */
	if (k!=1 && k!=4) get_num_pbm (f, buf1, &bi, &b);      /* Max value */
	else b = 1;

	fprintf (stderr,"\nPBM file class %d size %d columns X %d rows Max=%d\n",
		k, m, n, b);
	
/* Binary file? Re-open as 'rb' */        
	if (k>3)
	{
	  here = ftell (f);
	  fclose (f);
	  f = fopen (fn, "rb");       
	  here++;
	  if (fseek(f, here, 0) != 0) 
	  {
	    printf ("Input_PBM: Synx error, file '%s'. Use ASCII PGM.\n",fn);
	    exit (3);
	  }
	}

/* Allocate the image */
	if (k==3 || k==6)       /* Colour */
	  sys_abort (0, "Colour image.");
	else 
	{
	  im = (IMAGE)newimage (n, m);
	  im->info->oi = PBM_SE_ORIGIN_ROW;
	  im->info->oj = PBM_SE_ORIGIN_COL;
	  PBM_SE_ORIGIN_ROW = 0;
	  PBM_SE_ORIGIN_COL = 0;
	  for (i=0; i<n; i++)
	    for (j=0; j<m; j++)
	      if (k<3)
	      {
		fscanf (f, "%d", &val);
		im->data[i][j] = (unsigned char)val;
	      } else {
		fscanf (f, "%c", &ucval);
		im->data[i][j] = ucval;
	      }
	}
	return im;
}

IMAGE Generate_PBM (char *fn, int height, int width)
{
	int i,j,k,n,m,bi, b;
	unsigned char ucval;
	int val;
	int here;
	char buf1[256];
	FILE *f;
	IMAGE im;

	strcpy (buf1, fn);
	f = fopen (buf1, "r");
	if (f==NULL)
	{
	  printf ("Can't open the PBM file named '%s'\n", buf1);
	  return 0;
	}

	pbm_getln (f, buf1);
	if (buf1[0] == 'P')
	{
	  switch (buf1[1])
	  {
case '1':       k=1; break;
case '2':       k=2; break;
case '3':       k=3; break;
case '4':       k=4; break;
case '5':       k=5; break;
case '6':       k=6; break;
default:        printf ("Not a PBM/PGM/PPM file.\n");
		return 0;
	  }
	}
	bi = 2;

	get_num_pbm (f, buf1, &bi, &m);         /* Number of columns */
	get_num_pbm (f, buf1, &bi, &n);         /* Number of rows */
	if (k!=1 && k!=4) get_num_pbm (f, buf1, &bi, &b);      /* Max value */
	else b = 1;

	fprintf (stderr,"\nPBM file class %d size %d columns X %d rows Max=%d\n",
		k, m, n, b);
	
/* Binary file? Re-open as 'rb' */        
	if (k>3)
	{
	  here = ftell (f);
	  fclose (f);
	  f = fopen (fn, "rb");       
	  here++;
	  if (fseek(f, here, 0) != 0) 
	  {
	    printf ("Input_PBM: Synx error, file '%s'. Use ASCII PGM.\n",fn);
	    exit (3);
	  }
	}

/* Allocate the image */
	if (k==3 || k==6)       /* Colour */
	  sys_abort (0, "Colour image.");
	else 
	{
	  im = (IMAGE)newimage (height, width);
	  im->info->oi = PBM_SE_ORIGIN_ROW;
	  im->info->oj = PBM_SE_ORIGIN_COL;
	  PBM_SE_ORIGIN_ROW = 0;
	  PBM_SE_ORIGIN_COL = 0;
	  /****
	  for (i=0; i<n; i++)
	    for (j=0; j<m; j++)
	      if (k<3)
	      {
		fscanf (f, "%d", &val);
		im->data[i][j] = (unsigned char)val;
	      } else {
		fscanf (f, "%c", &ucval);
		im->data[i][j] = ucval;
	      }
	  ***/
	}
	return im;
}

IMAGE Output_PBM (IMAGE image, char *filename)
{
	FILE *f;
	int i,j,k, perline;
	char buf1[64];

	strcpy (buf1, filename);
	if (image->info->nx > 20) perline = 20;
	 else perline = image->info->nx-1;
	f = fopen (buf1, "w");
	if (f == 0) sys_abort (0, "Can't open output file.");

	fprintf (f,"P2\n#origin %d %d\n",image->info->oj,image->info->oi);
	fprintf (f, "%d %d %d\n", image->info->nx, image->info->ny, 255);
	k = 0;
	for (i=0; i<image->info->ny; i++)
	  for (j=0; j<image->info->nx; j++)
	  {
		fprintf (f, "%d ", image->data[i][j]);
		k++;
		if (k > perline)
		{
		  fprintf (f, "\n");
		  k = 0;
		}
	  }
	fprintf (f, "\n");
	fclose (f);
	return image;
}

void get_num_pbm (FILE *f, char *b, int *bi, int *res)
{
	int i;
	char str[80];

	while (b[*bi]==' ' || b[*bi]=='\t' || b[*bi]=='\n')
	{
	  if (b[*bi] == '\n') 
	  {
	    pbm_getln (f, b);
	    *bi = 0;
	  } else
	  *bi += 1;
	}

	i = 0;
	while (b[*bi]>='0' && b[*bi]<='9')
	  str[i++] = b[(*bi)++];
	str[i] = '\0';
	sscanf (str, "%d", res);
}


void pbm_getln (FILE *f, char *b)
{
	int i;
	char c;

/* Read the next significant line (non-comment) from f into buffer b */
	do
	{

/* Read the next line */
	  i = 0;
	  do
	  {
	    fscanf (f, "%c", &c);
	    b[i++] = c;
	    if (c == '\n') b[i] = '\0';
	  } while (c != '\n');

/* If a comment, look for a special parameter */
	  if (b[0] == '#') pbm_param (b);

	} while (b[0]=='\n' || b[0] == '#');
}

/*      Look for a parameter hidden in a comment        */
void pbm_param (char *s)
{
	int i,j;
	char key[24];

/* Extract the key word */
	for (i=0; i<23; i++)
	{
	  j = i;
	  if (s[i+1] == ' ' || s[i+1] == '\n') break;
	  key[i] = s[i+1];
	}
	key[j] = '\0';

/* Convert to lower case */
	for (i=0; i<j; i++)
	  if ( (key[i]>='A') && (key[i]<='Z') )
		key[i] = (char) ( (int)key[i] - (int)'A' + (int)'a' );

/* Which key word is it? */
	if (strcmp(key, "origin") == 0)         /* ORIGIN key word */
	{
	  sscanf (&(s[j+1]), "%d %d", 
	    &PBM_SE_ORIGIN_COL, &PBM_SE_ORIGIN_ROW);
	  return;
	}
}

struct image  *newimage (int ny, int nx)
{
	struct image  *x;                /* New image */
//	unsigned char *ptr;             /* new pixel array */
	int i;

	if (ny < 0 || nx < 0) {
		printf ("Error: Bad image size (%d,%d)\n", ny, nx);
		return 0;
	}

/*      Allocate the image structure    */
	x = (struct image  *) malloc( sizeof (struct image) );
	if (!x) {
		printf ("Out of storage in NEWIMAGE.\n");
		return 0;
	}

/*      Allocate and initialize the header      */

	x->info = (struct header *)malloc( sizeof(struct header) );
	if (!(x->info)) {
		printf ("Out of storage in NEWIMAGE.\n");
		return 0;
	}
	x->info->ny = ny;       x->info->nx = nx;
	x->info->oi = x->info->oj = 0;

/*      Allocate the pixel array        */

	x->data = (unsigned char **)malloc(sizeof(unsigned char *)*ny); 

/* Pointers to rows */
	if (!(x->data)) {
		printf ("Out of storage in NEWIMAGE.\n");
		return 0;
	}
	
	for (i=0; i<ny; i++) 
	{
	  x->data[i] = (unsigned char *)malloc(nx*sizeof(unsigned char));
	  if (x->data[i]==0)
	  {
		printf ("Out of storage. Newimage - row %d\n", i);
		exit(1);
	  }
	}
	return x;
}

void freeimage (struct image  *z)
{
/*      Free the storage associated with the image Z    */
	int i;

	if (z != 0) 
	{
	  for (i=0; i<z->info->ny; i++)
	      free (z->data[i]);
	   free (z->info);
	   free (z->data);
	   free (z);
	}
}

void sys_abort (int val, char *mess)
{
	fprintf (stderr, "**** System library ABORT %d: %s ****\n", 
			val, mess);
	exit (2);
}

void copy (IMAGE *a, IMAGE b)
{
	CopyVarImage (a, &b);
}

void CopyVarImage (IMAGE *a, IMAGE *b)
{
	int i,j;

	if (a == b) return;
	if (*a) freeimage (*a);
	*a = newimage ((*b)->info->ny, (*b)->info->nx);
	if (*a == 0) sys_abort (0, "No more storage.\n");

	for (i=0; i<(*b)->info->ny; i++)
	  for (j=0; j< (*b)->info->nx; j++)
	    (*a)->data[i][j] = (*b)->data[i][j];
	(*a)->info->oi = (*b)->info->oi;
	(*a)->info->oj = (*b)->info->oj;
}


float ** f2d (int ny, int nx)
{
	float **x, *y;
	int i;

	x = (float **)calloc ( ny, sizeof (float *) );
	if (x == 0)
	{
	  fprintf (stderr, "Out of storage: F2D.\n");
	  exit (1);
	}

	for (i=0; i<ny; i++)
	{  
	  x[i] = (float *) calloc ( nx, sizeof (float)  );
	  if (x[i] == 0)
	  {
	    fprintf (stderr, "Out of storage: F2D %d.\n", i);
	    exit (1);
	  }
	}
	return x;
}


BMPIMAGE Input_BMP (char *bmpfile)
{
  BMPIMAGE im;
  short infosize, bits;
  int used = 0, color = 0, offset, width, height, xreso, yreso;
  unsigned char red[256], green[256], blue[256];
  FILE *fp1;

  if ((fp1 = fopen(bmpfile, "rb")) == NULL) {
    fprintf(stderr, "Cannot open file : %s\n", bmpfile);
    exit(1);
  }
  // �w�b�_��� BITMAPFILEHEADER 
  fileheader(fp1, &offset);
  // �w�b�_��� BITMAPINFOHEADER 
  infoheader(fp1, &infosize, &width, &height, &xreso, &yreso, &bits, &color);
  color = usedcolor(bits, color);

  // OS/2 Bitmap 
  if (infosize == 12) {
    if (bits == 1 || bits == 4 || bits == 8) {
      used = rgbtriple(fp1, color, red, green, blue);
    }
    printf("[OS/2 bitmap] --- %d bit %ld color\n", bits, used);
  }
  // Windows Bitmap 
  else if (infosize == 40) {
    if (bits == 1 || bits == 4 || bits == 8) {
      used = rgbquad(fp1, color, red, green, blue);
    }
    printf("[Windows bitmap] --- %d bit %ld color\n", bits, used);
  } 
  else if (infosize == 108) {
    printf("[other bitmap]\n");
  }
  else {
    fprintf(stderr, "BITMAP INFOHEADER error\n");
  }

  im = (BMPIMAGE)new_bmpimage (infosize, bits, offset, width, height, xreso, yreso);

  if (bits == 32 || bits == 24 || bits == 8) {
    printf("%d [pixels]\n", read32(fp1, im,red, green, blue));
  }
  else if (bits == 4) {
    printf("%ld [pixels]\n", read4(fp1, im,red, green, blue));
  }
  else {
    fprintf(stderr, "%d bit �F�ɂ͑Ή����Ă��܂���\n", bits);
    exit(1);
  }

  fclose(fp1);

  return im;

}

BMPIMAGE Generate_BMP (char *bmpfile, int ny, int nx)
{
  BMPIMAGE im;
  short infosize, bits;
  int used = 0, color = 0, offset, width, height, xreso, yreso;
  unsigned char red[256], green[256], blue[256];
  FILE *fp1;

  if ((fp1 = fopen(bmpfile, "rb")) == NULL) {
    fprintf(stderr, "Cannot open file : %s\n", bmpfile);
    exit(1);
  }
  // �w�b�_��� BITMAPFILEHEADER 
  fileheader(fp1, &offset);
  // �w�b�_��� BITMAPINFOHEADER 
  infoheader(fp1, &infosize, &width, &height, &xreso, &yreso, &bits, &color);
  color = usedcolor(bits, color);

  // OS/2 Bitmap 
  if (infosize == 12) {
    if (bits == 1 || bits == 4 || bits == 8) {
      used = rgbtriple(fp1, color, red, green, blue);
    }
    printf("[OS/2 bitmap] --- %d bit %ld color\n", bits, used);
  }
  // Windows Bitmap 
  else if (infosize == 40) {
    if (bits == 1 || bits == 4 || bits == 8) {
      used = rgbquad(fp1, color, red, green, blue);
    }
    printf("[Windows bitmap] --- %d bit %ld color\n", bits, used);
  } 
  else if (infosize == 108) {
    printf("[other bitmap]\n");
  }
  else {
    fprintf(stderr, "BITMAP INFOHEADER error\n");
  }

  im = (BMPIMAGE)new_bmpimage (infosize, bits, offset, nx, ny, xreso, yreso);

/****
  if (bits == 32 || bits == 24 || bits == 8) {
    printf("%d [pixels]\n", read32(fp1, im,red, green, blue));
  }
  else if (bits == 4) {
    printf("%ld [pixels]\n", read4(fp1, im,red, green, blue));
  }
  else {
    fprintf(stderr, "%d bit �F�ɂ͑Ή����Ă��܂���\n", bits);
    exit(1);
  }
  ****/

  fclose(fp1);

  return im;

}

BMPIMAGE Output_BMP (BMPIMAGE im, char *filename)
{

  FILE *fp1;
  int line, size;
  int i, j ;
  int var_int,position, count = 0;
  short var_short;

  if ((fp1 = fopen(filename, "wb")) == NULL) {
    fprintf(stderr, "Cannot open file : %s\n", filename);
    exit(1);
  }

  im->bits = 24;
  im->offset = 54;
  // �摜�T�C�Y (1���C����4Byte(int)���E�ɂ��킹��) 
  line = (im->width * im->bits) / 8;
  if ((line % 4) != 0) {
    line = ((line / 4) + 1) * 4;
  }
  size = line * im->height;

  //BITMAPFILEHEADER 
  write_fileheader(fp1, size, im->offset);


  //BITMAPINFOHEADER 

  printf("[BITMAPINFOHEADER]\n");
  // ���w�b�_�̃T�C�Y biSize (Windows BMP �� 40 ����ɋ���) 
  var_int = 40;
  fwrite(&var_int, sizeof(int), 1, fp1);
  // �摜�̕� biWidth 
  var_int = im->width;
  printf("  Width              = %ld [pixels]\n", var_int);
  fwrite(&var_int, sizeof(int), 1, fp1);
  // �摜�̍��� biHeight 
  // (�����Ȃ�΍�������E��, �}�C�i�X�Ȃ�΍��ォ��E��) 
  var_int = im->height;
  printf("  Height             = %ld [pixels]\n", var_int);
  fwrite(&var_int, sizeof(int), 1, fp1);
  // �v���[���� biPlanes (�K�� 1) 
  var_short = 1;
  printf("  Planes             = %hd\n", var_short);
  fwrite(&var_short, sizeof(short), 1, fp1);
  // 1�s�N�Z���̃f�[�^�� biBitCount (1, 4, 8, 24, 32) 
  var_short = im->bits;
  printf("  Bits Per Pixel     = %hd [bits]\n", var_short);
  fwrite(&var_short, sizeof(short), 1, fp1);

  // ���k biCompression (�����k�Ȃ�� 0) 
  var_int = 0;
  printf("  Compression        = %ld\n", var_int);
  fwrite(&var_int, sizeof(int), 1, fp1);
  // �摜�̃T�C�Y biSizeImage 
  var_int = size;
  printf("  Bitmap Data Size   = %ld [Bytes]\n", var_int);
  fwrite(&var_int, sizeof(int), 1, fp1);
  // �������𑜓x pixel/m biXPelPerMeter 
  var_int = im->xreso;
  printf("  HResolution        = %ld [pixel/m]\n", var_int);
  fwrite(&var_int, sizeof(int), 1, fp1);
  // �c�����𑜓x pixel/m biYPelPerMeter 
  var_int = im->yreso;
  printf("  VResolution        = %ld [pixel/m]\n", var_int);
  fwrite(&var_int, sizeof(int), 1, fp1);
  // �p���b�g�� biClrUsed 
//  var_int = 1 << im->bits;
  var_int = 0;
  printf("  Colors             = %ld [colors]\n", var_int);
  fwrite(&var_int, sizeof(int), 1, fp1);
  // �p���b�g���̏d�v�ȐF  biClrImportant 
  var_int = 0;
  printf("  Important Colors   = %ld\n", var_int);
  fwrite(&var_int, sizeof(int), 1, fp1);

  // �t�@�C���w�b�_(14 Byte) + ���w�b�_�T�C�Y(40 Byte) 
  if ((count = ftell(fp1)) != 54) {
    fprintf(stderr, "BITMAPINFOHEADER write error : %ld\n", count);
    exit(1);
  }

  count = 0;

  for (i = 0; i < im->height; i++) {
    // �s�̐擪�ʒu 
    position = im->offset + line * (im->height - (i + 1));
    fseek(fp1, position, SEEK_SET);

    // �l�̏������� 
    for (j = 0; j < im->width; j++) {
	fputc(im->blue[i][j], fp1);
	fputc(im->green[i][j], fp1);
	fputc(im->red[i][j], fp1);
        count++;
    }
  }
  printf("%d [pixels]\n", count);
  fclose(fp1);
  return im;

}

/*---------------------------------*/
/* �t�@�C���w�b�_ BITMAPFILEHEADER */
/*---------------------------------*/

int write_fileheader(FILE * fp,
               int size, int offset)
{
  int count, filesize;
  short reserved = 0;
  char s[2];

  rewind(fp);

  // ���ʕ��� BM 
  s[0] = 'B';
  s[1] = 'M';
  fwrite(s, sizeof(char), 2, fp);

  printf("[BITMAPFILEHEADER]\n");
  // �t�@�C���T�C�Y bfSize 
  filesize = size + offset;
  printf("  File Size          = %ld[Bytes]\n", filesize);
  fwrite(&filesize, sizeof(int), 1, fp);
  // �\��G���A bfReserved1 
  fwrite(&reserved, sizeof(short), 1, fp);
  // �\��G���A bfReserved2 
  fwrite(&reserved, sizeof(short), 1, fp);
  // �f�[�^���܂ł̃I�t�Z�b�g bfOffBits 
  printf("  Bitmap Data Offset = %ld [Bytes]\n", offset);
  fwrite(&offset, sizeof(int), 1, fp);

  // �t�@�C���w�b�_�T�C�Y 14 Byte 
  if ((count = ftell(fp)) != 14) {
    fprintf(stderr, "BITMAPFILEHEADER write error : %ld\n", count);
    exit(1);
  }

  return count;
}


struct bmpimage  *new_bmpimage (  short infosize, short bits, 
  int offset, int width, int height, int xreso, int yreso)
{
	struct bmpimage  *x;                /* New image */
	int i;



	if (height < 0 || width < 0) {
		printf ("Error: Bad image size (%d,%d)\n", height, width);
		return 0;
	}

/*      Allocate the image structure    */
	x = (struct bmpimage  *) malloc( sizeof (struct bmpimage) );
	if (!x) {
		printf ("Out of storage in NEWIMAGE.\n");
		return 0;
	}

	x->infosize = infosize;
  	x->bits = bits ;
  	x->offset = offset ;
  	x->width = width ;
  	x->height = height;
  	x->xreso = xreso;
  	x->yreso = yreso;


/*      Allocate the pixel array        */

	x->red = (unsigned char **)malloc(sizeof(unsigned char *)*height); 
	x->green = (unsigned char **)malloc(sizeof(unsigned char *)*height); 
	x->blue = (unsigned char **)malloc(sizeof(unsigned char *)*height); 

/* Pointers to rows */
	if (!(x->red)) {
		printf ("Out of storage in NEWIMAGE.\n");
		return 0;
	}
	
	for (i=0; i<height; i++) 
	{
	  x->red[i] = (unsigned char *)malloc(width*sizeof(unsigned char));
	  if (x->red[i]==0)
	  {
		printf ("Out of storage. Newimage - row %d\n", i);
		exit(1);
	  }
	}

/* Pointers to rows */
	if (!(x->green)) {
		printf ("Out of storage in NEWIMAGE.\n");
		return 0;
	}
	
	for (i=0; i<height; i++) 
	{
	  x->green[i] = (unsigned char *)malloc(width*sizeof(unsigned char));
	  if (x->green[i]==0)
	  {
		printf ("Out of storage. Newimage - row %d\n", i);
		exit(1);
	  }
	}

/* Pointers to rows */
	if (!(x->blue)) {
		printf ("Out of storage in NEWIMAGE.\n");
		return 0;
	}
	
	for (i=0; i<height; i++) 
	{
	  x->blue[i] = (unsigned char *)malloc(width*sizeof(unsigned char));
	  if (x->blue[i]==0)
	  {
		printf ("Out of storage. Newimage - row %d\n", i);
		exit(1);
	  }
	}

	return x;
}

void free_bmpimage (struct bmpimage  *z)
{
/*      Free the storage associated with the image Z    */
	int i;

	if (z != 0) 
	{
	  for (i=0; i<z->height; i++){
	      free (z->red[i]);
	      free (z->green[i]);
	      free (z->blue[i]);
 	  }
	   free (z->red);
	   free (z->green);
	   free (z->blue);

	   free (z);
	}
}

/*
void copy_bmpimage (BMPIMAGE *a, BMPIMAGE b)
{
	CopyVarImage (a, &b);
}

void CopyVarBmpImage (BMPIMAGE *a, BMPIMAGE *b)
{
	int i,j;

	if (a == b) return;
	if (*a) free_bmpimage (*a);
	*a = new_bmpimage ((*b)->info->ny, (*b)->info->nx);
	if (*a == 0) sys_abort (0, "No more storage.\n");

	for (i=0; i<(*b)->info->ny; i++)
	  for (j=0; j< (*b)->info->nx; j++)
	    (*a)->data[i][j] = (*b)->data[i][j];
	(*a)->info->oi = (*b)->info->oi;
	(*a)->info->oj = (*b)->info->oj;
}
*/


/*----------------------------*/
/* �t�@�C���w�b�_�� (14 Byte) */
/*----------------------------*/
int fileheader(FILE * fp, int *offset)
{
  int count = 0;
  int var_int;
  short var_short;
  char s[10];

  // BITMAP �F������ "BM"
  if (fread(s, 2, 1, fp) == 1) {
    if (memcmp(s, "BM", 2) == 0) {
      printf("[BM] BITMAP file\n");
    } 
    else {
      fprintf(stderr, "%s : Not a BITMAP file\n", s);
      exit(1);
    }
    count += 2;
  }
  printf("  [BITMAPFILEHEADER]\n");
  // �t�@�C���T�C�Y
  if (fread(&var_int, 4, 1, fp) == 1) {
    printf("  Size          : %ld [Byte]\n", var_int);
    count += 4;
  }
  // �\��̈� 0
  if (fread(&var_short, 2, 1, fp) == 1) {
    count += 2;
  }
  // �\��̈� 0
  if (fread(&var_short, 2, 1, fp) == 1) {
    count += 2;
  }
  // �t�@�C���̐擪����摜�f�[�^�܂ł̈ʒu
  if (fread(&var_int, 4, 1, fp) == 1) {
    printf("  OffBits       : %ld [Byte]\n", var_int);
    *offset = var_int;
    count += 4;
  }
  return count;
}

/*------------------------------------------------------------------*/
/* ���w�b�_�� (12 Byte -> OS/2 Bitmap, 40 Byte -> Windows Bitmap) */
/*------------------------------------------------------------------*/
int infoheader(FILE * fp,
               short *infosize,
               int *width, int *height,
               int *x_coodinate, int *y_coodinate,
               short *BitCount, 
               int *ClrUsed)
{
  int count = 0;
  int var_int, compress = 0;
  short var_short;

  // BITMAPINFOHEADER �̃T�C�Y
  if (fread(&var_int, 4, 1, fp) == 1) {
    count += 4;
    *infosize = var_int;
  }

  printf("  [BITMAPINFOHEADER]\n");
  // OS/2 Bitmap
  if (*infosize == 12) {
    // �摜�f�[�^�̕�
    if (fread(&var_short, 2, 1, fp) == 1) {
      printf("  Width         : %d [pixel]\n", var_short);
      *width = var_short;
      count += 2;
    }
    // �摜�f�[�^�̍��� 
    if (fread(&var_short, 2, 1, fp) == 1) {
      printf("  Height        : %d [pixel]\n", var_short);
      *height = var_short;
      count += 2;
    }
    // �v���[���� (1�̂�) 
    if (fread(&var_short, 2, 1, fp) == 1) {
      count += 2;
    }
    // 1��f������̃r�b�g�� (1, 4, 8, 24, 32) 
    if (fread(&var_short, 2, 1, fp) == 1) {
      printf("  BitCount      : %d [bit]\n", var_short);
      *BitCount = var_short;
      count += 2;
    }
  }
  // Windows BMP 
  else if (*infosize == 40) {
    // �摜�f�[�^�̕� 
    if (fread(&var_int, 4, 1, fp) == 1) {
      printf("  Width         : %ld [pixel]\n", var_int);
      *width = var_int;
      count += 4;
    }
    // �摜�f�[�^�̍���
    if (fread(&var_int, 4, 1, fp) == 1) {
      printf("  Height        : %ld [pixel]\n", var_int);
      *height = var_int;
      count += 4;
    }
    // �v���[���� (1�̂�) 
    if (fread(&var_short, 2, 1, fp) == 1) {
      count += 2;
    }
    // 1��f������̃r�b�g�� (1, 4, 8, 24, 32) 
    if (fread(&var_short, 2, 1, fp) == 1) {
      printf("  BitCount      : %d [bit]\n", var_short);
      *BitCount = var_short;
      count += 2;
    }
    // ���k����  0 : �����k 
    //           1 : BI_RLE8 8bit RunLength ���k 
    //           2 : BI_RLE4 4bit RunLength ���k 
    if (fread(&var_int, 4, 1, fp) == 1) {
      printf("  Compression   : %ld\n", var_int);
      compress = var_int;
      count += 4;
    }
    // �摜�f�[�^�̃T�C�Y 
    if (fread(&var_int, 4, 1, fp) == 1) {
      printf("  SizeImage     : %ld [Byte]\n", var_int);
      count += 4;
    }
    // �������𑜓x (Pixel/meter) 
    if (fread(&var_int, 4, 1, fp) == 1) {
      printf("  XPelsPerMeter : %ld [pixel/m]\n", var_int);
      *x_coodinate = var_int;
      count += 4;
    }
    // �c�����𑜓x (Pixel/meter) 
    if (fread(&var_int, 4, 1, fp) == 1) {
      printf("  YPelsPerMeter : %ld [pixel/m]\n", var_int);
      *y_coodinate = var_int;
      count += 4;
    }
    // �g�p�F�� 
    if (fread(&var_int, 4, 1, fp) == 1) {
      printf("  ClrUsed       : %ld [color]\n", var_int);
      *ClrUsed = var_int;
      count += 4;
    }
    // �d�v�ȐF�̐� 0�̏ꍇ���ׂĂ̐F 
    if (fread(&var_int, 4, 1, fp) == 1) {
      count += 4;
    }
  } 
  else {
    fprintf(stderr, "Bitmap Info Header error\n");
  }

  if (compress != 0) {
    fprintf(stderr, "���k�r�b�g�}�b�v�ɂ͑Ή����Ă��܂���\n");
    exit(1);
  }
  if (*BitCount == 4 || *BitCount == 8 || *BitCount == 24 || *BitCount == 32) {
    ;
  } 
  else {
    fprintf(stderr, "%d �r�b�g�F�ɂ͑Ή����Ă��܂���\n", *BitCount);
    exit(1);
  }
  return count;
}

/*------------------*/
/* �g�p�F���J�E���g */
/*------------------*/
int usedcolor(short bits, int color)
{
  if (color != 0) {
    return color;
  } 
  else {
    return 1 << bits;
  }
}

/*-------------*/
/* OS/2 bitmap */
/*-------------*/
int rgbtriple(FILE * fp,
              int used,
              unsigned char *red,
              unsigned char *green, 
              unsigned char *blue)
{
  int i;
  int count = 0;

  // �r�b�g�̕��т� B G R 
  for (i = 0; i < used; i++) {
    blue[i] = fgetc(fp);
    green[i] = fgetc(fp);
    red[i] = fgetc(fp);
    count++;
  }

  return count;
}

/*----------------*/
/* Windows bitmap */
/*----------------*/
int rgbquad(FILE * fp,
            int used,
            unsigned char *red, 
            unsigned char *green, 
            unsigned char *blue)
{
  int i;
  int receive, count = 0;

  // �r�b�g�̕��т� B G R �\�� 
  for (i = 0; i < used; i++) {
    blue[i] = fgetc(fp);
    green[i] = fgetc(fp);
    red[i] = fgetc(fp);
    receive = fgetc(fp);
    count++;
  }
  return count;
}

/*----------------*/
/* �e�L�X�g�_���v */
/*----------------*/
int read32(FILE * bmp,
            BMPIMAGE im,
           unsigned char *red, 
           unsigned char *green, 
           unsigned char *blue)
{
  int alpha;
  int i, j, line, position, count = 0;

  // 4byte ���E�ɂ��킹�� 
  line = (im->width * im->bits) / 8;
  if ((line % 4) != 0) {
    line = ((line / 4) + 1) * 4;
  }

  for (i = 0; i < im->height; i++) {
    // �s�̐擪�ʒu 
    position = im->offset + line * (im->height - (i + 1));
    fseek(bmp, position, SEEK_SET);

    // �l�̓ǂݍ��� 
    for (j = 0; j < im->width; j++) {
      // 32 bit �F 
      if (im->bits == 32) {
        im->blue[i][j] = fgetc(bmp);
        im->green[i][j] = fgetc(bmp);
        im->red[i][j] = fgetc(bmp);
        alpha = fgetc(bmp);
        count++;
      }
      // 24 bit �F 
      else if (im->bits == 24) {
        im->blue[i][j] = fgetc(bmp);
        im->green[i][j] = fgetc(bmp);
        im->red[i][j] = fgetc(bmp);
        count++;
      }
      // 8 bit �F 
      else if (im->bits == 8) {
        int index;
        index = fgetc(bmp);
	im->blue[i][j] = blue[index];
        im->green[i][j] = green[index];
        im->red[i][j] = red[index];
        count++;
      }
    }
  }
  return count;
}

int read4(FILE * bmp,
            BMPIMAGE im,
           unsigned char *red, 
           unsigned char *green, 
           unsigned char *blue)
{
  int i, j, line, position, count = 0;

  // 4byte ���E�ɂ��킹�� 
  line = (im->width * im->bits) / 8;
  if ((line % 4) != 0) {
    line = ((line / 4) + 1) * 4;
  }

  for (i = 0; i < im->height; i++) {
    // �s�̐擪�ʒu 
    position = im->offset + line * (im->height - (i + 1));
    fseek(bmp, position, SEEK_SET);
    // �l�̓ǂݍ��� 
    for (j = 0; j < (int) ((double) im->width / 2.0 + 0.5); j++) {
      int index, high, low;

      index = fgetc(bmp);
      // ��� 4bit 
      high = index >> 4;
      // ���� 4bit 
      low = index & 15;

        im->blue[i][2*j] = blue[high];
        im->green[i][2*j] = green[high];
        im->red[i][2*j] = red[high];
        im->blue[i][2*j+1] = blue[low];
        im->green[i][2*j+1] = green[low];
        im->red[i][2*j+1] = red[low];
      count += 2;
    }
  }
  return count;
}



