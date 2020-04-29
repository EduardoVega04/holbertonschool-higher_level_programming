#include "lists.h"
/**
 * insert_node - Insert a new node in a sorted linked list
 * @head: Head of the linked list
 * @number: Data to the new node
 * Return: Addres of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp_lento = *head, *tmp_rapido = *head, *new_node = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	if ((*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	tmp_rapido = (*head)->next;

	while (tmp_rapido != NULL)
	{
		if (tmp_rapido->n > number)
		{
			tmp_lento->next = new_node;
			new_node->next = tmp_rapido;
			return (new_node);
		}
		tmp_lento = tmp_lento->next;
		tmp_rapido = tmp_rapido->next;
	}

	tmp_lento->next = new_node;
	new_node->next = NULL;
	return (new_node);
}
