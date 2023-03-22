#include <stdio.h>
#include "Python.h"

/**
 * print_python_list_info - prints basic info and python list
 * @p: A PyObject list
 */

void print_python_list_info(PyObject *l)
{
	PyListObject *ll;
	int i;

	ll = (PyListObject *)l;

	printf("[*] Size of the Python List = %ld\n", ll->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", ll->allocated);
	for (i = 0; i < ll->ob_base.ob_size; i++)
	{
		printf("Element %d: %s", i, ll->ob_item[i]->ob_type->tp_name);
		printf("\n");
	}
}

