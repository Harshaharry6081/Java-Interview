# Stream API

## Common-Step-Stream-API-Coding-Level-I
GenZ Career on YouTube
Subscribe for Interview Preparation
Java Most Asked Stream API Coding Questions
1. Filter Even Numbers
Problem:  Given a list of integers, return a list containing only even numbers.
Solution:
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6);
List<Integer> evenNumbers = numbers.stream()
.filter(n -> n % 2 == 0)
.collect(Collectors.toList());
Explanation:  The filter  method is used to apply a condition that keeps only even numbers.
The collect  method gathers the results into a new list.
2. Find Maximum
Problem:  Find the maximum value in a list of integers.
Solution:
Optional<Integer> max = numbers.stream()
.max(Integer::compare);
Explanation:  The max method takes a comparator and returns the maximum element
wrapped in an Optional .
3. Sum of Elements
Problem:  Calculate the sum of elements in a list of integers.
Solution:
int sum = numbers.stream()
.mapToInt(Integer::intValue)
.sum();
Explanation:  mapToInt  converts the stream to an IntStream , which provides the sum
method to get the total.
4. List of Names to Uppercase
Problem:  Convert all strings in a list to uppercase.
Solution:
List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
GenZ Career on YouTube
Subscribe for Interview Preparation
List<String> upperNames = names.stream()
.map(String::toUpperCase)
.collect(Collectors.toList());
Explanation:  The map function applies String::toUpperCase  to each element,
transforming them to uppercase.
5. Sort List
Problem:  Sort a list of integers in ascending order.
Solution:
List<Integer> sortedNumbers = numbers.stream()
.sorted()
.collect(Collectors.toList());
Explanation:  The sorted  method sorts the elements of the stream in natural order.
6. Count Elements
Problem:  Count the number of elements in a list that are greater than 5.
Solution:
long count = numbers.stream()
.filter(n -> n > 5)
.count();
Explanation:  The filter  method removes elements that don't satisfy the condition, and
count  returns the number of elements remaining.
7. Get Distinct Elements
Problem:  Get a list of distinct elements from a list of integers.
Solution:
List<Integer> distinctNumbers = numbers.stream()
.distinct()
.collect(Collectors.toList());
Explanation:  The distinct  method filters the stream to include only unique elements.
8. Reduce to Sum
Problem:  Reduce a list of integers to their sum.
Solution:
int total = numbers.stream()
.reduce(0, Integer::sum);
GenZ Career on YouTube
Subscribe for Interview Preparation
Explanation:  The reduce  method takes an identity (0 in this case) and an accumulator
function ( Integer::sum ) to calculate the total.
9. Find Any
Problem:  Return any element from a list of integers.
Solution:
Optional<Integer> anyElement = numbers.stream()
.findAny();
Explanation:  findAny  potentially returns any element from the stream, wrapped in an
Optional .
10. List First Names
Problem:  Extract first names from a list of full names.
Solution:
List<String> fullNames = Arrays.asList("Alice Johnson", "Bob Harris",
"Charlie Lou");
List<String> firstNames = fullNames.stream()
.map(name -> name.split(" ")[0])
.collect(Collectors.toList());
Explanation:  The map function splits each name string and selects the first part.
11. All Match
Problem:  Check if all numbers in a list are positive.
Solution:
boolean allPositive = numbers.stream()
.allMatch(n -> n > 0);
Explanation:  allMatch  returns true  if every element in the stream matches the given
predicate.
12. None Match
Problem:  Check if there are no negative numbers in a list.
Solution:
boolean noneNegative = numbers.stream()
.noneMatch(n -> n < 0);
Explanation:  noneMatch  checks that no elements match the negative condition.
GenZ Career on YouTube
Subscribe for Interview Preparation
13. Find First
Problem:  Find the first element in a list of integers.
Solution:
Optional<Integer> first = numbers.stream()
.findFirst();
Explanation:  findFirst  returns the first element of the stream, wrapped in an Optional .
14. FlatMap for Nested Lists
Problem:  Flatten a nested list structure.
Solution:
List<List<Integer>> nestedNumbers = Arrays.asList(Arrays.asList(1, 2),
Arrays.asList(3, 4, 5));
List<Integer> flatList = nestedNumbers.stream()
.flatMap(List::stream)
.collect(Collectors.toList());
Explanation:  flatMap  converts each element into its own stream and then merges them into
a single stream.
15. Grouping Elements
Problem:  Group users by age.
Solution:
Map<Integer, List<User>> usersByAge = users.stream()
.collect(Collectors.groupingBy(User::getAge));
Explanation:  The groupingBy  collector groups elements based on the age property, creating
a map where each key is an age and each value is a list of users with that age.
16. Peek Elements
Problem:  Print elements of a stream during processing without altering the stream.
Solution:
List<Integer> peekedAtNumbers = numbers.stream()
.peek(System.out::println)
.collect(Collectors.toList());
Explanation:  peek  is used for debugging or performing actions without changing the stream.
It prints each element before passing it along the stream.
GenZ Career on YouTube
Subscribe for Interview Preparation
17. Limit Stream
Problem:  Limit the output to the first 3 elements of the list.
Solution:
List<Integer> limited = numbers.stream()
.limit(3)
.collect(Collectors.toList());
Explanation:  limit  truncates the stream to be no longer than the specified size.
18. Skip Elements
Problem:  Skip the first 2 elements of a list and return the rest.
Solution:
List<Integer> skipped = numbers.stream()
.skip(2)
.collect(Collectors.toList());
Explanation:  skip  discards the first n elements of the stream.
19. Convert to Set
Problem:  Convert a list of integers to a set to remove duplicates.
Solution:
Set<Integer> uniqueNumbers = numbers.stream()
.collect(Collectors.toSet());
Explanation:  Collecting the stream into a Set automatically removes duplicates.
20. Summarizing Statistics
Problem:  Get summary statistics for a list of integers.
Solution:
IntSummaryStatistics stats = numbers.stream()
.mapToInt(Integer::intValue)
.summaryStatistics();
Explanation:  summaryStatistics  provides a summary (max, min, average, sum, count) for
a stream of integers.
## Common-Step-Stream-API-Coding-Level-II
GenZ Career on YouTube
Subscribe for Interview Preparation
1) Given a list of integers, find out all the even numbers that exist in the list using Stream
functions?
import java.util.*;
import java.util.stream.*;

```java
public class EvenNumber{
public static void main(String args[]) {
List<Integer> list = Arrays.asList(10,15,8,49,25,98,32);
```

list.stream()
.filter(n -> n%2 == 0)
.forEach(System.out::println);
/* or can also try below method */
Map<Boolean, List<Integer>> list = A rrays.stream(nums).boxed()
.collect(Collectors.partitioningBy(num -> num % 2 == 0));
System.out.println(list);

```java
}
}
```

Output:
10, 8, 98, 32
2) Given a list of integers, find out all the numbers starting with 1 using Stream functions?
import java.util.*;
import java.util.stream.*;

```java
public class NumberStartingWithOne{
public static void main(String args[]) {
List<Integer> myList = Arrays.asList(10,15,8,49,25,98,32);
```

myList.stream()
.map(s -> s + "") // Convert integer to String
.filter(s -> s.startsWith("1"))
.forEach(System.out::println);
/* or can also try below method */
List<String> list = Arrays.stream(arr).boxed()
.map(s -> s + "")
.filter(s -> s.startsWith("1"))
.collect(Collectors.toList());
System.out.println(list);

```java
}
```

GenZ Career on YouTube
Subscribe for Interview Preparation

```java
}
```

Output:
10, 15
3) How to find duplicate elements in a given integers list in java using Stream functions?
import java.util.*;
import java.util.stream.*;

```java
public class DuplicateElements {
public static void main(String args[]) {
List<Integer> myList = Arrays.asList(10,15,8,49,25,98,98,32,15);
Set<Integer> set = new HashSet();
```

myList.stream()
.filter(n -> !set.add(n))
.forEach(System.out::println);

```java
}
}
```

Output:
98, 15
// Or you can also try using distinct() keyword

```java
public static void getDataWithoutDuplicates() {
```

List<Integer> myList = Arra ys.asList(1, 1, 85, 6, 2, 3, 65, 6, 45, 45, 5662, 2582, 2, 2, 266,
666, 656);
myList.stream().distinct().forEach(noDuplicateData ->
System.out.println(noDuplicateData));

```java
}
```

Output : 1 85 6 2 3 65 45 5662 2582 266 666 656
//Or you can also use below

```java
public static void getDataWithoutDuplicates() {
```

List<Integer> myList = Arrays.asList(1, 1, 85, 6, 2, 3, 65, 6, 45, 45, 5662, 2582, 2, 2, 266,
666, 656);
Set<Integer> set = new HashSet<>(myList);
// Convert the set back to a l ist if needed
GenZ Career on YouTube
Subscribe for Interview Preparation
List<Integer> uniqueData = set.stream().collect(Collectors.toList());
// Print the unique elements
uniqueData.forEach(System.out::println);

```java
}
```

Output : 1 65 2 3 6 266 45 656 85 2582 666 5662
/* or can also try below single line code */
List<Integer> list = Arrays.stream(arr).boxed().distinct().collect(Collectors.toList());
4) Given the list of integers, find the first element of the list using Stream functions?
import java.util.*;
import java.util.stream.*;

```java
public class FindFirstElement{
public static void main(String args[]) {
List<Integer> myList = Arrays.asList(10,15,8,49,25,98,98,32,15);
```

myList.stream()
.findFirst()
.ifPresent(System.out::println);
/* or can also try below single line code */
Arrays.stream(arr).boxed().findFirst().ifPresent(System.out::print);

```java
}
}
```

Output:
10
5) Given a list of integers, find the total number of elements present in the list using Stream
functions?
import java.util.*;
import java.util.stream.*;

```java
public class FindTheTotalNumberOfElements{
public static void main(String args[]) {
List<Integer> myList = Arrays.asList(10,15,8,49,25,98,98,32,15);
```

long count =  myList.stream()
.count();
System.out.println(count);
/* or can also try below line code */
Arrays.stream(arr).boxed().count();

```java
}
}
```

GenZ Career on YouTube
Subscribe for Interview Preparation
Output:
9
6) Given a list of integers, find the maximum value element present in it using Stream functions?
import java.util.*;
import java.util.stream.*;

```java
public class FindMaxElement{
public static void main(String args[]) {
List<Integer> myList = Arrays.asList(10,15,8,49,25,98,98,32,15);
```

int max =  myList.stream()
.max(Integer::compare)
.get();
System.out.println(max);
/* or we can try using below way */
int maxdata = Arrays.stream(arr).boxed()
.max(Comparator.naturalOrder()).get();
System.out.println(maxdata);

```java
}
}
```

Output:
98
7) Given a String, find the first non -repeated character in it using Stream functions?
import java.util.*;
import java.util.stream.*;
import java.util.function.Function;

```java
public class FirstNonRepeated{
public static void main(String args[]) {
String input = "Java articles are Awesome";
```

Character result = input.chars() // Strea m of String
.mapToObj(s -> Character.toLowerCase(Character.valueOf((char) s))) // First convert to
Character object and then to lowercase
.collect(Collectors.groupingBy(Function.identity(), LinkedHashMap::new,
Collec tors.counting())) //Store the chars in map with count
.entrySet()
.stream()
.filter(entry -> entry.getValue() == 1L)
.map(entry -> entry.getKey())
GenZ Career on YouTube
Subscribe for Interview Preparation
.findFirst()
.get();
System.out.println(result);
/* or can also try using */
input.chars().mapToObj(c -> (char) c)
.filter(ch -> input.indexOf(ch) == input.lastIndexOf(ch))
.findFirst ().orElse(null);

```java
}
}
```

Output:
j
8) Given a String, find the first repeated character in it using Stream functions?
import java.util.*;
import java.util.stream.*;
import java.util.function.Function;

```java
public class FirstRepeated{
public static void main(String args[]) {
String input = "Java Articles are Awesome";
```

Character result = input.chars() // Stream of String
.mapToObj(s -> Character.toLowerCase(Character.valueOf((char) s))) //
First convert to Character object and then to lowercase
.collect(Collectors.groupingB y(Function.identity(), LinkedHashMap::new,
Collectors.counting())) //Store the chars in map with count
.entrySet()
.stream()
.filter(entry -> entry.getVa lue() > 1L)
.map(entry -> entry.getKey())
.findFirst()
.get();
System.out.println(result);
/* or can also try */
Set<Character > seenCharacters = new HashSet<>();
return input.chars()
.mapToObj(c -> (char) c)
.filter(c -> !seenCharacters.add(c))
.findFirst()
.orElse(null);
GenZ Career on YouTube
Subscribe for Interview Preparation

```java
}
}
```

Output:
a
9) Given a list of integers, sort all the values present in it using Stream functions?
import java.util.*;
import java.util.stream.*;
import java.util.function.Function;

```java
public class SortValues{
public static void main(String args[]) {
List<Integer> myList = Arrays.asList(10,15,8,49,25,98,98,32,15);
```

myList.stream()
.sorted()
.forEach(System.out::println);
/* Or can also try below w ay */
Arrays.stream(arr).boxed().sorted().collect(Collectors.toList())

```java
}
}
```

Output:
8
10
15
15
25
32
49
98
98
10) Given a list of integers, sort all the values present in it in descending order using Stream
functions?
import java.util.*;
import java.util.stream.*;
import java.util.function.Function;

```java
public class SortDescending{
public static void main(String args[]) {
List<Integer> myList = Arrays.asList(10,15,8,49,25,98,98,32,15);
```

GenZ Career on YouTube
Subscribe for Interview Preparation
myList.stream()
.sorted(Collections.reverseOrder())
.forEach(System.out::println);

```java
}
}
```

Output:
98
98
49
32
25
15
15
10
8
11) Given an integer array  nums, return  true  if any value appears  at least twice  in the array, and
return  false  if every element is distinct.

```java
public boolean containsDuplicate(int[] nums) {
```

List<Integer> list = Arrays.stream(nums)
.boxed()
.collect(Collectors.toList());
Set<Integer> set = new HashSet<>(list);

```java
if(set.size()  == list.size()) {
return false;
}
return true;
```

/* or can also try below way */
Set<Integer> setData = new HashSet<>();
return Arrays.stream(nums)
.anyMatch(num -> !setData.add(num));

```java
}
```

Input: nums = [ 1,2,3,1]
Output: true
Input: nums = [1,2,3,4]
Output: false
12) How will you get the current date and time using Java 8 Date and Time API?

```java
class Java8 {
public static void main(String[] args) {
System.out.println("Current Local Date: " + java.time.LocalDate.now());
```

GenZ Career on YouTube
Subscribe for Interview Preparation
//Used LocalDate API to get the date
System.out.println("Current Local Time: " + java.time.LocalTime.now());
//Used LocalTime API to get the time
System.out.println("Current Local Date and Time: " + java.time.LocalDateTime.n ow());
//Used LocalDateTime API to get both date and time

```java
}
}
```

13) Write a Java 8 program to concatenate two Streams?
import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

```java
public class Java8 {
public static void main(String[] args) {
List<String> list1 = Arrays.asList("Java", "8");
List<String> list2 = Arrays.asList("expla ined", "through", "programs");
Stream<String> concatStream = Stream.concat(list1.stream(), list2.stream());
// Concatenated the list1 and list2 by converting them into Stream
concatStream.forEach(str -> System.out.prin t(str + " "));
// Printed the Concatenated Stream
}
}
```

14) Java 8 program to perform cube on list elements and filter numbers greater than 50.
import java.util.*;

```java
public class Main {
public static void main(String[] args) {
List<Integer> integerList = Arrays.asList(4,5,6,7,1,2,3);
```

integerList.stream()
.map(i -> i*i*i)
.filter(i -> i>50)
.forEach(System.out::println);

```java
}
}
```

Output:
64
125
GenZ Career on YouTube
Subscribe for Interview Preparation
216
343
15) Write a Java 8 program to sort an array and then convert the sorted array into Stream?
import java.util.Arrays;

```java
public class Java8 {
public static void main(String[] args) {
int arr[] = { 99, 55, 203, 99, 4, 91 };
Arrays.parallelSort(arr);
// Sorted the Array using parallelSort()
Arrays.strea m(arr).forEach(n > System.out.print(n + " "));
```

/* Converted it into Stream and then
printed using forEach */

```java
}
}
```

16) How to use map to convert object into Uppercase in Java 8?

```java
public class Java8 {
public static void main(String[] args) {
```

List<String> nameLst = names.stream()
.map(String::toUpperCase)
.collect(Collectors.toList());
Syste m.out.println(nameLst);

```java
}
}
```

output:
AA, BB, CC, DD
17) How to convert a List of objects into a Map by considering duplicated keys and store them in
sorted order?

```java
public class TestNotes {
public static void main(String[] args) {
List<Notes> noteLst = new ArrayList<>();
noteLst.add(new Notes(1, "note1", 11));
noteLst.add(new Notes(2, "note2", 22));
noteLst.add(new Notes(3, "note3", 33));
noteLst.add(new Notes(4, "note4", 44));
noteLst.add(new Notes(5, "note5", 55));
```

GenZ Career on YouTube
Subscribe for Interview Preparation
noteLst.add(new Notes(6, "note4", 66));
Map<String, Long> notesRecords = noteLst.stream()
.sorted(Comparator
.comparingLong(Notes::getTagId)
.reversed()) // sorting is based on TagId 55,44,33,22,11
.collect(Collectors.toMap
(Notes::getTagName, Notes::getTagId,
(oldValue, newValue) -> oldValue,LinkedHashMap::new));
// consider old value 44 for dupilcate key
// it keeps order
System.out.println("Notes : " + notesRecords);

```java
}
}
```

18) How to count each element/word from the String ArrayList in Java8?

```java
public class TestNotes {
public static void main(String[] args) {
List<String> names = Arrays.asList("AA", "BB", "AA", "CC");
```

Map<String,Long> namesCount = names
.stream()
.collect(
Collectors.groupingBy(
Function.identity(), Collectors.counting()));
System.out.println(namesCount);

```java
}
}
```

Output:

```java
{CC=1, BB=1, AA=2}
```

19) How to find only duplicate elements with its count from the String ArrayList in Java8?

```java
public class TestNotes {
public static void main(String[] args)
List<String> names = Arrays.asList("AA", "BB", "AA", "CC");
```

Map<String,Long> namesCount = names
.stream()
.filter(x ->Collections.frequency(names, x)>1)
.collect(Collectors.groupingBy
(Function.identity(), Collectors.counting()));
System.out.println(namesCount);
/*or you can also try using  */
GenZ Career on YouTube
Subscribe for Interview Preparation
Map<String, Long> namesCount = names.stream()
.collect(Collectors.groupingBy(Function.identity(), Collectors.counting()))
.entrySet()
.stream()
.filter(entry -> entry.getValue() > 1)
.collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));

```java
}
}
```

Output:

```java
{AA=2}
```

20) How to check if list is empty in Java 8 using Optional, if not null iterate through the list and
print the object?
Optional.ofNullable(noteLst)
.orElseGet(Collections::emptyList) // creates empty immutable list: [] in case noteLst is
null
.stream().filter(Objects::nonNull) //loop throgh each object and consider non null
objects
.map( note -> Notes::getTagName) // method reference, consider only tag name
.forEach(System.out::println); // it will print tag names
21) Write a Program to find the Maximum element in an array?

```java
public static int findMaxElement(int[] arr) {
return Arrays.stream(arr).max().getAsInt();
}
```

Input: 12,19,20,88,00,9
output: 88
22) Write a program to print the count of each character in a String?

```java
public static void findCountOfChars(String s) {
```

Map<String, Long> map = Arrays.stream(s.split(""))
.map(String::toLowerCase)
.collect(Collectors
.groupingBy(str -> str,
LinkedHashMap::new, Collectors.counting()));
// or you can also try using Function.identify() instead of LinkedHashMap
Map<String, Long> mapObject = Arrays.stream(s.split(""))
.map(S tring::toLowerCase)
.collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
GenZ Career on YouTube
Subscribe for Interview Preparation

```java
}
Input: String s = "string data to count each character";
Output: {s=1, t=5, r=3, i=1, n=2, g=1,  =5, d=1, a=5, o=2, c=4, u=1, e=2, h=2}
```
