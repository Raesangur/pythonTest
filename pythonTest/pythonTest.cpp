#define PYTHON_SOURCE "../../../Programmes/Python_382/include/Python.h"
#include PYTHON_SOURCE
#include <iostream>

int
main()
{
    PyObject* pInt;
    Py_Initialize();
    FILE* fp = _Py_fopen("../Hello World.py", "r");
    PyRun_SimpleFile(fp, "../Hello World.py");
    Py_Finalize();

    std::cout << "Hello World from this C++ code!\n";

    return 0;
}
