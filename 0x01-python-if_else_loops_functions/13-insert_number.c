#include "lists.h"
/**
 * insert_node - Insert a new node in a sorted linked list
 * @head: Head of the linked list
 * @number: Data to the new node
 * Return: Addres of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	int contador = 0;
	listint_t *tmp_lento = *head;
	listint_t *tmp_rapido = *head;
	listint_t *new_node = NULL;

	if (*head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	while (tmp_rapido->next != NULL && tmp_rapido->n < number)
	{
		if (tmp_lento->next != NULL && contador == 1)
		{
			tmp_lento = tmp_lento->next;
			contador = 0;
		}

		contador++;
		tmp_rapido = tmp_rapido->next;
	}

	tmp_lento->next = new_node;
	new_node->next = tmp_rapido;

	return (new_node);
}
