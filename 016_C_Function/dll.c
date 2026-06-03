// http://jaster-textcube.blogspot.com/2008/03/mingw%EC%97%90%EC%84%9C-dll-%EB%A7%8C%EB%93%A4%EA%B8%B0-msvc%EC%97%90%EC%84%9C-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0.html
#include <stdio.h>
#include "dll.h"

extern "C" int DLLEXPORT hello(char *name)
{
	printf ("Hello\n");
}