#!/usr/bin/python

from turtle import *
import math

def ngon_interior_angle(n):
    return ((n-2) * 180.0) / n

def ngon_side_length(n, r):
    return math.sin(math.pi / 2.0 / n) * 2.0 * r

# v1 and v2 are indicies referencing how far around the circle they are
# the actual values don't matter, so long as they are accurate RELATIVE
# to one another.
def length_from_vert_to_another(n, r, v1, v2):
    theta = math.abs(v1 - v2) * (2.0 * math.pi / n)
    return 2.0 * r * math.sin(theta / 2.0)

def generate_ngon_verts(n, r, center):
    angle_segment = (2.0 * math.pi / n)

    return [
        (math.cos(angle_segment * i + (math.pi / 2.0)) * r + center[0],
         math.sin(angle_segment * i + (math.pi / 2.0)) * r + center[1])
        for i in range(n)
    ]

def draw_ngon(n, r, center):
    verts = generate_ngon_verts(n, r, center)
    goto(verts[0])

    down()
    begin_fill()

    for i in range(n):
        goto(verts[(i+1) % n])

    end_fill()
    up()


def draw_pattern(n, r, center):
    verts = generate_ngon_verts(n, r, center)
    goto(verts[0])

    down()
    begin_fill()

    cur_vert = 0
    cur_step = 1
    drawn_lines = set()
    while True:
        next_vert = (cur_vert + cur_step) % n
        cur_step = (cur_step + 1) % n
        goto(verts[next_vert])

        if next_vert != cur_vert and (cur_vert, next_vert) in drawn_lines:
            break
        drawn_lines.add((cur_vert, next_vert))
        cur_vert = next_vert

    end_fill()
    up()

def draw_pattern_2(n, r, center):
    verts = generate_ngon_verts(n, r, center)
    goto(verts[0])

    down()
    begin_fill()

    cur_vert = 0
    cur_step = 1
    drawn_lines = set()
    while True:
        next_vert = (cur_vert + cur_step) % n
        cur_step = (cur_step * 3) % n
        goto(verts[next_vert])

        if next_vert != cur_vert and (cur_vert, next_vert) in drawn_lines:
            cur_step = 1
            if next_vert + cur_step == 0:
                break
        if cur_step == 0:
            cur_step = 1

        drawn_lines.add((cur_vert, next_vert))
        cur_vert = next_vert

    end_fill()
    up()

up()
centers = generate_ngon_verts(12-3, 325, (0, 0))
for n in range(3, 12):
    center = centers[n-3]
    width(1)
    color('blue', 'yellow')
    #draw_ngon(n, 50, center)
    color('red', 'green')
    width(3)
    draw_pattern(n, 50, center)
done()
