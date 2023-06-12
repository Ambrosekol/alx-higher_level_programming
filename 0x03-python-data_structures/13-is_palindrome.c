#include "lists.h"
/**
  * is_palindrome - Checks if a list is a palendrome
  * @head: List Head
  * Return: returns a 1 or 0
  */

int is_palindrome(listint_t **head)
{
	listint_t *arry;
	int buffer[1024], indx, fwd, prev;

	arry = *head;
	indx = 0;
	fwd = 0;
	if (*head == NULL)
		return (1);
	while (arry != NULL)
	{
		buffer[indx] = arry->n;
		indx += 1;
		arry = arry->next;
	}
	if ((indx % 2) != 0)
	{
		return (0);
	}
	prev = indx - 1;
	while (fwd < (indx / 2))
	{
		if (buffer[fwd] != buffer[prev])
		{
			return (0);
		}
		prev -= 1;
		fwd += 1;
	}
	return (1);
}
