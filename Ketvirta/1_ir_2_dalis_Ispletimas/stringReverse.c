#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Python.h>

char* stringReverse(char* originalString) {
	int begin, count = 0;
	
	while(originalString[count] != '\0')
		count++;
	
	for (begin = 0; begin < count / 2; begin++) {
		char temp = originalString[begin];
		originalString[begin] = originalString[count-1-begin];
		originalString[count-1-begin] = temp;
	}	
	
	return originalString;
}

static PyObject* stringReverseError;

static PyObject* py_stringReverse(PyObject* self, PyObject* args) {
  char *n;
  if (!PyArg_ParseTuple(args, "s", &n)) {
      PyErr_SetString(stringReverseError, "Please check input string");
      return NULL;
  }

  return Py_BuildValue("s", stringReverse(n));
}

static PyMethodDef stringReverseModuleMethods[] = {
  {"stringReverse", py_stringReverse, METH_VARARGS, "Reverses input string"},
  {NULL, NULL, 0, NULL}
};

static struct PyModuleDef stringReverseModule = {
  PyModuleDef_HEAD_INIT,
  "StringReverseModule",
  "Reverses input string",
  -1,
  stringReverseModuleMethods
};

PyMODINIT_FUNC PyInit_stringReverse(void)
{
  PyObject *mod =  PyModule_Create(&stringReverseModule);
  stringReverseError = PyErr_NewException("StringReverseModule.error", NULL, NULL);
  Py_INCREF(stringReverseError);
  PyModule_AddObject(mod, "error", stringReverseError);
  return mod;
}