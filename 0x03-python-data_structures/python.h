#ifndef PYTHON_H
#define PYTHON_H

/* Definitions and declarations for Python API */

/* Object structures, types, and macros */
typedef struct _object
{
    /* ... */
} PyObject;

/* Function declarations */
PyObject *PyList_New(Py_ssize_t size);
Py_ssize_t PyList_Size(PyObject *list);
PyObject *PyList_GetItem(PyObject *list, Py_ssize_t index);

/* ... (more declarations) */

#endif /* PYTHON_H */
