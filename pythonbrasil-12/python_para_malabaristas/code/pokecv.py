#! /usr/bin/env python2
# -*- coding: utf-8 -*-

import cv2
import numpy as np

LEFT = 1
RIGHT = -1
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (0, 0, 255)


class Poke(object):
    """Draws a creature from given center point and radius"""

    def __init__(self, center_point, radius):
        self.center_point = center_point
        self.radius = radius

    def ear(self, side, offset=0):

        multiplier = side  # flip sides when drawing right ear
        circle_center = self.center_point
        circle_radius = self.radius

        point1x = circle_center[0] - (int(offset * circle_radius) +
                                      int(1.2 * circle_radius)
                                      ) * multiplier
        point1y = circle_center[1] - circle_radius  # target: 160

        point2x = circle_center[0] - int(0.5 * circle_radius) * multiplier
        point2y = circle_center[1] - int(0.85 * circle_radius)  # target: 170

        point3x = circle_center[0] - int(0.9 * circle_radius) * multiplier
        point3y = circle_center[1] - int(0.4 * circle_radius)  # target: 205

        points = np.array([[point1x, point1y],
                           [point2x, point2y],
                           [point3x, point3y]])
        # print side, points

        return points

    def tail(self):

        circle_center = self.center_point
        circle_radius = self.radius

        # tail
        p1x = circle_center[0]
        p1y = circle_center[1] + int(0.6 * circle_radius)
        p2x = circle_center[0] + int(1.1 * circle_radius)
        p2y = circle_center[1] + int(0.6 * circle_radius)
        p3x = circle_center[0] + int(1.1 * circle_radius)
        p3y = circle_center[1] + int(0.05 * circle_radius)
        p4x = circle_center[0] + int(2 * circle_radius)
        p4y = circle_center[1] - int(0.25 * circle_radius)
        p5x = circle_center[0] + int(2.2 * circle_radius)
        p5y = circle_center[1] + int(0.5 * circle_radius)
        p6x = circle_center[0] + int(1.5 * circle_radius)
        p6y = circle_center[1] + int(0.5 * circle_radius)
        p7x = circle_center[0] + int(1.1 * circle_radius)
        p7y = circle_center[1] + int(1 * circle_radius)
        p8x = circle_center[0]
        p8y = circle_center[1] + int(1 * circle_radius)

        points = np.array([[p1x, p1y],
                           [p2x, p2y],
                           [p3x, p3y],
                           [p4x, p4y],
                           [p5x, p5y],
                           [p6x, p6y],
                           [p7x, p7y],
                           [p8x, p8y]])
        return points

    def eye(self, side):

        center = self.center_point
        radius = self.radius

        black_circle_x = center[0] + int(0.4 * radius) * side
        black_circle_y = center[1] - int(0.4 * radius)
        black_circle_radius = int(0.18 * radius)

        white_circle_x = center[0] + int(0.39 * radius) * side
        white_circle_y = center[1] - int(0.45 * radius)
        white_circle_radius = int(0.06 * radius)

        return (black_circle_x, black_circle_y, black_circle_radius,
                white_circle_x, white_circle_y, white_circle_radius)

    def draw_eye(self, canvas, eye):

        cv2.circle(canvas, (eye[0], eye[1]), eye[2],
                   BLACK, thickness=-1)

        cv2.circle(canvas, (eye[3], eye[4]), eye[5],
                   WHITE, thickness=-1)

    def cheek(self, side):

        center = self.center_point
        radius = self.radius

        red_circle_x = center[0] + int(0.7 * radius) * side
        red_circle_y = center[1] + int(0.25 * radius)
        red_circle_radius = int(0.25 * radius)

        return (red_circle_x, red_circle_y, red_circle_radius)

    def draw_cheek(self, canvas, cheek):

        cv2.circle(canvas, (cheek[0], cheek[1]), cheek[2],
                   RED, thickness=-1)

    def draw_creature(self, canvas, color):

        circle_center = self.center_point
        circle_radius = self.radius

        # body
        cv2.circle(canvas, circle_center, circle_radius,
                   color, thickness=-1)  # filled
        # ears
        cv2.fillPoly(canvas, [self.ear(LEFT, 0.3)], color)
        cv2.fillPoly(canvas, [self.ear(RIGHT)], color)
        # tail
        cv2.fillPoly(canvas, [self.tail()], color)

        # left eye
        left_eye = self.eye(LEFT)
        self.draw_eye(canvas, left_eye)

        # right eye
        right_eye = self.eye(RIGHT)
        self.draw_eye(canvas, right_eye)

        # cheeks
        self.draw_cheek(canvas, self.cheek(LEFT))
        self.draw_cheek(canvas, self.cheek(RIGHT))

if __name__ == '__main__':

    circle_center = (320, 240)
    circle_radius = 80

    poke = Poke(circle_center, circle_radius)

    color = (0, 255, 255)  # yellow
    canvas = np.zeros((480, 640, 3), dtype='uint8')  # blank canvas
    poke.draw_creature(canvas, color)
    # show
    cv2.imshow("canvas", canvas)
    cv2.waitKey(0)
