package com.codeWars;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

// A pangram is a sentence that contains every single letter of the alphabet at least once.
// For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
// because it uses the letters A-Z at least once (case is irrelevant).
//
// Given a string, detect whether or not it is a pangram. Return True if it is, False if not.
// Ignore numbers and punctuation.

public class DetectPangram {
  public boolean check(String sentence) {
    String lowerCaseSentence = sentence.toLowerCase();
    String[] alphabet = "abcdefghijklmnopqrstuvwxyz".split("");
    for (String letter : alphabet) {
      if (!lowerCaseSentence.contains(letter)) return false;
    }
    return true;
  }

// // Other solutions

//  public boolean check(String sentence){
//    return sentence.chars().map(Character::toLowerCase).filter(Character::isAlphabetic).distinct().count() == 26;
//  }

//  public boolean check(String sentence){
//    for (char c = 'a'; c<='z'; c++)
//      if (!sentence.toLowerCase().contains("" + c))
//        return false;
//    return true;
//
//  }

  @Test
  public void test1() {
    String pangram1 = "The quick brown fox jumps over the lazy dog.";
    Assertions.assertTrue(this.check(pangram1));
  }

  @Test
  public void test2() {
    String pangram2 = "You shall not pass!";
    Assertions.assertFalse(this.check(pangram2));
  }
}
