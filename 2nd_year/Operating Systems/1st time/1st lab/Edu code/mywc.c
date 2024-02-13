#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

#define BUFFER_SIZE 1

int main(int argc, char *argv[]) {
    // Check if the program was called with at least one argument (the input file).
    if (argc < 2) {
        printf("Too few arguments. \nUsage: %s <input file>\n", argv[0]);
        return -1;
    }

    // Open the input file for reading.
    int fd = open(argv[1], O_RDONLY);
    if (fd == -1) {
        printf("Error opening file %s\n", argv[1]);
        return -1;
    }

    // Initialize the line, word, and byte counters.
    int lines = 0, words = 0, bytes = 0;
    // Initialize a buffer to store the bytes read from the file. This is done but not completely necessary as the
    // buffer size will be of length 1, but we think it is good practice to do it this way, as it is more versatile
    char buffer[BUFFER_SIZE];
    // Initialize a variable to keep track of whether we are currently inside a word.
    int in_word = 0;
    // Read the file in chunks of size BUFFER_SIZE, in this case 1, and update the counters based on the bytes read.
    int n;
    while ((n = read(fd, buffer, BUFFER_SIZE)) > 0) {
        bytes += n;
        // This for would be used if the BUFFER_SIZE was anything larger than 1
        //for (int i = 0; i < n; i++) {
        // If we encounter a newline character, increment the line counter and reset the in_word flag.
        // We are using the in_word as a boolean to check weather the character being analyzed is inside a word.
        if (buffer[0] == '\n') {
            lines++;
            in_word = 0;
            // If we encounter a space or a tab character, reset the in_word flag, as this is the separation between words.
        } else if (buffer[0] == ' ' || buffer[0] == '\t') {
            in_word = 0;
            // If we encounter a non-space character, and we were not inside a word before, increment the word
            // counter and set the in_word flag.
        } else if (!in_word) {
            in_word = 1;
            words++;
        }
        // Lastly, if we are inside a word, and a character is read, no counter will be updated except for the
        // bytes one, which is done at the start.
        //} If the BUFFER_SIZE was anything but 1, this line would need to be uncommented

    }

    // fd is the name given to the file inside the code, to reference the open file
    // CLOSE the input file.
    close(fd);

    // Check if there was an error reading the file, and print an error message if there was.
    if (n == -1) {
        printf("Error reading file %s\n", argv[1]);
        return -1;
    }

    // Print the line, word, and byte counters, followed by the input file name.
    printf("%d %d %d %s\n", lines, words, bytes, argv[1]);
    return 0;
}