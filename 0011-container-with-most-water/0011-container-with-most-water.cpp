class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0,j = height.size()-1;
        int max_area = 0, min_height, distance, area;
        while(i<j){
            min_height = min(height[i],height[j]);
            distance = j - i;
            area = min_height * distance;
            max_area = max(max_area, area);
            if(height[i] < height[j])
                i+=1;
            else
                j-=1;
        }
        return max_area;
    }
};