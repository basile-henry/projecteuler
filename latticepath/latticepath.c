#include <stdio.h>

const int x = 20;
int table[x][x];

int paths(int a, int b) {
	if (a == 0 || b == 0) {
		return 1;
	} else if (table[a][b] != 0) {
		return table[a][b];
	}

	int result = paths(a-1, b) + paths(a, b-1);

	table[a][b] = result;
	table[b][a] = result;
	return result;
}

int main() {

	printf("Lattice paths for a %d by %d grid: %d\n", x, x, paths(x, x));

	return 0;
}