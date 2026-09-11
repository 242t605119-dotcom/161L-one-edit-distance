# LeetCode 161 - One Edit Distance

## Problem

Given two strings `s` and `t`, return `true` if they are **one edit distance** apart.

An edit can be one of the following:

* Insert one character
* Delete one character
* Replace one character

The goal is to determine whether exactly one such edit is required to convert one string into the other.

---

## Examples

### Example 1

**Input:**

```text
s = "ab"
t = "acb"
```

**Output:**

```text
true
```

**Explanation:**

Insert `'c'` into `"ab"` to get `"acb"`.

---

### Example 2

**Input:**

```text
s = "cab"
t = "ad"
```

**Output:**

```text
false
```

**Explanation:**

More than one edit is required to convert one string into the other.

---

### Example 3

**Input:**

```text
s = "1203"
t = "1213"
```

**Output:**

```text
true
```

**Explanation:**

Replace `'0'` with `'1'`.

---

## Approach

The first thing to check is the difference in the lengths of the two strings.

### Case 1: Length difference is greater than 1

If the lengths differ by more than 1, the strings cannot be one edit distance apart.

For example:

```text
s = "abc"
t = "abcdef"
```

There are too many characters to add or remove with only one operation.

So we return `false`.

---

### Case 2: Strings have the same length

If both strings have the same length, the only possible operation is **replacement**.

We compare the characters at the same positions.

If there is exactly **one different character**, the strings are one edit distance apart.

Example:

```text
s = "abc"
t = "adc"
```

Comparison:

```text
a = a
b != d
c = c
```

There is exactly one difference, so the answer is `true`.

If there are zero differences, the strings are equal, which means they are **zero edits apart**, so the answer is `false`.

If there are more than one difference, the answer is also `false`.

---

### Case 3: Lengths differ by exactly 1

If one string is longer than the other by one character, the possible operation is **insertion/deletion**.

We can use two pointers to compare the strings.

When the characters are equal, move both pointers.

When the characters are different, move the pointer only in the longer string.

Only one such mismatch is allowed.

Example:

```text
s = "ab"
t = "acb"
```

At the mismatch:

```text
a = a
b != c
```

We move the pointer in the longer string:

```text
b = b
```

Only one insertion is needed, so the answer is `true`.

---

## Algorithm

1. Find the lengths of `s` and `t`.
2. If their length difference is greater than `1`, return `false`.
3. If `s` is longer, swap the strings so that `s` is the shorter string.
4. If both strings have the same length:

   * Compare characters one by one.
   * Count the number of differences.
   * Return `true` only when there is exactly one difference.
5. If the lengths differ by one:

   * Compare both strings using two pointers.
   * Allow only one mismatch.
   * Skip one character from the longer string when a mismatch occurs.
6. Return whether the strings are exactly one edit apart.

---

## Time Complexity

**O(n)**

Where `n` is the length of the shorter string.

We may need to compare every character once.

---

## Space Complexity

**O(1)**

Only a few variables and pointers are used. No extra data structure proportional to the input size is required.

---

## Key Concepts

* String manipulation
* Two pointers
* Character comparison
* Insert, delete, and replace operations
* Length difference
* Linear traversal

---

## Important Edge Cases

### Equal strings

```text
s = "abc"
t = "abc"
```

Output:

```text
false
```

Because zero edits are required.

### One character difference

```text
s = "abc"
t = "adc"
```

Output:

```text
true
```

One replacement is required.

### One character insertion

```text
s = "abc"
t = "abdc"
```

Output:

```text
true
```

One insertion is required.

### One character deletion

```text
s = "abcd"
t = "acd"
```

Output:

```text
true
```

One deletion is required.

### More than one edit

```text
s = "abc"
t = "axy"
```

Output:

```text
false
```

More than one character needs to be changed.

---

## What I Learned

This problem helped me understand how to compare two strings efficiently instead of trying every possible edit.

The important part is first checking the **length difference** and then deciding whether the required operation can be an insertion, deletion, or replacement.

I also practiced the **two-pointer technique**, which is useful for many string and array problems.

---

## LeetCode Details

* **Problem Number:** 161
* **Problem Name:** One Edit Distance
* **Difficulty:** Medium
* **Topic:** Strings
* **Language:** Python

---

## Author

T.Nandhini
