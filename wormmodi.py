import modi
import time
import random

angles_reset = 50
motor_list = [0, 1]
angles_array = [
 [0, 28, 14, 5, 0, -1, -2, -1, -1, -2, -3, -1],
 [-3, 22, 19, 7, 0, -1, -2, -2, -1, -2, -2, -1],
 [-6, 15, 24, 9, 1, -1, -2, -2, -2, -2, -2, -2],
 [-10, 10, 24, 14, 3, -1, -2, -2, -2, -2, -2, -2],
 [-14, 5, 18, 21, 5, 0, -2, -2, -2, -2, -2, -4],
 [-19, 0, 14, 23, 10, 0, -2, -3, -2, -2, -2, -5],
 [-24, -3, 10, 18, 18, 3, -2, -3, -3, -2, -2, -6],
 [-29, -8, 6, 16, 21, 8, 0, -3, -3, -3, -3, -4],
 [-34, -12, 3, 13, 18, 15, 1, -3, -4, -3, -3, -4],
 [-34, -18, 0, 10, 16, 19, 5, -2, -4, -4, -3, -5],
 [-22, -25, -4, 7, 14, 17, 13, 0, -4, -4, -4, -6],
 [-14, -27, -11, 4, 12, 16, 17, 3, -3, -5, -5, -7],
 [-5, -20, -20, 0, 10, 14, 15, 11, -1, -5, -5, -6],
 [1, -14, -24, -6, 7, 13, 15, 16, 1, -5, -6, -7],
 [9, -8, -19, -16, 2, 11, 14, 15, 10, -2, -6, -7],
 [15, -2, -14, -21, -1, 9, 13, 14, 10, 5, -5, -10],
 [21, 2, -11, -22, -7, 6, 13, 14, 10, 5, 0, -11],
 [28, 8, -7, -18, -16, 2, 11, 14, 11, 7, 4, -10],
 [35, 13, -2, -14, -20, -2, 9, 13, 12, 8, 4, -2],
 [37, 21, 1, -10, -16, -12, 5, 12, 13, 10, 5, 0],
 [26, 29, 7, -6, -14, -17, 0, 11, 13, 11, 7, 1],
 [17, 33, 12, -3, -12, -15, -8, 8, 13, 12, 8, 3],
 [11, 34, 15, 0, -9, -13, -14, 5, 12, 13, 10, 5],
 [5, 29, 22, 4, -7, -12, -12, -4, 10, 14, 11, 7],
 [0, 21, 29, 9, -3, -10, -11, -10, 7, 13, 13, 9],
 [-6, 16, 32, 12, -1, -8, -11, -9, -1, 12, 14, 11],
 [-12, 10, 29, 18, 2, -7, -10, -9, -7, 9, 14, 13],
 [-19, 3, 23, 26, 6, -4, -9, -9, -6, 1, 13, 15],
 [-25, -1, 17, 28, 12, -2, -8, -10, -6, 0, 7, 16],
 [-33, -8, 12, 23, 21, 1, -7, -10, -7, -1, 5, 11],
 [-39, -14, 6, 19, 26, 5, -5, -9, -8, -3, 3, 10],
 [-40, -20, 1, 16, 27, 10, -3, -9, -8, -4, 1, 8],
 [-40, -27, -3, 13, 23, 19, 0, -7, -9, -6, 0, 6],
 [-31, -34, -9, 8, 19, 24, 4, -6, -9, -7, -1, 4],
 [-22, -30, -23, 2, 17, 26, 9, -3, -8, -8, -3, 1],
 [-14, -26, -30, -3, 12, 22, 18, 0, -7, -8, -5, 0],
 [-7, -21, -27, -18, 6, 19, 24, 6, -4, -8, -6, -2],
 [0, -15, -24, -27, 0, 14, 21, 16, -1, -7, -7, -4],
 [5, -10, -22, -30, -6, 10, 19, 21, 2, -6, -8, -6],
 [11, -5, -18, -26, -19, 4, 16, 20, 13, -2, -8, -8],
 [18, 0, -13, -23, -26, -1, 12, 18, 14, 7, -6, -9],
 [25, 6, -9, -20, -24, -14, 7, 16, 15, 9, 2, -10],
 [32, 13, -4, -15, -22, -22, 2, 13, 16, 11, 3, -3],
 [31, 21, 1, -12, -20, -21, -10, 9, 15, 13, 6, -1],
 [19, 28, 7, -8, -17, -20, -18, 4, 14, 14, 9, 1],
 [10, 27, 15, -3, -14, -19, -17, -6, 11, 15, 11, 4],
 [0, 20, 24, 2, -11, -17, -17, -14, 7, 14, 13, 8],
 [-8, 13, 28, 7, -7, -15, -17, -14, -3, 12, 14, 10],
 [-16, 7, 26, 13, -4, -13, -16, -15, -11, 9, 14, 13],
 [-24, 0, 19, 22, 0, -11, -16, -15, -10, 0, 13, 15],
 [-30, -5, 14, 25, 5, -8, -15, -15, -11, -1, 7, 16],
 [-36, -11, 9, 25, 10, -5, -14, -15, -11, -3, 5, 12],
 [-44, -18, 4, 19, 19, -1, -12, -15, -13, -6, 2, 10],
 [-42, -25, -1, 15, 23, 2, -10, -15, -13, -7, 0, 8],
 [-43, -29, -5, 12, 25, 5, -7, -14, -14, -9, -1, 6],
 [-42, -33, -9, 9, 24, 9, -5, -13, -14, -10, -2, 4],
 [-42, -38, -14, 5, 18, 17, -2, -11, -14, -11, -4, 2],
 [-33, -43, -20, 0, 15, 21, 1, -9, -14, -12, -6, 0],
 [-25, -37, -32, -5, 11, 22, 6, -7, -13, -12, -8, -2],
 [-17, -32, -39, -12, 7, 18, 15, -3, -11, -13, -10, -4],
 [-10, -27, -35, -26, 0, 14, 20, 2, -9, -13, -11, -7],
 [-2, -20, -31, -34, -6, 10, 17, 11, -5, -12, -12, -9],
 [5, -14, -27, -32, -21, 3, 14, 17, 0, -10, -12, -11],
 [14, -7, -22, -30, -30, -2, 11, 16, 10, -6, -12, -12],
 [20, -1, -17, -28, -34, -8, 7, 13, 10, 3, -10, -13],
 [29, 6, -12, -25, -31, -21, 2, 11, 11, 5, -2, -15],
 [31, 14, -6, -21, -28, -29, -3, 9, 11, 7, 0, -8],
 [21, 24, 0, -16, -26, -27, -16, 4, 11, 9, 2, -6],
 [13, 28, 6, -12, -23, -26, -24, 0, 9, 10, 4, -3],
 [6, 26, 13, -6, -20, -25, -24, -12, 6, 10, 7, 0],
 [-1, 19, 23, 0, -15, -23, -24, -20, 2, 10, 8, 3],
 [-8, 13, 27, 4, -12, -21, -23, -20, -8, 8, 10, 6],
 [-15, 7, 26, 11, -7, -19, -22, -20, -16, 5, 10, 8],
 [-23, 0, 19, 20, -2, -16, -21, -21, -16, -4, 9, 10],
 [-29, -5, 14, 24, 2, -13, -20, -21, -16, -6, 2, 12],
 [-34, -11, 9, 24, 7, -10, -19, -21, -17, -8, 0, 8],
 [-42, -17, 4, 19, 17, -5, -17, -21, -18, -11, -2, 6],
 [-48, -23, -1, 14, 21, 0, -14, -20, -19, -13, -4, 4],
 [-49, -29, -5, 11, 23, 3, -12, -19, -19, -14, -6, 1],
 [-50, -36, -11, 7, 18, 13, -7, -18, -20, -16, -9, 0],
 [-40, -44, -17, 2, 14, 18, -3, -15, -19, -17, -11, -3],
 [-28, -39, -32, -4, 11, 21, 2, -12, -18, -18, -13, -6],
 [-17, -33, -39, -10, 7, 17, 12, -8, -17, -18, -15, -9],
 [-9, -28, -41, -17, 2, 14, 17, -4, -15, -18, -16, -11],
 [0, -21, -36, -30, -3, 10, 15, 7, -11, -18, -17, -13],
 [8, -14, -31, -37, -10, 6, 13, 13, -7, -16, -18, -15],
 [15, -8, -27, -39, -16, 2, 11, 12, 2, -14, -18, -17],
 [24, 0, -21, -34, -28, -3, 8, 11, 9, -10, -18, -19],
 [32, 6, -15, -30, -34, -9, 5, 10, 9, 0, -16, -19],
 [32, 15, -9, -25, -31, -22, 0, 9, 9, 2, -6, -21],
 [23, 26, -1, -19, -29, -30, -5, 7, 9, 4, -4, -13],
 [17, 30, 4, -14, -26, -33, -10, 4, 9, 6, -2, -11],
 [12, 30, 12, -9, -23, -30, -21, 0, 8, 7, 0, -8],
 [6, 24, 24, -2, -19, -27, -28, -5, 6, 8, 3, -5],
 [0, 18, 28, 5, -14, -25, -27, -16, 2, 8, 5, -1],
 [-7, 11, 24, 18, -7, -21, -26, -24, -2, 6, 6, 1],
 [-13, 5, 19, 25, 0, -17, -24, -24, -13, 3, 7, 4],
 [-19, 0, 16, 27, 5, -13, -22, -23, -15, -5, 7, 7],
 [-26, -6, 11, 23, 17, -7, -20, -22, -17, -8, 0, 8],
 [-32, -12, 5, 18, 23, -1, -16, -22, -19, -11, -2, 4],
 [-36, -16, 1, 15, 25, 3, -13, -20, -19, -13, -4, 3],
 [-43, -22, -3, 11, 21, 14, -8, -19, -20, -15, -7, 0],
 [-41, -30, -8, 7, 18, 20, -3, -16, -20, -17, -10, -2],
 [-29, -36, -13, 3, 15, 23, 0, -13, -19, -18, -12, -4],
 [-20, -36, -20, 0, 12, 19, 11, -9, -18, -19, -14, -7],
 [-10, -29, -30, -6, 8, 17, 18, -4, -16, -19, -16, -10],
 [-1, -23, -35, -12, 4, 14, 16, 6, -12, -19, -17, -12],
 [7, -15, -29, -25, -1, 11, 15, 14, -8, -17, -18, -15],
 [15, -8, -24, -31, -7, 7, 14, 13, 2, -14, -19, -17],
 [22, -1, -20, -33, -13, 3, 12, 13, 10, -11, -18, -18],
 [31, 6, -14, -27, -24, -1, 9, 13, 10, 0, -16, -19],
 [39, 13, -8, -23, -29, -6, 7, 12, 10, 2, -7, -21],
 [39, 22, -2, -19, -26, -18, 2, 11, 11, 4, -5, -14],
 [30, 32, 5, -13, -23, -25, -2, 9, 11, 6, -2, -12],
 [22, 35, 12, -8, -21, -28, -7, 6, 11, 8, 0, -9],
 [14, 29, 25, -1, -17, -25, -18, 2, 10, 9, 3, -5],
 [6, 24, 32, 5, -12, -22, -24, -2, 8, 10, 5, -2],
 [0, 18, 33, 12, -8, -19, -22, -13, 4, 10, 7, 0],
 [-9, 12, 27, 24, -1, -15, -21, -20, 0, 8, 8, 3],
 [-16, 5, 22, 30, 4, -11, -19, -19, -9, 6, 9, 6],
 [-22, 0, 18, 31, 10, -7, -16, -19, -16, 3, 9, 8],
 [-30, -7, 13, 26, 21, -2, -14, -18, -16, -6, 7, 10],
 [-37, -13, 7, 22, 27, 3, -11, -17, -16, -8, 0, 11],
 [-43, -19, 2, 18, 29, 8, -8, -16, -16, -10, -1, 6],
 [-45, -27, -3, 14, 25, 18, -4, -14, -16, -12, -4, 4],
 [-35, -36, -9, 9, 21, 24, 0, -12, -16, -13, -6, 1],
 [-27, -40, -16, 5, 19, 27, 5, -9, -15, -14, -8, 0],
 [-19, -34, -29, -1, 14, 23, 16, -4, -14, -15, -10, -4],
 [-12, -28, -36, -8, 10, 20, 22, 0, -11, -15, -12, -6],
 [-3, -22, -32, -23, 3, 17, 21, 12, -7, -14, -14, -9],
 [4, -15, -28, -31, -3, 12, 19, 19, -2, -12, -14, -11],
 [10, -9, -24, -34, -10, 8, 17, 18, 7, -10, -15, -13],
 [19, -2, -19, -30, -23, 1, 14, 17, 15, -5, -13, -15],
 [27, 4, -14, -26, -30, -4, 10, 16, 15, 5, -11, -15],
 [36, 12, -8, -22, -27, -17, 5, 15, 15, 8, -1, -17],
 [39, 21, -1, -17, -25, -25, 0, 12, 15, 10, 1, -8],
 [30, 31, 5, -13, -23, -24, -13, 8, 15, 12, 4, -5],
 [22, 37, 12, -7, -19, -23, -21, 3, 13, 14, 7, -2],
 [16, 35, 19, -2, -16, -22, -26, 0, 11, 14, 9, 1],
 [9, 29, 29, 4, -12, -21, -24, -12, 7, 14, 11, 4],
 [1, 22, 33, 11, -7, -18, -22, -20, 3, 12, 12, 7],
 [-6, 15, 29, 24, -1, -15, -21, -20, -8, 9, 13, 10],
 [-13, 8, 24, 30, 5, -11, -19, -19, -11, 0, 13, 13],
 [-19, 2, 20, 32, 10, -8, -18, -19, -12, -2, 6, 15],
 [-28, -4, 15, 27, 22, -2, -15, -19, -14, -5, 3, 10],
 [-35, -11, 9, 23, 28, 2, -12, -18, -16, -8, 1, 9],
 [-40, -16, 4, 20, 30, 7, -9, -17, -16, -10, -1, 7],
 [-43, -24, -1, 16, 26, 19, -4, -15, -17, -12, -4, 4],
 [-33, -34, -7, 11, 22, 25, 0, -12, -16, -14, -6, 1],
 [-25, -37, -14, 6, 20, 28, 5, -10, -16, -14, -8, -1],
 [-18, -37, -20, 1, 17, 24, 16, -5, -15, -15, -10, -3],
 [-11, -30, -31, -4, 12, 21, 23, 0, -12, -15, -12, -6],
 [-3, -24, -35, -11, 8, 19, 21, 10, -9, -15, -14, -9],
 [4, -16, -30, -25, 1, 15, 20, 19, -4, -13, -15, -11],
 [11, -10, -25, -31, -5, 11, 18, 18, 6, -11, -15, -14],
 [21, -1, -20, -28, -19, 5, 15, 18, 15, -6, -14, -15],
 [29, 5, -14, -25, -27, -1, 12, 17, 15, 5, -12, -16],
 [36, 11, -8, -22, -30, -7, 9, 16, 15, 7, -3, -18],
 [39, 20, -2, -18, -26, -19, 4, 14, 16, 9, 0, -10],
 [29, 30, 4, -13, -23, -25, -1, 12, 15, 11, 2, -7],
 [21, 35, 11, -8, -20, -24, -13, 8, 15, 13, 5, -4],
 [14, 34, 19, -2, -16, -22, -21, 3, 13, 14, 8, 0],
 [6, 27, 29, 4, -12, -20, -20, -9, 10, 15, 11, 3],
 [0, 20, 34, 10, -8, -17, -20, -16, 6, 14, 12, 6],
 [-7, 14, 33, 16, -3, -15, -19, -16, -4, 12, 14, 9],
 [-16, 7, 26, 27, 2, -12, -17, -17, -13, 8, 14, 12],
 [-22, 1, 21, 31, 7, -8, -16, -17, -12, 0, 13, 14],
 [-28, -4, 16, 31, 13, -5, -15, -16, -12, -3, 6, 16],
 [-36, -11, 11, 26, 23, 0, -12, -16, -13, -5, 4, 11],
 [-42, -17, 5, 21, 28, 4, -10, -15, -14, -7, 1, 9],
 [-43, -23, 0, 18, 29, 9, -7, -14, -14, -9, 0, 7],
 [-45, -30, -5, 14, 25, 19, -2, -13, -15, -11, -3, 5],
 [-35, -39, -11, 8, 21, 25, 1, -11, -15, -12, -5, 2],
 [-27, -35, -26, 2, 18, 27, 7, -7, -14, -13, -7, 0],
 [-19, -31, -35, -5, 13, 23, 18, -3, -12, -14, -9, -3],
 [-12, -27, -38, -11, 8, 20, 23, 1, -10, -13, -11, -5],
 [-5, -22, -34, -26, 1, 16, 21, 13, -6, -13, -12, -8],
 [0, -16, -29, -33, -5, 11, 19, 20, -1, -11, -13, -10],
 [8, -10, -25, -31, -20, 5, 16, 19, 11, -7, -13, -12],
 [15, -3, -19, -28, -29, -1, 13, 18, 12, 1, -12, -14],
 [23, 3, -14, -25, -28, -16, 7, 16, 14, 11, -10, -12],
 [31, 10, -8, -21, -26, -25, 1, 13, 15, 11, -3, -8],
 [30, 19, -2, -17, -24, -24, -12, 9, 15, 12, 1, -6],
 [19, 27, 4, -12, -21, -24, -20, 4, 14, 13, 5, -3],
 [11, 30, 9, -8, -18, -23, -25, 0, 12, 14, 8, 0],
 [4, 26, 16, -3, -16, -22, -23, -11, 8, 14, 10, 3],
 [-4, 18, 24, 2, -12, -20, -23, -19, 3, 12, 12, 6],
 [-11, 12, 28, 7, -9, -18, -22, -19, -7, 10, 13, 9],
 [-19, 5, 25, 13, -5, -16, -20, -19, -15, 7, 13, 11],
 [-27, -1, 19, 22, 0, -13, -19, -19, -14, -2, 12, 14],
 [-33, -7, 13, 25, 4, -10, -18, -19, -15, -4, 5, 15],
 [-39, -13, 9, 25, 9, -7, -17, -19, -15, -6, 3, 11],
 [-46, -20, 3, 19, 18, -3, -15, -19, -16, -9, 0, 9],
 [-45, -27, -2, 15, 22, 0, -12, -18, -17, -11, -2, 7],
 [-44, -32, -7, 11, 23, 5, -10, -17, -17, -12, -4, 4],
 [-44, -38, -13, 6, 18, 15, -6, -16, -18, -14, -6, 1],
 [-35, -44, -18, 1, 15, 19, -2, -14, -18, -15, -8, 0],
 [-28, -39, -32, -4, 11, 21, 3, -11, -17, -16, -10, -3],
 [-19, -34, -40, -11, 7, 17, 13, -6, -15, -17, -13, -6],
 [-12, -30, -42, -17, 2, 14, 18, -2, -13, -17, -14, -8],
 [-4, -24, -37, -31, -4, 10, 15, 8, -10, -16, -15, -11],
 [2, -17, -33, -38, -11, 6, 13, 14, -5, -15, -16, -13],
 [12, -10, -27, -35, -25, 0, 11, 13, 4, -11, -16, -15],
 [20, -3, -21, -31, -33, -6, 7, 12, 12, -7, -15, -16],
 [26, 2, -16, -29, -36, -12, 4, 11, 11, 2, -13, -17],
 [35, 10, -10, -25, -33, -24, -1, 9, 10, 4, -3, -19],
 [37, 18, -4, -21, -30, -31, -6, 6, 10, 6, -1, -11],
 [27, 29, 2, -16, -27, -30, -19, 2, 10, 8, 1, -8],
 [19, 32, 11, -10, -23, -28, -27, -2, 8, 9, 3, -5],
 [11, 27, 24, -3, -19, -27, -26, -15, 4, 9, 6, -1],
 [3, 21, 30, 4, -14, -24, -26, -23, 0, 8, 7, 2],
 [-4, 16, 31, 11, -10, -22, -25, -22, -11, 6, 9, 5],
 [-12, 9, 25, 23, -3, -18, -24, -23, -19, 2, 8, 7],
 [-19, 2, 20, 28, 3, -14, -22, -23, -19, -7, 7, 9],
 [-29, -5, 14, 24, 16, -8, -20, -23, -20, -10, 0, 10],
 [-37, -12, 8, 21, 23, -2, -17, -23, -21, -13, -3, 5],
 [-43, -18, 3, 17, 26, 2, -14, -22, -22, -15, -6, 2],
 [-45, -26, -2, 14, 23, 14, -9, -20, -22, -17, -9, 0],
 [-47, -33, -8, 9, 19, 21, -4, -18, -22, -19, -11, -3],
 [-37, -41, -14, 4, 17, 24, 0, -15, -21, -20, -13, -5],
 [-29, -44, -22, 0, 14, 21, 12, -10, -20, -21, -16, -8],
 [-22, -38, -34, -7, 9, 18, 19, -5, -17, -21, -18, -11],
 [-14, -32, -40, -14, 5, 16, 17, 6, -14, -20, -19, -14],
 [-5, -25, -36, -29, -1, 12, 17, 15, -9, -18, -20, -17],
 [2, -18, -32, -36, -9, 8, 15, 14, 3, -15, -20, -19]
]

if __name__ == "__main__":
    
    # bundle = modi.MODI(1)
    bundle = modi.MODI(
        conn_type='ble',
        network_uuid="CDB67A2D"
    )    
    print("===============")

    ultrasonic = bundle.ultrasonics[0]
    motor = [bundle.motors[0], bundle.motors[1]]

    for i in motor_list:
        motor[i].first_degree = angles_reset
        motor[i].second_degree = angles_reset
    print("All Motor : 50 degree")
   
    while True:
        ran = []
        for i in angles_array:
            ran.append(random.randrange(0, len(angles_array)))
        del ran[0:2*len(angles_array)//3]
        ran_set = set(ran)
        ran = list(ran_set)
        ran.sort()
        ran_index = 0

        for i in angles_array:
            print("RANDOM : ", ran)
            print("angled_array : ", angles_array.index(i))
            if ran_index < len(ran) and ran[ran_index] == angles_array.index(i):
                for ii in range(0, 3):
                    print("1")
                    motor[0].first_degree = 35
                    motor[0].second_degree = 35
                    motor[1].first_degree = 65
                    motor[1].second_degree = 65
                    time.sleep(0.05)

                    print("2")
                    motor[0].first_degree = 65
                    motor[0].second_degree = 35
                    motor[1].first_degree = 35
                    motor[1].second_degree = 65
                    time.sleep(0.05)

                    print("3")
                    motor[0].first_degree = 65
                    motor[0].second_degree = 65
                    motor[1].first_degree = 35
                    motor[1].second_degree = 35 
                    time.sleep(0.05)

                    print("4")
                    motor[0].first_degree = 35
                    motor[0].second_degree = 65
                    motor[1].first_degree = 65
                    motor[1].second_degree = 35 
                    time.sleep(0.05)
                ran_index += 1

            if ultrasonic.distance < 5 :
                for ii in range(0, 2):
                    print("Ultra Sonic")
                    motor[0].first_degree = 65
                    motor[0].second_degree = 65
                    motor[1].first_degree = 35
                    motor[1].second_degree = 35
                    time.sleep(0.05)

                    motor[0].first_degree = 65
                    motor[0].second_degree = 35
                    motor[1].first_degree = 35
                    motor[1].second_degree = 65
                    time.sleep(0.05)

                    motor[0].first_degree = 35
                    motor[0].second_degree = 35
                    motor[1].first_degree = 65
                    motor[1].second_degree = 65 
                    time.sleep(0.05)

                    motor[0].first_degree = 35
                    motor[0].second_degree = 65
                    motor[1].first_degree = 65
                    motor[1].second_degree = 35 
                    time.sleep(0.05)

            print("")
            motor[0].first_degree = 50 + i[0]//(1.3)
            motor[0].second_degree = 50 + i[1]//(1.3)
            motor[1].first_degree = 50 + i[2]//(1.3)
            motor[1].second_degree = 50 + i[3]//(1.3)
            time.sleep(0.1)