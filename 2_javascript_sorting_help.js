/**********************************************************************
Write a recursive function called 'shortestToLongest' which takes an
array of lowercase strings and returns them sorted from shortest to
longest.

Strings of equal length should be sorted alphabetically.

(Hint: str1 < str2 will return true if str1 comes before str2
alphabetically)

Your function should accept a default argument called 'sorted' which
holds the currently sorted elements. Each recursive step should add
the shortest string in the 'strings' array to the end of 'sorted'.


**********************************************************************/

// 1. Find the shortest string in the 'strings' array
// 2. Remove the shortest string from the 'strings' array
// 3. Push the shortest string to the back of the 'sorted' array
// 4. Recurse until the 'strings' array is empty (base case)
function shortestToLongest(strings, sorted) {
    // Ensure we don't have an undefined sorted array
    if (sorted === undefined) sorted = [];

    var shortest;

    // Establish the base case: no elements in strings
    if (strings.length == 0) {
        return sorted;
    }

    // We have elements in strings, so let's find the shortest element
    for (i = 0; i < strings.length; i++) {
        // Initialize shortest to the first element
        if (i == 0) {
            shortest = strings[i];
        }
        // If strings[i] is shorter in length than shortest, we have a
        // new shortest
        else if (shortest.length > strings[i].length) {
            shortest = strings[i];
        }
        // If strings[i] is the same length as shortest, check to see
        // which comes first alphabetically
        else if (shortest > strings[i]) {
            shortest = strings[i];
        }
    }

    // The shortest element should be in shortest, so let's remove it
    // from strings, and add it to the end of sorted
    strings.splice(strings.indexOf(shortest),1);
    sorted.push(shortest);

    // To see recursive steps
    //console.log(sorted);

    return shortestToLongest(strings,sorted);
}

// Sorts the strings from shortest to longest
let strings1 = ["abc", "de", "", "f", "ghijk", "lmno"]
console.log(shortestToLongest(strings1));
// ['', 'f', 'de', 'abc', 'lmno', 'ghijk']

// Accepts a pre-sorted default parameter
let strings2 = ["pomegranate", "persimmon", "peach"];
let sorted = ["pea", "pear"];
console.log(shortestToLongest(strings2, sorted));
// ['pea', 'pear', 'peach', 'persimmon', 'pomegranate']

// Sorts strings of the same length alphabetically
let strings3 = ["dog", "cat", "elephant", "ant", "pig", "emu"];
console.log(shortestToLongest(strings3));
// ['ant', 'cat', 'dog', 'emu', 'pig', 'elephant']