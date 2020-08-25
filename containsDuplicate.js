
// contains duplicate - leetcode
var containsDuplicate = function(nums) {
    numsToSet = new Set(nums)
    return numsToSet.size !== nums.length
};


// https://leetcode.com/problems/contains-duplicate/