{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2cd1eb0e-130b-418b-8fd1-a9551ca2dc2a",
   "metadata": {},
   "outputs": [],
   "source": [
    "months = [\n",
    "    \"\", \"January\", \"February\", \"March\", \"April\", \"May\", \"June\",\n",
    "    \"July\", \"August\", \"September\", \"October\", \"November\", \"December\"\n",
    "]\n",
    "\n",
    "# Read input from user\n",
    "month_num = int(input(\"Enter the month: \"))\n",
    "\n",
    "# Check if input is in valid range\n",
    "if 1 <= month_num <= 12:\n",
    "    print(f\"Month {month_num} is {months[month_num]}\")\n",
    "else:\n",
    "    print(\"Invalid month number! Please enter a number between 1 and 12.\")"
   ]
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
