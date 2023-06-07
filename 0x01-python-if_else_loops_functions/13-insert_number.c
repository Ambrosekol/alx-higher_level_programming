#include "lists.h"
#include <stdio.h>
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *newItem;
    listint_t *currentItem, *prevItem;
    listint_t *mainval;

    currentItem = *head;
    mainval = *head;
    newItem = malloc(sizeof(listint_t));
    if (newItem == NULL)
        return (NULL);
    newItem->n = number;
    newItem->next = NULL;
    if (*head == NULL)
    {
        *head = newItem;
        return (newItem);
    }
    /*while (mainval != NULL)
    {
        if ((mainval->next == NULL) && (mainval->n < newItem->n))
        {
           mainval->next = newItem;
        }
        mainval = mainval->next;
    }*/
    while (currentItem != NULL)
    {
        prevItem = currentItem;
        currentItem = prevItem->next;
        if ((newItem->n > prevItem->n) && (newItem->n < currentItem->n))
        {
            prevItem->next = newItem;
            newItem->next = currentItem;
        }
        else if (prevItem->n == newItem->n)
        {
            prevItem->next = newItem;
            newItem->next = currentItem;
        }
        else if (mainval->n > newItem->n)
        {
            newItem->next = mainval;
            *head = newItem;
        }
    }
    return (newItem);
}