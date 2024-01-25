%{
#include "y.tab.h"
%}

%%

"the"               { return THE; }
"a"                 { return A; }
"boy"               { return BOY; }
"girl"              { return GIRL; }
"flower"            { return FLOWER; }
"touches"           { return TOUCHES; }
"likes"             { return LIKES; }
"sees"              { return SEES; }
"with"              { return WITH; }
\n                  { return EOL; }
.                   { /* Ignore any other characters */ }

%%

int yywrap(void) {
    return 1;
}
