#include <Python.h>
#include "structmember.h"

typedef struct{
  PyObject_HEAD
  float x;
} Kvadratas;

static void Kvadratas_dealloc(Kvadratas* self){
    Py_TYPE(self)->tp_free((PyObject*)self);
}

static PyObject * Kvadratas_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    Kvadratas *self;

    self = (Kvadratas *)type->tp_alloc(type, 0);
    if (self != NULL) {
        self->x = 0;
    }

    return (PyObject *)self;
}

static int Kvadratas_init(Kvadratas *self, PyObject *args, PyObject *kwds)
{
    if (!PyArg_ParseTuple(args, "f", &self->x))
        return -1;
    return 0;
}

static PyMemberDef Kvadratas_members[] = {
    {"x", T_INT, offsetof(Kvadratas, x), 0, "Kvadrato krastine"},
    {NULL}  /* Sentinel */
};


static PyObject * Kvadratas_diagonal(Kvadratas* self)
{
    return Py_BuildValue("f", self->x * sqrt(2));
}
static PyMethodDef Kvadratas_methods[] = {
    {"diagonal", (PyCFunction)Kvadratas_diagonal, METH_NOARGS, "Apskaiciuoti kvadrato istrizaine"},
    {NULL}  /* Sentinel */
};

static PyObject* Kvadratas_str(Kvadratas* self){
    return PyUnicode_FromFormat("(%f)", self->x);
}


static PyTypeObject kvadratasType ={
  PyVarObject_HEAD_INIT(NULL, 0) 
  "Kvadratai.Kvadratas", /*tp_name*/
  sizeof(Kvadratas), /*tp_basicsize*/
  0, /*tp_itemsize*/
  (destructor) Kvadratas_dealloc, /*tp_dealloc*/
  0, /*tp_print*/
  0, /*tp_getattr*/
  0, /*tp_setattr*/
  0, /*tp_reserved*/
  0, /*tp_repr*/
  0, /*tp_as_number*/
  0, /*tp_as_sequence*/
  0, /*tp_as_mapping*/
  0, /*tp_hash */
  0, /*tp_call*/
  (reprfunc) Kvadratas_str, /*tp_str*/
  0, /*tp_getattro*/
  0, /*tp_setattro*/
  0, /*tp_as_buffer*/ 
  Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE, /*tp_flags*/ 
  "Apskaiciuoti kvadrato istrizaine pagal krastine", /* tp_doc */
  0,
  0,
  0,
  0,
  0,
  0,
  Kvadratas_methods, //cia bus metodai
  Kvadratas_members,
  0,
  0,
  0,
  0,
  0,
  0,
  (initproc)Kvadratas_init,
  0,
  Kvadratas_new,
};




static struct PyModuleDef kvadratai ={
  PyModuleDef_HEAD_INIT, 
  "Kvadratai", // name of module 
  "Kvadrato tipas", // module documentation, may be NULL
  -1, // size of per- interpreter state of the module, or -1 if the module keeps state in global variables. 
  NULL, NULL, NULL, NULL, NULL
};

PyMODINIT_FUNC PyInit_kvadratas (void){
  PyObject* m;
  if (PyType_Ready(&kvadratasType) < 0)
    return NULL;
  m = PyModule_Create(&kvadratai);
  if (m == NULL)
    return NULL;
  Py_INCREF(&kvadratasType);
  PyModule_AddObject(m, "Kvadratas", (PyObject*)&kvadratasType);
  return m;
}