#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * check_cycle - Checks if there is a cycle in the list
 * @list: Head of the linked list
 * Return: 1 if there is a cycle, otherwise returns 0
 */
int check_cycle(listint_t *list)
{
	listint_t *normal = NULL;
	listint_t *lento = NULL;
	int contador = 0;

	normal = list;
	lento = list;

	while (normal != NULL)
	{
		normal = normal->next;
		contador++;

		if (contador == 3)
		{
			lento = lento->next;
			contador = 0;
		}

		if (normal == lento)
		{
			return (1);
		}
	}
	return (0);
}
