
# 0x00. Python - Hello, World

## Learning Objectives
- How to use the Python interpreter
- How to print text and variables using **```print```**
- How to use strings
- What are indexing and slicing in Python


## 0. Run Python file

👻 Write a Shell script that runs a Python script.

- The Python file name will be saved in the environment variable **```$PYFILE```**
  , hint: ```export PYFILE=main.py```

## 1. Run inline
👻 Write a Shell script that runs Python code.

- The Python code will be saved in the environment variable **```$PYCODE```**, hint:
  ```export PYCODE='print(f"Best School: {88+10}")'```

## 2. Hello, print
👻 Write a Python script that prints exactly **```"Programming is like building a multilingual puzzle, followed by a new line.```**
- Use the function **```print```**

## 3. Print integer
👻 Write a Python script that prints the integer stored in the variable **```number```**, followed by **```Battery street```**, followed by a new line.
- You are not allowed to cast the variable **```number```** into a string
- Your code must be 3 lines long
- You have to use f-strings 

## 4. Print float
👻 Write a Python script that prints the float stored in the variable **```number```** with a precision of 2 digits.
- The output of the program should be:
    - **```Float```**:, followed by the float with only 2 digits
    - followed by a new line
- You are not allowed to cast **```number```** to string
- You have to use f-strings

## 5. Print string
👻 Write a Python script that prints 3 times a string stored in the variable **```str```**, followed by its first 9 characters.
- You are not allowed to use any loops or conditional statement
- Your program should be maximum 5 lines long

## 6. Play with strings
👻 Write a Python script that prints **```Welcome to Holberton School!```**
- You are not allowed to use any loops or conditional statements.
- You have to use the variables **```str1```** and **```str2```** in your new line of code
- Your program should be exactly 5 lines long, check with: ```wc -l 6-concat.py```

## 7. Copy - Cut - Paste
👻 Write a Python script exactly 8 lines long
- **```word_first_3```** should contain the first 3 letters of the variable **```word```**
- **```word_last_2```** should contain the last 2 letters of the variable **```word```**
- **```middle_word```** should contain the value of the variable **```word```** without the first and last letters

## 8. Create a new sentence
👻 Write a Python script that prints **```object-oriented programming with Python```**, followed by a new line.
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 5 lines long
- You are not allowed to create new variables
- You are not allowed to use string literals

## 9. Easter Egg
👻 Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
- Your script should be maximum 98 characters long, check with: ```wc -m 9-easter_egg.py```

## 10. Linked list cycle ~~```pending```~~ :(
👻 Write a function in C that checks if a singly linked list has a cycle in it.
- Prototype: **```int check_cycle(listint_t *list);```**
- Return: **```0```** if there is no cycle, **```1```** if there is a cycle
Requirements:

- Only these functions are allowed: **```write```**, **```printf```**, **```putchar```**, **```puts```**, **```malloc```**, **```free```**
<details><summary>Use</summary><blockquote>
  <details><summary>list.h</summary><blockquote>

    #ifndef LISTS_H
    #define LISTS_H

    #include <stdlib.h>

    /**
    * struct listint_s - singly linked list
    * @n: integer
    * @next: points to the next node
    *
    * Description: singly linked list node structure
    * 
    */
    typedef struct listint_s
    {
        int n;
        struct listint_s *next;
    } listint_t;

    size_t print_listint(const listint_t *h);
    listint_t *add_nodeint(listint_t **head, const int n);
    void free_listint(listint_t *head);
    int check_cycle(listint_t *list);

    #endif /* LISTS_H */
  </blockquote></details>
  <details><summary>10-linked_lists.c</summary><blockquote>

    #include <stdio.h>
    #include <stdlib.h>
    #include "lists.h"

    /**
    * print_listint - prints all elements of a listint_t list
    * @h: pointer to head of list
    * Return: number of nodes
    */
    size_t print_listint(const listint_t *h)
    {
        const listint_t *current;
        unsigned int n; /* number of nodes */

        current = h;
        n = 0;
        while (current != NULL)
        {
            printf("%i\n", current->n);
            current = current->next;
            n++;
        }

        return (n);
    }

    /**
    * add_nodeint - adds a new node at the beginning of a listint_t list
    * @head: pointer to a pointer of the start of the list
    * @n: integer to be included in node
    * Return: address of the new element or NULL if it fails
    */
    listint_t *add_nodeint(listint_t **head, const int n)
    {
        listint_t *new;

        new = malloc(sizeof(listint_t));
        if (new == NULL)
            return (NULL);

        new->n = n;
        new->next = *head;
        *head = new;

        return (new);
    }

    /**
    * free_listint - frees a listint_t list
    * @head: pointer to list to be freed
    * Return: void
    */
    void free_listint(listint_t *head)
    {
        listint_t *current;

        while (head != NULL)
        {
            current = head;
            head = head->next;
            free(current);
        }
    }
  </blockquote></details>
  <details><summary>10-main.c</summary><blockquote>

    #include <stdlib.h>
    #include <string.h>
    #include <stdio.h>
    #include "lists.h"

    /**
    * main - check the code
    *
    * Return: Always 0.
    */
    int main(void)
    {
        listint_t *head;
        listint_t *current;
        listint_t *temp;
        int i;

        head = NULL;
        add_nodeint(&head, 0);
        add_nodeint(&head, 1);
        add_nodeint(&head, 2);
        add_nodeint(&head, 3);
        add_nodeint(&head, 4);
        add_nodeint(&head, 98);
        add_nodeint(&head, 402);
        add_nodeint(&head, 1024);
        print_listint(head);

        if (check_cycle(head) == 0)
            printf("Linked list has no cycle\n");
        else if (check_cycle(head) == 1)
            printf("Linked list has a cycle\n");

        current = head;
        for (i = 0; i < 4; i++)
            current = current->next;
        temp = current->next;
        current->next = head;

        if (check_cycle(head) == 0)
            printf("Linked list has no cycle\n");
        else if (check_cycle(head) == 1)
            printf("Linked list has a cycle\n");

        current = head;
        for (i = 0; i < 4; i++)
            current = current->next;
        current->next = temp;

        free_listint(head);

        return (0);
    }
  </blockquote></details>
</blockquote></details>

Compile with:
```bash
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle
```

## 11. Hello, write
👻 Write a Python script that prints exactly **```and that piece of art is useful - Dora Korpar, 2015-10-19```**, followed by a new line.
- Use the function **```write```** from the **```sys```** module
- You are not allowed to use **```print```**
- Your script should print to **```stderr```**
- Your script should exit with the status code **```1```**

## 12. Compile
👻 Write a Python script compiles a Python script file.
- The Python file name will be stored in the environment variable **```$PYFILE```**
- The output filename has to be **```$PYFILEc```** (ex: **```export PYFILE=my_main.py```** => output filename: **```my_main.pyc```**)

After executing **```101-compile```**, check for **```main.pyc```**

```bash
  ls
```
Search and count occurrences of the string from the file.
```bash
  cat main.pyc | zgrep -c "Best School"
```
Display the file in hexadecimal bytes format.
```bash
  od -t x1 main.pyc # SYSTEM DEPENDANT => CAN BE DIFFERENT
```

## 13. ByteCode -> Python #1
👻 Write the Python function **```def magic_calculation(a, b):```** that does exactly the same as the following Python bytecode
```
  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```
