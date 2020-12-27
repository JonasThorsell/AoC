// Copyright (c) 2020 Jonas Thorsell

#include <cstdlib>
#include <cstdio>
#include <cassert>

const int NCUPS = 1000000;
const int NMOVES = 10000000;

struct dll {
    struct dll * n;
    struct dll * p;
    int l;
};

struct dll * cl;
struct dll * cc;

inline void move() {
    struct dll * pick = cc->n;
    cc->n = cc->n->n->n->n;
    cc->n->p = cc;
    int dcl = cc->l - 1;
    if (dcl == 0) dcl = NCUPS;
    while (dcl == pick->l || dcl == pick->n->l || dcl == pick->n->n->l) {
        if (--dcl == 0) dcl = NCUPS;
    }
    struct dll * dc = &cl[dcl-1];
    dc->n->p = pick->n->n;
    pick->p = dc;
    pick->n->n->n = dc->n;
    dc->n = pick;
    cc = cc->n;
}

int main() {

    cl = (struct dll *)malloc(sizeof(struct dll) * NCUPS);
    for (int i = 0; i < NCUPS; i++) {
        cl[i].n = &cl[(i+1)%NCUPS];
        cl[i].p = &cl[i>0 ? i-1 : NCUPS-1];
        cl[i].l = i+1;
    }

    struct dll * cp = cl;
    for (int i = 0; i < 9; i++) {
        char c;
        int r = scanf("%c", &c);
        assert(r==1);
        int n = (int)(c-0x30);
        if (i == 0)
            cc = &cl[n-1];
        if (cp->l != n) {
            struct dll * pick = &cl[n-1];
            pick->p->n = pick->n;
            pick->n->p = pick->p;
            cp->p->n = pick;
            pick->p = cp->p;
            cp->p = pick;
            pick->n = cp;
        }
        else {
            cp = cp->n;
        }
    }
    
    for (int m = 0; m < NMOVES; m++) {
        move();
    }

    long long int a = (long long int)cl[0].n->l;
    long long int b = (long long int)cl[0].n->n->l;
    printf("%lli x %lli = %lli\n", a, b, a*b);
    
    free(cl);
}
