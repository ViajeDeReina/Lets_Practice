//
//  Quiz1978.c
//  CodingTest
//
//  Created by Yeahwon Do on 14/07/2020
/*
#include <stdio.h>

int main()
{
    int i,j, n, ttl;
    int *nums;
    
    scanf("%d",&n);
    nums = (int *)malloc(n*sizeof(int));
    ttl = n;
    
    for (i=0; i<n; i++)
    {
        scanf("%d", &nums[i]);
    }
    
    for (i=0; i<n; i++)
    {
        j=2;
        if (nums[i]==1)
        {
            ttl -=1;
        }
        while (j<nums[i])
        {
            if (nums[i]==2){break;}
            else if (nums[i]%j ==0)
            {
                ttl -=1;
                break;
            }
            j +=1;
        }
    }
    printf("%d", ttl);
    //free(nums); << I don't understand why it doesn't work :(
    return 0;
}
*/
