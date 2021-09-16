# Simulate Monty Hall game in Python
If you don't know probability or think that it is hard to understand the proof, but want to know which is the right answer to the Monty Hall problem, 
why don't you just actually play it many times and see the result?

### Here are some assumptions:
1. You don't want a goat.
1. The player randomly choose a door.
2. The monty always open a door which has a goat and not the player's door.

# Bonus: Birthday Problem

You may hear the birthday problem.
*There are k people in a room. Assume each person’s birthday is equally likely to be any of the 365 days of the year (we exclude February 29), and that people’s birthdays are independent (we will define independence formally later, but intuitively it means that knowing some people’s birthdays gives us no information about other people’s birthdays; this would not hold if, e.g., we knew that two of the people were twins). What is the probability that at least one pair of people in the group have the same birthday? - Introduction to probability by Joseph K.Blitzstein, Jessica Hwang, page 12*.

And they said that only 23 people is enough for the 50/50 chance, but you didn't buy it. Now we will find out the true by actually sample n people randomly many times to see that how many people are enough for the 50/50 chance.

![Number of people and probability of a birthday match.](./images/birthday_problem.png)

