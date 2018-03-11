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
    print("after adding 1:", m, sep='\n')
    b = b + 20
    m = m + b
    print("after adding matrix b:", m, sep='\n')
    m.randomize()
    print("after randomize :", m, sep='\n')
    m *= 3
    print("after multiply by 3 :", m, sep='\n')


if __name__ == "__main__":
    main()
