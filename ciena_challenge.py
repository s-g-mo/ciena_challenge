'''
FUNCTION SET ciena_challenge.py

A set of functions which are each solutions to programming challenges I was
assigned by Ciena. I wasn't allowed to use any 3rd party libraries. 2 hour time
limit

Stephen Mosher Feb. 26, 2022
'''


'''
Warmup Exercise.

Given an array of integers, find the maximum (non-zero) integer NOT in the array.

Ex. [1,2,3] - the maximum element not in the array is 4
    [1,3,6,2,1,1] - the maximum element not in the array is 5
    [-1,-2] - the maximum element not in the array is 1
'''
def warmup(A):

  # If all the elements in the array are less than zero, return 1.
  less_than_zero = [element for element in A if element < 0]
  if len(less_than_zero) == len(A):
    return 1

  # Otherwise proceed with cases that have at least some positive elements.
  else:

    # Reduce the input array into a unique, sorted, list.
    unique_elements = list(set(A))

    # Trick to compute the forward difference b/w elements in the array.
    unique_elements_shifted = unique_elements[1:]
    diffs = [a - b for a,b in zip(unique_elements_shifted, unique_elements)]

    # If the differences b/w subsequent elements are all equal to one,
    # then the maximum integer not in the array is the length of the array + 1
    equal_one = [diff for diff in diffs if diff == 1]
    if len(equal_one) == len(diffs):  
      return len(A) + 1

    # However, if there's a gap somehwere (a difference > 1), the maximum
    # element not in the array is the last element that gives difference > 1, -1.
    else:
      idx = [(idx,diff) for (idx,diff) in enumerate(diffs) if diff !=1][0][-1]
      return unique_elements[idx] - 1

'''
Problem 1.

Given an integer N, return an array that contains N unique integers that sum to
zero.

'''
def problem1(N):
  # List to hold answer.
  answer = []
  
  # Two cases, first case, N is an even integer.
  if (N % 2) == 0:
    
    for i in range(0, N//2):
      answer.append(N-i)
    
    # Negative mirror of all but the first element.
    elements_to_mirror = answer[1:]
    negatives = [-element for element in elements_to_mirror]
    
    # Append the negatives.
    for negative in negatives:
      answer.append(negative)
    
    # Append negative N to balance N.
    answer.append(-N)
    
    # Check sum and length and return.
    assert (sum(answer) == 0)
    assert (len(answer) == N)
    print('(answer, sum, length of list)')
    return (answer, sum(answer), len(answer))
  
  # Second case, N is an odd integer
  elif (N % 2) != 0:
    
    for i in range(0,(N-1)//2):
      answer.append(N-i)
    
    # Negatives (balance all the elements in answer).
    elements_to_mirror = answer.copy()
    negatives = [-element for element in elements_to_mirror]
    
    for negative in negatives:
      answer.append(negative)
    
    # Append 0 such that we have N elements total.
    answer.append(0)
    
    # Check sum and length and return.
    print('(answer, sum, length of list)')
    assert (sum(answer) == 0)
    assert (len(answer) == N)
    return (answer, sum(answer), len(answer))

'''
Problem 2.

Given an integer N, return the maximum possible integer formed by deleting a 
single 5 from the integer.

'''
def problem2(N):

    # Check negative.
    if N < 0:

      # Convert to string and strip '-'
      N = int(str(N).strip('-'))

      # Split into digits.
      digits = [int(n) for n in str(N)]
      
      # Look for 5s.
      fives_in_number = [True for n in digits if n == 5]
      
      # If no 5s return as is. 
      if not fives_in_number:
        return N

      # If 5s in number find indices.
      idxs_of_5s = [idx for (idx,number) in enumerate(digits) if number == 5]

      # Compute all possible results of deleting a 5.
      results = []
      for idx in idxs_of_5s:
        numbers = digits.copy()
        result = digits[:idx] + digits[idx+1:]
        result = int(''.join(map(str, result)))
        results.append(result)

      # Tranform back to negative.
      results = [-result for result in results]

      # Return max result.
      return max(results)
     
    # Check positive.
    if N >= 0:

      # Split into digits.
      digits = [int(n) for n in str(N)]
  
      # Look for 5s.
      fives_in_number = [True for n in digits if n == 5]
  
      # If no 5s return as is. 
      if not fives_in_number:
        return N
  
      # If 5s in number find indices.
      idxs_of_5s = [idx for (idx,number) in enumerate(digits) if number == 5]
      
      # Compute all possible results of deleting a 5
      results = []
      for idx in idxs_of_5s:
        numbers = digits.copy()
        result = digits[:idx] + digits[idx+1:]
        result = int(''.join(map(str, result)))
        results.append(result)

    # Return max result.
    return max(results)


'''
Problem 3.

Ran out of time and didn't complete.
'''
