#include "lists.h"
#include <stdio.h>
/**
* check_cycle - checks if a singly linked list has a cycle in it
* @list: the list to be checked
* Return: 1 if cycle detected else 0
*/
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast = list;

	if (!list || !list->next)
		return (0);
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
