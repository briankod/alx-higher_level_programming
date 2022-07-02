#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - function that prints strings in Python
 * @p: a pointer to the Python object
 *
 * Return: void.
 */
void print_python_string(PyObject *p)
{
	PyObject *s, *rep;

	(void)rep;
	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "s"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	rep = PyObject_rep(p);
	s = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
	printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
	printf("  value: %s\n", PyBytes_AsString(s));
}
