from PIL import Image
import random
import math

def smoothstep(t):
    return t * t * (3 - 2 * t)

def value_noise_purepython(width, height, scale=8, octaves=4, persistence=0.5, seed=None):
    if seed is not None:
        random.seed(seed)
    def single_layer(sx, sy):
        gx = int(math.ceil(width / sx)) + 1
        gy = int(math.ceil(height / sy)) + 1
        grid = [[random.random() for _ in range(gx)] for __ in range(gy)]
        xs = [i / sx for i in range(width)]
        ys = [j / sy for j in range(height)]
        xi = [int(math.floor(x)) for x in xs]
        yi = [int(math.floor(y)) for y in ys]
        xf = [xs[i] - xi[i] for i in range(width)]
        yf = [ys[j] - yi[j] for j in range(height)]
        xf_s = [smoothstep(v) for v in xf]
        yf_s = [smoothstep(v) for v in yf]
        out = [[0.0 for _ in range(width)] for __ in range(height)]
        for j in range(height):
            for i in range(width):
                x0 = xi[i]
                y0 = yi[j]
                v00 = grid[y0][x0]
                v10 = grid[y0][x0 + 1]
                v01 = grid[y0 + 1][x0]
                v11 = grid[y0 + 1][x0 + 1]
                ix0 = v00 * (1 - xf_s[i]) + v10 * xf_s[i]
                ix1 = v01 * (1 - xf_s[i]) + v11 * xf_s[i]
                out[j][i] = ix0 * (1 - yf_s[j]) + ix1 * yf_s[j]
        return out

    noise = [[0.0 for _ in range(width)] for __ in range(height)]
    amplitude = 1.0
    frequency = scale
    max_amp = 0.0
    for _ in range(octaves):
        layer = single_layer(frequency, frequency)
        for j in range(height):
            for i in range(width):
                noise[j][i] += layer[j][i] * amplitude
        max_amp += amplitude
        amplitude *= persistence
        frequency *= 2
    # normalize
    minv = min(min(row) for row in noise)
    maxv = max(max(row) for row in noise)
    rng = maxv - minv if maxv > minv else 1.0
    for j in range(height):
        for i in range(width):
            noise[j][i] = (noise[j][i] - minv) / rng
    # convert to PIL Image('L')
    im = Image.new('L', (width, height))
    px = im.load()
    for j in range(height):
        for i in range(width):
            px[i, j] = int(round(noise[j][i] * 255))
    return im

# compatibility wrapper used by renderer
def value_noise(width, height, scale=8, octaves=4, persistence=0.5, seed=None):
    return value_noise_purepython(width, height, scale=scale, octaves=octaves, persistence=persistence, seed=seed)
