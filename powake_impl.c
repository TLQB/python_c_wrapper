#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <string.h>

static const char VALID_LICENSE[] = "ABC123-XYZ789";
static int is_licensed = 0;

static PyObject* check_license(PyObject* self, PyObject* args) {
    const char* license_key;
    if (!PyArg_ParseTuple(args, "s", &license_key)) {
        return NULL;
    }
    
    is_licensed = (strcmp(license_key, VALID_LICENSE) == 0);
    return PyBool_FromLong(is_licensed);
}

static PyObject* impl_func(PyObject* self, PyObject* args) {
    if (!is_licensed) {
        PyErr_SetString(PyExc_RuntimeError, "License key không hợp lệ hoặc chưa được kích hoạt");
        return NULL;
    }
    
    printf("Hello World\n");
    fflush(stdout);
    Py_RETURN_NONE;
}

static PyMethodDef AMethods[] = {
    {"func", impl_func, METH_NOARGS, "Prints Hello World"},
    {"add_license", check_license, METH_VARARGS, "Checks license key"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef amodule = {
    PyModuleDef_HEAD_INIT,
    "a_impl",
    NULL,
    -1,
    AMethods
};

PyMODINIT_FUNC PyInit_powake_impl(void) {
    return PyModule_Create(&amodule);
}