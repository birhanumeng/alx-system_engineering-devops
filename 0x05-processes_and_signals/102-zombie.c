#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - Creates an infinite loop to make
 * a program stall
 *
 * Return: 0 (Success)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Crates 5 zombie processes
 *
 * Return: 0 (Success)
 */
int main(void)
{
	int i;
	pid_t Zombie;

	for (i = 0; i < 5; i++)
	{
		Zombie = fork();
		if (!Zombie)
			return (0);
		printf("Zombie process created, PID: %d\n", Zombie);
	}
	infinite_while();
	return (0);
}
