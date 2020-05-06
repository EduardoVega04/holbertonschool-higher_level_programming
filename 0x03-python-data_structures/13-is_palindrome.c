#include "lists.h"
/**
 * is_palindrome - Checks if a linked list is palindrome
 * @head: pointer to head of list
 * Return: 1 if it's palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int *array = NULL;
	int nodos = 0;
	int i = 0;
	int j;

	if (*head == NULL || head == NULL)
		return (1);

	while (tmp != NULL)
	{
		nodos++;
		tmp = tmp->next;
	}

	array = malloc(sizeof(int) * 100);
	tmp = *head;

	while (tmp != NULL)
	{
		array[i] = tmp->n;
		i++;
		tmp = tmp->next;
	}

	for (j = 0; j < (nodos / 2); j++)
	{
		if (array[j] == array[nodos - 1])
		{
			nodos--;
			continue;
		}
		else
			return (0);
	}
	return (1);
}
