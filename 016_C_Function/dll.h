#ifdef BUILD_DLL
    #define DLLEXPORT __declspec(dllexport)
#else
    #define DLLEXPORT __declspec(dllimport)
#endif

extern "C" int DLLEXPORT hello(char*);