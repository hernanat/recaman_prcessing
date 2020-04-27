# About

This is a small processing program to visualize [Recaman's sequence](https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence).

# Usage

You can include tickers on the number line:

```python
drawNumberLine(tickers = True)
```

You can draw the points of the sequence with the arcs:

```python
drawSequenceArcs(points = True)
```

Instead of arcs, you can draw circles whose diameters are
  equal to the distance `|a_n - a_{n-1}|`.

