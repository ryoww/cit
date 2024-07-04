# 大数の法則に関する考察

## はじめに

大数の法則（Law of Large Numbers）とは、確率変数の独立した試行を繰り返すと、その平均値が真の平均値に収束するという統計学の原理。

## プログラム 1：円周率の近似

### コードの説明

このプログラムでは、ランダムな点を正方形の中に打ち、円の内部に落ちた点の数を数えることで円周率$\pi$を近似します。

```python
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
import matplotlib.patches as patches
import math

fig, ax = plt.subplots()

value = []
x = []
y = []
ims = []
n = 0

c = patches.Circle(xy=(0, 0), radius=1, fill=False)

N1 = 10000
n = 0
counter = 1

for i in range(N1):
    yy = (random.uniform(-1, 1))
    xx = (random.uniform(-1, 1))

    x.append(xx)
    y.append(yy)

    if math.sqrt(xx**2 + yy**2) < 1: #円の内部に落ちたものをカウント
        n = n + 1

    p = 4 * float(n / counter)

    text1 = ax.text(-0.5, 0.1, "pi:" + str(p), size=20, color="green")
    text2 = ax.text(-0.5, 0.3, str(n) + ":" + str(N1), size=20, color="green")

    ax.add_patch(c)
    im = plt.scatter(x, y, s=10)
    ims.append([im] + [text1] + [text2])

    counter = counter + 1

ani = animation.ArtistAnimation(fig, ims, interval=150)
plt.show()
```

### 大数の法則との関係

このプログラムでは、点の数が増えるにつれて円周率の近似値が真の値に収束する様子が観察できる。点の数が少ない場合、近似値にはばらつきがあるが、試行回数が増えるにつれて値は安定してくる。

```python
N1 = 100
```

の条件で実行した場合、$\pi = 3.44$ なった。また、

```python
N1 = 10000
```

の条件で実行した場合、$\pi = 3.15$ となったことからも点の数が増えるにつれて円周率の近似値が真の値に収束しつつあることが分かる。

## 結論

大数の法則は、多くの試行を行うことで結果が真の値に収束することを示す。円周率の近似やコイントスのシミュレーションを通じて、この法則の実証を確認できた。試行回数が多くなるほど、結果は理論値に近づき、ばらつきが減少する。
