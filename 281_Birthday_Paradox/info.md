# Birthday Paradox
```
In a set of n randomly selected people, what is the probability that at least two people share the same birthday?
What is the smallest value of n where the probability is at least 50% or 99%?
```


Let `p(N)` be the probability that at least two of a group of `n` randomly selected people share the same birthday. By the pigeonhole principle, since there are `366` possibilities for birthdays (including February 29), it follows that when `n >= 367`, `p(n) = 100%`. The counterintuitive part of the answer is that for smaller `n`, the relationship between n and `p(n)` is (very) non-linear.

In fact, the thresholds to surpass 50% and 99% are quite small: 50% probability is reached with just 23 people and 99% with just 70 people.

```
A mathematical paradox is any statement (or a set of statements) that seems to contradict itself (or each other) while simultaneously seeming completely logical. Paradox (at least mathematical paradox) is only a wrong statement that seems right because of lack of essential logic or information or application of logic to a situation where it is not applicable. 
```

Though it is not technically a paradox, it is often referred to as such because the probability is counter-intuitively high.

**Explanation:**
```
Imagine you are in a room with a group of friends. You might think that it's unlikely for two people in the room to have the same birthday because there are 365 days in a year, right?

Well, the birthday paradox is a bit surprising. It says that in a group of just 23 people, there's actually a pretty good chance that at least two of them share the same birthday!

This might seem strange at first, but here's why it happens: There are so many pairs of people in the room, and each pair could potentially have a matching birthday. With 23 people, there are 253 possible pairs (23 people choose 2), and that's a lot of chances for a birthday match.

So, even though there are 365 days in a year, when you have a group of people, the chances of at least two people having the same birthday become surprisingly high. It's a fun math puzzle that shows how our intuition about probability can sometimes be a bit different from what math tells us.
```

## Use Case:

Real-world applications for the birthday problem include a cryptographic attack called the birthday attack, which uses this probabilistic model to reduce the complexity of finding a collision for a hash function, as well as calculating the approximate risk of a hash collision existing within the hashes of a given size of population.