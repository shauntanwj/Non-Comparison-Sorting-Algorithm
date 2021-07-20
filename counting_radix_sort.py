# Question 1: Transaction Interval

def maximum(lst):
    
    """
    Input: a list
    Output: maximum item of the list
    
    This function is to find the maximum item of the input list.
    It loops through the list and compare and find the maximum item in the list lastly return the maximum item.
    
    Example: maximum([3,1,16,6,1]) return 16
    
    Best and Worst Time complexity: O(N) where N is the length of the input list.
    Space Complexity: O(N) where N is the size/length of the input list.
    Axilliary Space Complexity: O(1)
    """
    
    max_item = lst[0]       
    for item in lst:
        if item > max_item:
            max_item = item
    return max_item

def radix_sort(new_list):
    
    """
    Input: a list of integers
    Output: a sorted integer list
    
    This function is to sort a given list asscendingly. The function will first find the greatest integer in the list. Then, 
    it will create a count_array of 0 to 9 and then loop through every column of every integer in the list. 
    To get the number of the current column, I've used the formula (number//base^column)%base. 
    Then base on the number of the column, append them into the respective bucket in count_array. And then loop through
    the count_array and update the list. This process will go repeat for the number of column for the greatest integer in the list. 
    
    Example: radix_sort([6,2,15,9,1,4]) return [1,2,4,6,9,15]
    
    Time Complexity: O(NK) where N is the number of element in the list and K is the largest number of digits in the list.
    Space Complexity: O(NK) where N is the number of element and K is the largest number of digits in the list.
    Auxiliary Space Complexity: O(N) where N is the number of element in the list.
    """
    
    # check if the list is empty, if it is then returnempty list
    if len(new_list) == 0:
        return new_list
     
    # find the maximum item in the list
    max_item = maximum(new_list) 
    
    # creat a count array of length 10, [0...9]
    # but need to have another loop to create empty nested list because if not it will point to the same list
    count_array = [None]*(10)  
    for i in range(len(count_array)): 
        count_array[i] = []
    
    
    # loop each column of every digits in the list, starting from the rightmost column to leftmost column
    # then add the digits into the count_array based on the number on the respective column
    base = 10
    column = 0
    for i in range(len(str(max_item))): 
        for item in range(len(new_list)): 
            number = new_list[item]
            pos = ((number//(base**column))%base) 
            count_array[pos].append(number)
    
    
        # updating the list with the latest position for each digit
        index = 0  # first position of the new_list
        for a in range(len(count_array)): 
            for b in count_array[a]:   
                new_list[index] = b
                index = index + 1
            count_array[a] = []
        column += 1     # after updating the list go to the next column 
    return new_list

def best_interval(transactions, t):
    
    """
    Input: a unsorted non-negative integer of list 'transactions' and a non negative integer 't'
    Output: (best_t, count) 'best_t' is a tuple containing the best-interval and 't' the number of elements in the interval of length t starting at best_t
    
    This function will first sort the unsorted list transactions by calling radix_sort and then starting from the first integer 
    in the sorted list, loop through each of them and find the best_t and count by using 2 pointer lower_bound and upper_bound.
    lower_bound will point to the lower-bound of the current interval, and then upper bound will point to the upper-bound 
    of the current interval. Thus for each iteration the function will find the upper-bound of that current interval, 
    then compute the count using the 2 pointer, (upper_bound - lower_bound) + 1. And then it will check with the max_count to see 
    whether its the best interval, if it is then, max_count will equal to count and best_t will be the upper_bound integer minus t. 
    start is the start time for the interval and end is the end time is the end time for the interval which is equal to start+t.
    start_index will contain all the different transactions index with no duplicate so that the start time do not have to run the same 
    transaction twice. 
    
    Time Complexity: O(NK) where N is the number of element in transactions, K isthe greatest number of digits in transactions. 
    Space Complexity: O(N) where N is the number of element in transactions
    Auxiliary Space Complexity: O(N) where N is the number of element in transactions 
    """
    
    transactions = radix_sort(transactions)
    count = 0
    max_count = 0
    best_t = 0
    
    # if the transaction is empty then return (0,0)
    if len(transactions) == 0:
        return(best_t, max_count)
    
    start = transactions[0]
    end = start + t
    start_index = []
    upper_bound = 0
    lower_bound = 0

    for i in range(len(transactions)):
        if i+1 != len(transactions): 
            # if i and i+1 is not equal then append i+1 into the start_index list
            if transactions[i] != transactions[i+1]:
                start_index.append(i+1)          
        if transactions[i] >= start and transactions[i] <= end:  # if the integer is within the interval change the upper_bound
            upper_bound = i
        else:
            count = (upper_bound - lower_bound) + 1
            # check if the count is greater than the max_count
            if count > max_count:
                max_count = count
                best_t = transactions[upper_bound] - t
                if best_t < 0:
                    best_t = 0
            # reset the count and get the new lower_bound index, start time and end time
            count = 0
            lower_bound = start_index.pop(0)
            start = transactions[lower_bound]
            end = start + t
            if transactions[i] <= end:
                upper_bound = i
    count = (upper_bound - lower_bound) + 1
    if count > max_count:
        max_count = count
        best_t = transactions[upper_bound] - t
        if best_t < 0:
            best_t = 0  
    return(best_t, max_count) 



# Question 2: Anagrams

def radix_sort_string(wrd):
    
    """
    Input: a string
    Output: a sorted string in alphabetical order
    
    This function is to sort a string in alphabetical order.
    It will first create a count_array(bucket) of length 26, [a-z]. Then it will loop through each alphabet to get the position to be
    appended into the count_array. Then it will loop through each count_array and add the alphabet in the list, sorted_wrd. 
    Last, used "".join() to join all the alphabet in the list. 
    
    Example: radix_sort_string("zlaaaa") return "aaaalz"
    
    Time Complexity: O(MN) where M is the length of the string, N is the length of count_array
                     since N is always constane equals to 26 we can say that the complexity is
                     O(M).
    Space Complexity: O(M) where M is the length of the string
    Auxiliary Space Complexity: O(M) where M is the length of the word
    """
    
    # create a bucket of length 26, [a-z]
    count_array = [None]*(26)  
    for i in range(len(count_array)): 
        count_array[i] = []
     
    # ord(alphabet) will get the ascii code of the character then minus 97 since ascii 97 is 'a' which will be in the first bucket
    for j in range(len(wrd)):
        alphabet = wrd[j]
        alpha_numb = ord(alphabet) - 97     
        count_array[alpha_numb].append(alphabet)
    
    # create an empty list and loop through the count_array and add the characters in the list 
    sorted_wrd = []
    for i in range(len(count_array)):
        for j in count_array[i]:
            sorted_wrd+=j

    return("".join(sorted_wrd)) # used .join to join the characters in sorted_wrd together

def longest_length_string(lst):
    
    """
    Input: a list of strings
    Output: the maximum length of the string in the list
    
    This function is to find the longest string in the list and return it's length.
    It will loop through the list and compare it with the current max_length string in the list. 
    
    Example: longest_length_string(["sim", "l", "dtg", "harlooo"]) return 7
    
    Time Complexity: O(N) where N is the length of the list
    Space Complexity: O(N) where N is the length of the input list
    Auxiliary Space Complexity: O(1)
    """
    
    # if the list is empty then return 0, since there's no strings in the list
    if len(lst) == 0:  
        return 0
    
    max_length = len(lst[0])
    for item in lst:
        if len(item) > max_length:
            max_length = len(item)
    return max_length

def radix_sort_lst_strings(lst):
    
    """
    Input: a list of strings
    Output: a tuple with the first element is a list of strings which is sorted based on 
            the length and alphabetical order based on each alphabetically sorted string
            and the second element is the a list of strings which is sorted based 
            on the length and each string is alphabetically sorted.
    
    This function will first take in a list and then loop through each string to sort it alphabetically, and then 
    based on the alphabatically sorted string, sort the whole list based on the length and in alphabetical order
    based on each alphabatically sorted string. Last return two list which is the list with sorted string and original string.
    This enable me to keep track of the original word easier, just have to get the index of the word, since both list is sorted
    based on the alphabetical sorted string, one contain the string which is alphabetically sorted, another with the original string. 
    
    Example: radix_sort_lst_strings([spot, tops, cat, zlaa, dad]) will first alphabetically sort to [opst, opst, act, aalz, add] -> 
             then lastly after sorting the alphabetical sorted string, return ([add, act, aalz, opst, opst], [dad, cat, zlaa, spot, tops])
    
    Time Complexity: O(LM + LN) where L is the length of the list, M is the longest string, N is the length of count_array
                     but since we know that count_array is always going to be O(27) which is a constant, thus 
                     the time complexity can be said to be O(LM).
                     
    Space Complexity: O(LM) where L is length of the list and M is the longest string.
    
    Auxiliary Space Complexity: O(L) where L is the length of the list
    """
    
    # find the length of the longest string in the list
    frequency = longest_length_string(lst)
    
    # anagram_list would later return all the list of string which is sorted alphabetically 
    anagram_list = []
    
    # create count array of length 27 because if the string reach a column that it doesn't have then add it to the first bucket
    count_array = [None]*(27)  
    for i in range(len(count_array)): # O(M)
        count_array[i] = []
       
    # loop through the input list and for each string call radix_sort_string to get sort each string alphabetically
    for i in range(len(lst)):
        anagram_list.append(radix_sort_string(lst[i]))
    
    # This part of the code will loop for frequency time, and then loop each string in the anagram_list
    # word is the original string which is not sorted alphabetically
    # ana_word is the string which has sorted alphabetically
    # if the column is smaller than the length of the string, then it means it exist for that column, 
    # then find the position of that alphabet and append it into count_array
    # else it means that that particular string doesn't have that column thus add it into the first bucket
    # in the count_array, it will store the sorted string first and then the original string
    
    col = -1  # col is column which starts from the rightmost alphabet of the word 
    for i in range(frequency):       
        for j in range(len(anagram_list)):
            word = lst[j]          
            ana_word = anagram_list[j]     
            if abs(col)-1 < len(ana_word):   
                alphabet = ana_word[col]
                
                # plus 1 is because the first bucket is not for 'a', 
                # the first bucket is for the string that the particular column does not exist
                alpha_numb = ord(alphabet) - 97 + 1  
                count_array[alpha_numb].append(ana_word)
                count_array[alpha_numb].append(word)
                
            else:
                count_array[0].append(ana_word)
                count_array[0].append(word)
    
  
        # update the anagram_list and original list  
        index = 0  
        for i in range(len(count_array)):  # get the item constant 
            # here it will loop the nested list with increment of 2
            # first string in the nested list is the alphabetical sorted string
            # second string in the nested list is the original word
            for j in range(0,len(count_array[i]),2):   
                anagram_list[index] = count_array[i][j]
                lst[index] = count_array[i][j+1]
                index = index + 1
            count_array[i] = [] 
        
        col -= 1

    return(lst,anagram_list)

def words_with_anagrams(list1, list2):
    
    """
    Input: 2 list of strings, list1 and list2
    Output: a list of strings in list1 which have at least one anagram in list2
    
    This function will first call radix_sort_lst_strings for list1 and list2 to get the tuple,
    then ori_1 is the list containing unsorted string of list1 but is sorted based on length and the alphabetical order of the sorted strings
    ana_1 is the list containing sorted string of list1 and is sorted based on length and the alphabetical order of the sorted strings
    ana_2 is the list containing sorted string of list2 and is sorted based on length and the alphabetical order of the sorted strings.
    After that it will loop through ana_1 and compare each string with ana_2 if there is then get the index of the string in ana_1 
    to get the orginal word in ori_1 and append it into the output_list
    
    Time Complexity: O(L1M1+L2M2) where L1 is the length of the list1, M1 is the number of characters in the longest string in list1
                                        L2 is the length of the list2, M2 is the number of characters in the longest string in list2
                                        
    Space Complexity: O(L1+L2) where L1 is the length of the list1, L2 is the length of the list2
    
    Auxiliary Space Complexity: O(L1) where L1 is the length of the list1                                
    """
    
    lst_a = radix_sort_lst_strings(list1)
    lst_b = radix_sort_lst_strings(list2)
    ori_1 = lst_a[0]
    ana_1 = lst_a[1]
    ana_2 = lst_b[1]
    output_list=[]
    
    # i is a pointer for ana_1
    # j is a pointer for ana_2
    i = 0
    j = 0

    
    while i < len(ana_1):
        # if the previous item is equal to the current item in ana_1 
        # and equal to the previous item in ana_2 then add the current item 
        if ana_1[i-1] == ana_1[i] and ana_1[i-1] == ana_2[j-1]:
            output_list.append(ori_1[i])
            i+=1
        elif i < len(ana_1) and j < len(ana_2):
            if len(ana_1[i]) == len(ana_2[j]):  
                if ana_1[i] == ana_2[j]:
                    output_list.append(ori_1[i])
                    j+=1
                    i+=1
                elif ana_1[i] > ana_2[j]:  # if the current item in ana_1 is greater than the current item in ana_2 than j plus 1
                    j+=1
                else:   # else it means that the current item in ana_1 is smaller than the current item in ana_2 than j plus 1
                    i+=1
            elif len(ana_1[i]) > len(ana_2[j]):  # if the length of the current string in ana_1 is greater than the one in ana_2 then j pointer +1
                j+=1
            elif len(ana_1[i]) < len(ana_2[j]):  # if the length of the current string in ana_1 is smaller than the one in ana_2 then i pointer +1
                i+=1
        else:
            break
    return(output_list)













