#include "lists.h"
/**
 * is_palindrome - Checks if a linked list is palindrome
 * @head: pointer to head of list
 * Return: 1 if it's palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int size;
	int options[2048];
	int i;

	size = 0;
	if (head == NULL || *head == NULL)
		return (1);

	while(*head != NULL)
	{
		size++;
		options[size - 1] = (*head)->n;
		head = &(*head)->next;
	}

	for (i = 0; i < size / 2; i++)
	{
		if (options[i] != options[size - i - 1])
			return (0);
	}

	return (1);
}

