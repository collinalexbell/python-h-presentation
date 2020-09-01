#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <string.h>

static PyObject *HelloWorldError;
static PyObject * helloworld(PyObject *self, PyObject *args) {
		const char *name;
    int num_printed;

    if (!PyArg_ParseTuple(args, "s", &name))
        return NULL;
    num_printed = printf("Hello %s\n", name);
    if (strlen(name) <= 0) {
        PyErr_SetString(HelloWorldError, "No name provided");
        return NULL;
    }
    return PyLong_FromLong(num_printed);
}

static PyMethodDef HelloWorldMethods[] = {
    {"world",  helloworld, METH_VARARGS,
     "Execute a shell command."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef helloworldmodule = {
    PyModuleDef_HEAD_INIT,
    "hello",   /* name of module */
    "This is a module docstring", /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    HelloWorldMethods
};


PyMODINIT_FUNC PyInit_hello(void) {
    PyObject *m;

    m = PyModule_Create(&helloworldmodule);
    if (m == NULL)
        return NULL;

    HelloWorldError = PyErr_NewException("helloworld.error", NULL, NULL);
    Py_XINCREF(HelloWorldError);
    if (PyModule_AddObject(m, "error", HelloWorldError) < 0) {
        Py_XDECREF(HelloWorldError);
        Py_CLEAR(HelloWorldError);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}

