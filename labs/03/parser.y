%{
#include <stdio.h>
int yylex(void);
void yyerror(const char *s);
%}

%token THE A BOY GIRL FLOWER TOUCHES LIKES SEES WITH EOL

%%

sentence : noun_phrase verb_phrase EOL {
    printf("PASS\n");
}
        | sentence noun_phrase verb_phrase EOL {
    printf("PASS\n");
}
        | error EOL {
    printf("FAIL\n");
}
        ;

noun_phrase : article noun {
    printf("noun_phrase\n");
}
            | article noun prep_phrase {
    printf("noun_phrase\n");
}
            ;

verb_phrase : verb {
    printf("verb_phrase\n");
}
            | verb noun_phrase {
    printf("verb_phrase\n");
}
            ;

prep_phrase : prep cmplx_noun {
    printf("prep_phrase\n");
}
            ;

cmplx_noun : noun {
    printf("cmplx_noun\n");
}
            | noun prep_phrase {
    printf("cmplx_noun\n");
}
            ;

article : A {
    printf("article\n");
}
        | THE {
    printf("article\n");
}
        ;

noun : BOY {
    printf("noun\n");
}
        | GIRL {
    printf("noun\n");
}
        | FLOWER {
    printf("noun\n");
}
        ;

verb : TOUCHES {
    printf("verb\n");
}
        | LIKES {
    printf("verb\n");
}
        | SEES {
    printf("verb\n");
}
        ;

prep : WITH {
    printf("prep\n");
}
        ;

%%

void yyerror(const char *s) {
    printf("Error: %s\n", s);
}

int main(void) {
    yyparse();
    return 0;
}