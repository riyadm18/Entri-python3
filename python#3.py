{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d08f0370-265e-4d22-89a3-638504b0e633",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter first number:  2\n",
      "Enter second number:  7\n",
      "Enter third number:  9\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The greatest number is: 9\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"Enter first number: \"))\n",
    "b = int(input(\"Enter second number: \"))\n",
    "c = int(input(\"Enter third number: \"))\n",
    "\n",
    "if a >= b and a >= c:\n",
    "    print(\"The greatest number is:\", a)\n",
    "elif b >= a and b >= c:\n",
    "    print(\"The greatest number is:\", b)\n",
    "else:\n",
    "    print(\"The greatest number is:\", c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "04913381-f5a9-4a7f-84e9-73c9d11e1099",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Factorial of 7 is 5040\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter a number: \"))\n",
    "factorial = 1\n",
    "\n",
    "for i in range(1, num + 1):\n",
    "    factorial *= i\n",
    "\n",
    "print(\"Factorial of\", num, \"is\", factorial)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8acbdcf5-2d8a-4008-82c3-192cef8d2499",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  42\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Reversed number is: 24\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter a number: \"))\n",
    "reverse = 0\n",
    "\n",
    "while num > 0:\n",
    "    digit = num % 10\n",
    "    reverse = reverse * 10 + digit\n",
    "    num //= 10\n",
    "\n",
    "print(\"Reversed number is:\", reverse)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "92b73c6a-582a-41a4-bbcd-388b0543d7e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  7\n",
      "Enter how many multiples you want:  7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Multiples of 7 are:\n",
      "7\n",
      "14\n",
      "21\n",
      "28\n",
      "35\n",
      "42\n",
      "49\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter a number: \"))\n",
    "limit = int(input(\"Enter how many multiples you want: \"))\n",
    "\n",
    "print(\"Multiples of\", num, \"are:\")\n",
    "for i in range(1, limit + 1):\n",
    "    print(num * i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9c696934-a744-4dc1-9126-5a28f9204052",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      ": TRUE\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "TRUE\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      ": LOWER\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LOWER\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      ": DONE\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "DONE\n"
     ]
    }
   ],
   "source": [
    "while True:\n",
    "    user_input = input(\":\")\n",
    "    print(user_input)\n",
    "    if user_input.lower() == 'done':\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c368a850-e3a5-4ee2-9e6f-ac302a0a2e6d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "Fizz\n",
      "4\n",
      "Buzz\n",
      "Fizz\n",
      "7\n",
      "8\n",
      "Fizz\n",
      "Buzz\n"
     ]
    }
   ],
   "source": [
    "for i in range(1, 11):\n",
    "    if i % 3 == 0 and i % 5 == 0:\n",
    "        print(\"FizzBuzz\")\n",
    "    elif i % 3 == 0:\n",
    "        print(\"Fizz\")\n",
    "    elif i % 5 == 0:\n",
    "        print(\"Buzz\")\n",
    "    else:\n",
    "        print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ff3cd85b-c684-4145-9e67-6c3bfb18a2cc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5 4 3 2 1 \n",
      "4 3 2 1 \n",
      "3 2 1 \n",
      "2 1 \n",
      "1 \n"
     ]
    }
   ],
   "source": [
    "for i in range(5, 0, -1):\n",
    "    for j in range(i, 0, -1):\n",
    "        print(j, end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "949353d5-a2ee-4bb3-824d-b2aab0b86463",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
