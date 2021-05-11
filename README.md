# shift-linkedlist
Shift a singly-linked-list by k steps. The shift operation should be done in place without needing extra space. Positive k means forward shift; negative k means backward shift.

Example: original llist: 0 -> 1 -> 2 -> 3 -> 4 -> 5; shifted by k=2: 4 -> 5 -> 0 -> 1 -> 2 -> 3; shifted by k=-2: 2 -> 3 -> 4 -> 5 -> 0 -> 1; shifted by k=8: 4 -> 5 -> 0 -> 1 -> 2 -> 3 (same as k=2 case, the net effective shift is 2).

Tips: In one pass O(n), find the list length and tail. In another pass O(~n/2) determine the new tail, aka, the break point. Then rearrange the llist accordingly. For the case of k larger than the actual length of the llist, shift operation is cycling the llist with a net effective shift.