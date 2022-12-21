def additional_seats(k,h):
    
    h.sort(key =lambda x:x[0])
    #Creating heap of journey end time i.e when th epassengers get down
    end_soon = [h[0][1]]
    #for calculating additional capacity
    if k == 0:
        additional_cap = 1
    else:
        additional_cap = 0
    #iterating over the heap starting from one sing 0 already in heap
    for i in range(1,len(h)):
        end_early = end_soon[0]
        #comparing the start time of next passenger and end time of the previous passenger and if start time greater than
        #previous end time the coming passenger can use same seat else new seat.
        if h[i][0] >= end_early:
            heapq.heapreplace(end_soon,h[i][1])
        else:
            heapq.heappush(end_soon,h[i][1])
            #additional capacituy calculations
            if len(end_soon) <= k:
                additional_cap = 0
            else:
                additional_cap += 1       
    return additional_cap