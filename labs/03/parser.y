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
        | sentence noun_phrase verb_phrase prep_phrase EOL {
    printf("PASS\n");
}
        | sentence noun_phrase verb_phrase prep_phrase EOL {
    printf("PASS\n");
}
        | error EOL {
    printf("FAIL\n");
}
        ;

noun_phrase : cmplx_noun {
    printf("noun_phrase\n");
}
            | cmplx_noun prep_phrase {
    printf("noun_phrase\n");
}
            ;

verb_phrase : cmplx_verb {
    printf("verb_phrase\n");
}
            | cmplx_verb prep_phrase {
    printf("verb_phrase\n");
}
            ;

prep_phrase : prep cmplx_noun {
    printf("prep_phrase\n");
}
            ;

cmplx_noun : article noun {
    printf("cmplx_noun\n");
}
            ;

cmplx_verb : verb {
    printf("cmplx_verb\n");
}
            | verb noun_phrase {
    printf("cmplx_verb\n");
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
