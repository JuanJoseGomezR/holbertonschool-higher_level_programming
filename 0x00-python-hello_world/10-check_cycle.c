#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
  * list - linked list
  * Return: integer
  */
int check_cycle(listint_t *list)
{
	listint_t *aux;

	if (list == '\0')
		return (0);
	while (list)
	{
		aux = list;
		list = list->next;
		if (aux <= list)
			return (1);
	}
	return (0);
}
