
%module cpython
%{
    #define SWIG_FILE_WITH_INIT
    #include "cpython.h"
%}

int Hello(int str);
