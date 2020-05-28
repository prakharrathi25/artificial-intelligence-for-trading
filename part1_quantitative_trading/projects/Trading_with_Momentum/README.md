# Project: Trading with Momentum
**Aim:** Implementing a momentum trading strategy and testing to see if it has the potential to be profitable. 

**Topic**: Basic Quantitative Trading

## Overview
* Generating a trading signal based on a momentum indicator, computing this signal for a given time range, and applying the signal to a dataset in order to estimate projected returns.
* Performing a statistical test on the mean of the returns to conclude if there is alpha in the signal.
* The dataset is a set of end-of-day stock prices that comes from [Quotemedia](http://www.quotemedia.com/).

## Concepts
* Using Pandas to resample end-of-day stock prices to a dataframe of end-of-month prices.
* Implementing Python methods that:
    - Return the best and worst performing stocks at a given point in time.
    - Calculate a sample of the portfolio returns of longing the best stocks and shorting the worst ones over a particular time window.
* Calculating the T-statistic and its corresponding p-value, and using this information to determine whether it is safe to rule out the possibility that the observed sample portfolio returns came about due to random chance.

## Grading and Evaluation 

* [Here](https://review.udacity.com/#!/reviews/2294895)
