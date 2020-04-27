# About

This is a small [Python Processing](https://py.processing.org/) program to visualize [Recaman's sequence](https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence).

# Usage

You can include tickers on the number line:

```python
drawNumberLine(tickers = True)
```

You can draw the points of the sequence with the arcs:

```python
drawSequenceArcs(points = True)
```

![](https://github.com/hernanat/recaman_prcessing/blob/master/examples/50_terms_normal.png | width=950)
![](https://github.com/hernanat/recaman_prcessing/blob/master/examples/500_terms_normal.png | width=950)

Instead of arcs, you can draw circles whose diameters are
  equal to the distance `|a_n - a_{n-1}|`.

```python
drawSequenceArcs(mode = 'x')
```

![](https://github.com/hernanat/recaman_prcessing/blob/master/examples/50_terms_circles.png | width=950)
![](https://github.com/hernanat/recaman_prcessing/blob/master/examples/500_terms_circles.png | width=950)

