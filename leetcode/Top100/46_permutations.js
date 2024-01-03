/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    var original = nums.slice();
    const len = nums.length;
    let result = [];

    if (len === 1) return [nums];

    for(var i = 0; i < len; i++ ) {
        for(var j = 0; j < len-1; j++){
            [original[j+1], original[j]] = [original[j], original[j+1]];
            if (!(nums in result)) result.push([...original]);
        }   
    };
    console.log(result);

    return result;
};