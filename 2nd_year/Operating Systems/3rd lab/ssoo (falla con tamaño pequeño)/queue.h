#ifndef HEADER_FILE
#define HEADER_FILE


struct element {
	// Define the struct yourself
	char what;
  int to_who;
  int by_who;
  int how_much;
};

typedef struct queue {
	// Define the struct yourself
	int elements_in;
	int size;
	int front;
	int back;
  struct element *data;


}queue;

queue* queue_init (int size);
int queue_destroy (queue *q);
int queue_put (queue *q, struct element* elem);
struct element * queue_get(queue *q);
int queue_empty (queue *q);
int queue_full(queue *q);
void print_queue(queue *q);

#endif
