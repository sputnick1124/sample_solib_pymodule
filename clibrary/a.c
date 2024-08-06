#include <math.h>
#include "a.h"

struct Res quadratic(struct Inp i) {
	struct Res res = { .valid = 0 };
	double r = i.b*i.b - 4*i.a*i.c;
	if (r > 0) {
		double det = 2*i.a;
		double rs = sqrt(r);
		res.valid = 1;
		res.a = (-i.b + rs) / det;
		res.b = (-i.b - rs) / det;
	}
	return res;
}
