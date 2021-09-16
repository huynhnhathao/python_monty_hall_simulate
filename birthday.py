import numpy as np

def birthday_problem(num_people: int, n: int, ) -> float:
        """
        Randomly sample num_people peoples birthday from 1 to 355 n times and return the ratio of 
        birthday match/n
        """
        count = 0
        for i in range(0,n):
            sample = np.random.randint(1, 355, num_people)
            if len(sample) != len(set(sample)):
                count +=1
        return count/n

if __name__ == '__main__':
    print(birthday_problem(num_people=23, n = 50000))

