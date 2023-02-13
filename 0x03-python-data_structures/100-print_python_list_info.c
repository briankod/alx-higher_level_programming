#include "Python.h"
/**
 * print_python_list_info - function prints basic info on Python lists
 * @p: variable to the pointer
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	PyObjList *list;
	Py_ssize_t sz, s;
	PyObject *obj;
	struct _typeobject *type;

	if (strcmp(p->ob_type->tp_name, "list") == 0)
	{
		list = (PyObjList *)p;
		sz = list->ob_base.ob_size;
		printf("[*] Size of the Python List = %ld\n", sz);
		printf("[*] Allocated = %ld\n", list->allocated);
		for (s = 0; s < sz; s++)
		{
			obj = list->ob_item[s];
			type = obj->ob_type;
			printf("Element %ld: %s\n", s, type->tp_name);
		}
	}
}
