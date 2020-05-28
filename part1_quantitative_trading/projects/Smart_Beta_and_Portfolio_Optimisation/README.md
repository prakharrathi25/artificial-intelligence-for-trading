# Project: Trading with Momentum

**Aim:** Creating and optimizing a smart beta stock portfolio.
**Topic**: Portfolio Optimization, ETFs, Indices, and Stocks.

## Overview
* Building a smart beta portfolio and calculating its tracking error against a benchmark stock index in order to see how well it performs.
* Using quadratic programming to optimize the portfolio's weights.
* Rebalancing this portfolio and then calculating turnover in order to evaluate performance and determine optimal rebalancing frequency.
* The dataset is a set of end-of-day stock prices that comes from Quotemedia.* The dataset is a set of end-of-day stock prices that comes from [Quotemedia](http://www.quotemedia.com/).

## Concepts
* Using Pandas/NumPy to calculate portfolio weights based on dollar volume, as well as weights based on dividend returns.
* Writing methods that compute returns, weighted returns, cumulative returns, and tracking error.
* Solving convex optimization problems (quadratic programming) with the CVXPY Python library.
* Implementing methods that rebalance portfolio weights at any desired frequency and return the cost, or annualized turnover, of doing so.

## Grading and Evaluation 

* [Here](https://review.udacity.com/#!/reviews/2300739)
