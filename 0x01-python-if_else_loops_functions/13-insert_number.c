#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *newItem;
    listint_t *currentItem;
    listint_t *prevItem;

    currentItem = *head;
    newItem = malloc(sizeof(listint_t));
    if (newItem == NULL)
        return (NULL);
    newItem->n = number;
    newItem->next = NULL;
    while (currentItem != NULL)
    {
        prevItem = currentItem;
        currentItem = currentItem->next;
        if ((newItem->n >= prevItem->n) && (newItem->n <= currentItem->n))
        {
            prevItem->next = newItem;
            newItem->next = currentItem;
        }
        else
        {
            prevItem->next = newItem;
        }
    }
    return (newItem);

}