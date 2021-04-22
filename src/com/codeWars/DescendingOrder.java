package com.codeWars;

// Your task is to make a function that can take any non-negative integer as an argument
// and return it with its digits in descending order. Essentially, rearrange the digits
// to create the highest possible number.

import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.Collections;
import java.util.stream.IntStream;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class DescendingOrder {

  public int sortDesc(final int num) {
    // Return 0 or single digits
    if (num < 0 || num == 0) return 0;
    if (num % 10 == num) return num;

    int[] digits = String.valueOf(num).chars().map(digit -> digit - 48).toArray();
    Integer[] numbers = Arrays.stream(digits).boxed().toArray(Integer[]::new);
    Arrays.sort(numbers, Collections.reverseOrder());
    String newNumber = "";
    for (Integer digit : numbers) {
//      System.out.println(digit);
      newNumber = newNumber.concat(digit.toString());
    }
    return Integer.parseInt(newNumber);
  }

  @Test
  public void test1() {
    assertEquals(0, this.sortDesc(0));
  }

  @Test
  public void test2() {
    assertEquals(7, this.sortDesc(7));
  }

  @Test
  public void test3() {
    assertEquals(51, this.sortDesc(15));
  }


  @Test
  public void test4() {
    assertEquals(987654321, this.sortDesc(123456789));
  }
}
