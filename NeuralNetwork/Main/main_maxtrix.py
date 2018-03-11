# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main_maxtrix.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fbenneto <f.benneto@student.42.fr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/03/11 18:03:58 by fbenneto          #+#    #+#              #
#    Updated: 2018/03/11 18:03:58 by fbenneto         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# from numpy import *
from Matrix import Matrix


def main():
    m = Matrix(5, 2)
    b = Matrix(5, 2)
    print("show matrix :", m, sep='\n')
    m += 10
    print("after adding 10:", m, sep='\n')
    b = b + 20
    m = m + b
    print("after adding matrix b:", m, sep='\n')
    m.randomize()
    print("after randomize :", m, sep='\n')
    m *= 3
    print("after multiply by 3 :", m, sep='\n')
    d = Matrix(2, 3)
    g = Matrix(3, 3)
    g.matrix = [
        [3, 5, 8],
        [2, 6, 6],
        [7, 9, 4]
    ]
    d += 5
    h = d * g
    print("after multiply d :\n{}\nby g :\n{}\nres :\n{}".format(d, g, h))
    h = g.transpose()
    print("after transpose :\n{}".format(h))


if __name__ == "__main__":
    main()
