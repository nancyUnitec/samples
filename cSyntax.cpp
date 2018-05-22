

//the use of malloc

int** block = (int**)malloc(sizeof(int*));

//realloc
int** block = (int**)malloc(sizeof(int*));
void f(int ***block, int *lastSize)
{
	//both the left and the right side are *block
	*block = (int**)realloc(*block, sizeof(int*)*(*lastSize + 1));
	int **block_content = *block;
	//malloc space for the new space
	block_content[*lastSize] = (int*)malloc(arrSize*sizeof(int));
	
}

//memcopy  memcpy((int*), (int*), arrSize * sizeof(int));
memcpy(desc, sour, arrSize * sizeof(int));


//string s
//string to char*
const char* pchar = s.data();//strlen is for char* only

 //get length of the char* or string
if (strlen(pchar) <= 1) //for char*
int len = s.length();//for string

//get substring, from position left, length is wl
 S.substr(left, wl) //s is a string
 
//vector
vector<int> va;//调用默认构造函数，里面什么也没有
    for(int i=0;i<5;i++)
        va.push_back(i);//放5个元素进去
    vector<int> vb(va);//用va初始化vb，此种用法要求va与vb必须是同一种容器，且类型相同
    vector<int> vc{1,2,3,4};//初始化列表
    vector<int> vc2={1,2,3,4};//同上，C++11新标准
    vector<int> vd(va.begin(),va.end());//用迭代器指定的范围初始化

    vector<int> ve(10);//包含10初始化值的元素，在ve当中里面有10个0次构造函数是explicit
    vector<int>  vf(10,1);//在vf里面塞进10个1
	
	

//init vector with array
int arr1[] = {1, 2, 3};
vector<int> iv1(arr1, arr1 + 3);

list<int> li={2,3,4};
vector<int> vli(li.begin(),li.end())//使用迭代器可以把不同容器，类型相同的元素用来初始化

ios::sync_with_stdio(false);
vector<int> va,vb,vc;
va={1,2,3,4};//用C++11的初始化列表来赋值
swap(va,vc);//交换va和vc
for(auto x:vc)//输出应该是va里面的值
        cout<<x<<" ";

		
//check if the vector is empty:
if (intervals.empty())
	
//sort the vector
struct student{
      char name[10];
      int score;
};
vector<student> vectorStudents;

//待排序的首元素下标，末尾元素下标，比较函数指针
//if you want to use sort(),you have to #include<algorithm> at first
sort(vectorStudents.begin(), vectorStudents.end(), comp);
bool comp(const student &a, const student &b){
     return a.score < b.score;
}

//reverse the vector
vector<int> tmp;  
reverse(tmp.begin(), tmp.end());   //一句话实现vector反转  

//get the last element of the vector:
vector<Interval> res;
res.back()

//get the size of the vector:
intervals.size()

//map
unordered_map<string, int> dict;

//access the element which key = k
dict[k]

//find how many str in the dict
dict.count(str)


#include "stdafx.h"

#include <iostream>
#include <string>
using namespace std;

#include "forCPP.h"
#include "leetcode.h"

int testLeetCode()
{
	/*
	int arr[3] = { 1,1,2 };
	//int* nums = (int*)malloc(3 * sizeof(int));
	arr[0] = 1;
	arr[1] = 1;
	arr[2] = 2;
	removeDuplicates(arr, 3);
	*/

	/*
	char *s = "aaa";
	char *p = "a*a";

	bool res = isMatch(s, p);

	*/
	
	
	struct ListNode n1, n2, n3, n4;
	n1.val = 1; n1.next = &n2;
	n2.val = 2; n2.next = &n3;
	n3.val = 3; n3.next = &n4;
	n4.val = 4; n4.next = NULL;
	
	struct ListNode* res = swapPairs(&n1);

	return 0;
}

int removeDuplicates(int* nums, int numsSize)
{
	int i = 0;
	int count = 0;
	int position = 0;
	if (nums == NULL)
		count = 0;
	else if (numsSize == 0)
		count = 0;
	else
	{
		count = 1;
		while (position < numsSize)
		{
			while (nums[position] == nums[i])
			{
				position++;
			}

			if (position < numsSize)
			{
				nums[i + 1] = nums[position];
				count++;
				i++;
				//position++;
			}
		}
		//count = i+1;
	}




	return count;

}

bool match(char a, char b)
{
	return (a == b) || ((b == '.') && (a != '\0'));
}

bool isMatch(char* s, char* p) {
	bool res = false;
	bool temp = true;
	int i = 0;
	int j = 0;

	while ((s[i] != '\0') || (p[j] != '\0'))
	{
		printf("wwwww i = %d, j = %d \n", i, j);
		//printf(" s = %s, p = %s \n",s,p);
		printf("wwwww s[i]= %c, p[j] = %c \n", s[i], p[j]);
		printf("wwwww s+i= 0x%x, p+j = 0x%x \n", s + i, p + j);
		printf("wwwww *(s+i)= %c, *(p+j) = %c \n", *(s + i), *(p + j));

		temp = match(s[i], p[j]);
		if (temp)
		{
			i++;
			j++;
		}
		else
		{
			if (p[j] == '*')
			{
				if (match(s[i], p[j - 1]))
					i++;
				else
					j++;
			}

			else if (p[j + 1] == '*')
				j += 2;
			else
				break;
		}

	}


	printf(" i = %d, j = %d \n", i, j);
	printf(" s = %s, p = %s \n", s, p);
	printf(" s[i]= %c, p[j] = %c \n", s[i], p[j]);
	printf(" s+i= 0x%x, p+j = 0x%x \n", s + i, p + j);

	if (s[i] == '\0')
	{

		if ((p[j] == '\0')
			//||((p[j+1]=='*')&&(p[j+2]=='\0'))||
			|| (match(s[i - 1], p[j + 1]) && (p[j] == '*'))
			|| (match(s[i - 1], p[j]) && (p[j - 1] == '*'))
			)

			res = true;


	}

	return res;

}



/*
struct ListNode* swap(struct ListNode* n1,struct ListNode* n2)
{
struct ListNode* tmp = n2-> next;
n1->next = tmp;
n2->next = n1;

return n1;
}

*/

/*
struct ListNode* swapPairs(struct ListNode* head) {

if (!head)
return NULL;

else if (!(head->next))
return head;

else
{
//struct ListNode* new = (struct ListNode*)malloc(sizeof(struct ListNode));
//new ->next = head->next;
struct ListNode* new;
struct ListNode* tail;
//struct ListNode* tmp;

struct ListNode* i = head;
struct ListNode* j = head->next;
new = j;

while (i&&j)
{
//tail = swap(i,j);
//tmp = j-> next;
i->next = j->next;
j->next = i;
tail = i;

if (i->next)
{
i = i->next;
j = i->next;

if (j)
{
tail->next = j;
}

}
else
break;

}

return new;

}

}


*/

struct ListNode* swapPairs(struct ListNode* head) {

	if (!head)
		return NULL;

	else if (!(head->next))
		return head;

	else
	{
		struct ListNode* newHead = swapPairs(head->next->next);
		struct ListNode* tmp = head->next;
		head->next = newHead;
		tmp->next = head;
		return tmp;

	}

}

struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    
	// acceptted 1
    // if(head == NULL)
    //     return NULL;
    // else if(head->next == NULL)
    //     return NULL;
    
    // struct ListNode* first = head;
    // struct ListNode* second = head;
    // struct ListNode* prev;
    // int count = 0;
    // while(first)
    // {
    //     count++;
    //     first = first->next;
    // }
    // int pos = count - n;
    // int index = 0;
    
    // if(index < pos)
    // {
    //     while(index < pos)
    //     {
    //         prev = second;
    //         second = second->next;
    //         index++;
    //     }
    //     prev->next = second->next;

    // }
    // else
    // {
    //     head = head->next;
    // }
       
    // return head;


	// acceptted 2
	if(head == NULL)
        return NULL;
    else if(head->next == NULL)
        return NULL;
    
    struct ListNode* first = head;
    struct ListNode* second = head;
    struct ListNode* prev = head;
    int gap = 0;
    while(gap<n)
    {
        gap++;
        first = first->next;
    }
    //int pos = count - n;
    //int index = 0;
    
    while(first)
    {
        prev = second; 
        first = first->next;  //what you want is to link prev with prev->next-next, so the second is redundant.
        second = second->next;
    }    
    
    if(second == head)  //if you use a dummy node point to the head, u can omit this step.
        head = head->next;
    else 
        prev->next = second->next;

    return head;
}

