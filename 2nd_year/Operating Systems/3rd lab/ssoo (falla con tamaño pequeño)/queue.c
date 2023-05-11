// OS-P3 2022-2023

#include "queue.h"
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// To create a queue
queue *queue_init(int size) {
  queue *q = (queue *)malloc(sizeof(queue));

  q->size = size;

  q->elements_in=0;

  q->front=0;

  q->back=0;
  
  q->data = malloc(q->size * sizeof(struct element));
  return q;
}

// To check queue state
int queue_empty(queue *q) {
  if (q->elements_in == 0) {
    return 1;
  }
  return 0;
}

int queue_full(queue *q) {
  if (q->elements_in == q->size) {
    return 1;
  }
  return 0;
}

// To Enqueue an element
int queue_put(queue *q, struct element *x) {
  int next;
  next = q->front + 1;
  //if (next == q->size) {
    //next = 0;
  //}
  if ((q->elements_in) == q->size) {
    return -1;
  }
  q->elements_in = q->elements_in + 1;
  q->data[q->front] = *x;
  q->front = next;
  return 0;
}

// To Dequeue an element.
struct element *queue_get(queue *q) {
  struct element *element;
  if (queue_empty(q) == 1) {
    exit(-1);
  }
  //printf("Testing before ...\n");
  element = &(q->data[q->back]);
  if (q->back + 1 == q->size) {
    q->front = 0;
  } else {
    q->back++;
  }
  q->elements_in--;

  return element;
}

void print_queue(struct queue *q) {
  int v = 2; // queue_empty(q);
  // if (v==1) {
  //     printf("Queue is empty.\n");
  //     return;
  // }
  printf("Queue elements: \n");
  for (int i = q->back; i <= q->front; i++) {
    printf("(%c, %d, %d, %d) ", q->data[i].what, q->data[i].to_who,
           q->data[i].by_who, q->data[i].how_much);
    printf("%d-----------------------------\n", i);
  }
}

// To destroy the queue and free the resources
int queue_destroy(queue *q) {
  free(q->data);
  free(q);
  return 0;
}
