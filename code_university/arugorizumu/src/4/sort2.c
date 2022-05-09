#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#define BUF_SIZE 80
#define NAME_SIZE 32
struct student {
	int score;
	char name[NAME_SIZE];
};
struct student *table;
int counter_compare, counter_copy;
void Clear() {
	counter_compare = 0; counter_copy = 0;
}
void Counter() {
	printf("Compare %d Copy %d\n", counter_compare, counter_copy);
}
int my_compare(const struct student *a, const struct student *b) {
	counter_compare++;
	return (a->score > b->score) ? 1 : (a->score < b->score) ? -1 : 0;
}
void my_swap(struct student *a, struct student *b) {
	struct student c;
	counter_copy += 3;
	memcpy(&c, a, sizeof(struct student));
	memcpy(a, b, sizeof(struct student));
	memcpy(b, &c, sizeof(struct student));
}
/* Copy data from src to dst */
void my_copy(struct student *src, struct student *dst) {
	counter_copy++;
	memcpy(dst, src, sizeof(struct student));
}
void count_func(int size) {
	int i, key;
	int count[501]; /* Score ranges from 0 to 500 (501 key values) */
	struct student *work;
	if ((work = malloc(sizeof(struct student) * size)) == NULL) {
		printf("Cannot allocate memory \n"); exit(1);
	}
	/* Clear counter */
	for (i = 0; i <= 500; i++)
		...
	/* Frequency distribution */
	for (i = 0; i < size; i++) {
		key = table[i].score;
		...
	}
	/* Cumlative frequency distribution */
	for (i = 0; i < 500; i++)
		...
	for (i = size - 1; i >= 0; i--) {
		key = table[i].score;
		/* Copy the data, based on cumlative frequency distribution */
		...
	}
	for (i = 0; i < size; i++)
		my_copy(&work[i], &table[i]);
	free(work);
}
void Count(int size) {
	count_func(size);
}
void heap_func(int left, int right) {
	struct student root;
	int child, parent;
	/* The element which goes down the heap */
	my_copy(&table[left], &root);
	for (parent = left; parent < (right + 1) / 2; parent = child) {
		int r, l;
		l = parent * 2 + 1;
		r = l + 1;
		if (r <= right && my_compare(&table[r], &table[l]) == 1)
			child = r; /* Larger one is selected */
		else
			child = l;
		if (my_compare(&root, &table[child]) == 1) break;
		my_copy(&table[child], &table[parent]);
	}
	my_copy(&root, &table[parent]);
}
void Heap(int size) {
	int i;
	for (i = size / 2 - 1; i >= 0; i--)
		/* Heap is created for all subtrees */
		...
	/* Heap sort is performed for table[0] to table[i-1] */
	for (i = size - 1; i > 0; i--) {
		my_swap(&table[0], &table[i]);
		...
	}
}
void merge_func(int left, int right, struct student *work) {
	int center, i, j, num, base;
	if (left >= right) return;
	center = (left + right) / 2;
	/* Call merge_func() to sort the first half */
	...
	/* Call merge_func() to sort the last  half */
	...
	num = 0;
	for (i = left; i <= center; i++)
		my_copy(&table[i], &work[num++]);
	j = 0; base = left;
	while (i <= right && j < num)
		/* If work[j] is larger than table[i] */
		if (...)
			/* Copy table[i++] to table[base++] */
			...
		else
			/* Copy work[j++] to table[base++] */
			...
	while (j < num)
		/* Copy work[j++] to table[base++] */
		...
}
void Merge(int size) {
	struct student *work;
	if ((work = malloc(sizeof(struct student) * size)) == NULL) {
		printf("Cannot allocate memory \n"); exit(1);
	}
	merge_func(0, size - 1, work);
	free(work);
}
void quick_func(int left, int right) {
	int i, j;
	struct student pivot;
	if (left >= right) return;
	i = left; j = right;
	my_copy(&table[(i + j) / 2], &pivot);
	do {

		...

	} while (i <= j);
	quick_func(left, j);
	quick_func(i, right);
}
void Quick(int size) {
	quick_func(0, size - 1);
}
void Disp(int size) {
	int i;
	for (i = 0; i < size; i++)
		printf("%d\t%s\n", table[i].score, table[i].name);
}
int main(int argc, char *argv[]) {
	FILE *fp;
	int n;
	char buf[BUF_SIZE];
	char command;
	if (argc != 2) {
		printf("Usage: %s <filename>\n", argv[0]); exit(1);
	}
	if ((fp = fopen(argv[1], "r")) == NULL) {
		printf("Cannot open file (%s) \n", argv[1]); exit(1);
	}
	/* Read the file to count the number of lines in the file */
	n = 0;
	while (fgets(buf, BUF_SIZE, fp) != NULL)
		n++;
	/* Memory allocation */
	if ((table = malloc(sizeof(struct student) * n)) == NULL) {
		printf("Cannot allocate memory \n"); exit(1);
	}
	/* Read the file again to copy the data */
	n = 0;
	fseek(fp, 0L, SEEK_SET);
	while (fgets(buf, BUF_SIZE, fp) != NULL) {
		sscanf(buf, "%d\t%s", &table[n].score, table[n].name);
		n++;
	}
	fclose(fp);

	Clear();
	printf("[d]       Display Table\n");
	printf("[o]       Couting Sort\n");
	printf("[h]       Heap Sort\n");
	printf("[m]       Merge Sort\n");
	printf("[q]       Quick Sort\n");
	printf("[c]       Clear Counters\n");
	printf("[e]       Exit\n");
	for (;;) {
		scanf(" %c", &command);
		switch (command) {
		case 'd':	Disp(n); break;
		case 'o':	Count(n); Counter(); break;
		case 'h':	Heap(n); Counter(); break;
		case 'm':	Merge(n); Counter(); break;
		case 'q':	Quick(n); Counter(); break;
		case 'c':	Clear(); break;
		case 'e':	free(table); return 0;
		}
	}
	return 0;
}