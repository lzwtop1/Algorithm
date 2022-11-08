n=int(input())
arr=input("")
num=[int(n) for n in arr.split()]
res=[]

m=len(num)
num.sort()
int_index=0


vector<int> reArrange(vector<int> data) {
    int len = data.size();
    vector<int> result(len);
    sort(data.begin(), data.end());
    int index = 0;
    result[index++] = data[len/2];
    int left = 0, right = len - 1;
    int flag = true;
    while (index < len) {
        if (flag) {
            result[index++] = data[left++];
        } else {
            result[index++] = data[right--];
        }
        flag = !flag;
    }
    return result;
}