using System;

namespace AdventOfCode2017
{
  class Day1
  {
    public static int NextDigit(int currentIndex, int sequenceLength)
    {
      if (currentIndex == sequenceLength - 1)
      {
        return 0;
      }

      return currentIndex + 1;
    }

    public static int HalfwayAroundDigit(int currentIndex, int sequenceLength)
    {
      int nextIndex = currentIndex + sequenceLength / 2;

      if (nextIndex >= sequenceLength)
      {
        nextIndex -= sequenceLength;
      }

      return nextIndex;
    }

    public static long Captcha(string sequence, Func<int, int, int> nextIndexCalculator)
    {
      long sum = 0;

      for (int i = 0; i < sequence.Length; i++)
      {
        int nextIndex = nextIndexCalculator(i, sequence.Length);

        if (sequence[i] == sequence[nextIndex])
        {
          sum += (int)Char.GetNumericValue(sequence[i]);
        }
      }

      return sum;
    }

    public static long Part1(string sequence)
    {
      return Captcha(sequence, NextDigit);
    }

    public static long Part2(string sequence)
    {
      return Captcha(sequence, HalfwayAroundDigit);
    }

    public static void Main(string[] args)
    {
      CheckAnswer(Part1, "1122", 3);
      CheckAnswer(Part1, "1111", 4);
      CheckAnswer(Part1, "1234", 0);
      CheckAnswer(Part1, "91212129", 9);

      CheckAnswer(Part2, "1212", 6);
      CheckAnswer(Part2, "1221", 0);
      CheckAnswer(Part2, "123425", 4);
      CheckAnswer(Part2, "123123", 12);
      CheckAnswer(Part2, "12131415", 4);

      string captcha = System.IO.File.ReadAllText("../../Day1.txt");
      Console.WriteLine($"Part 1 solution: {Part1(captcha)}");
      Console.WriteLine($"Part 2 solution: {Part2(captcha)}");

      Console.ReadKey();
    }

    private static void CheckAnswer(Func<string, long> captchaAlgorithm, string sequence, long expectedAnswer)
    {
      long actualAnswer = captchaAlgorithm(sequence);

      if (actualAnswer == expectedAnswer)
      {
        Console.WriteLine($"Sequence {sequence} success!");
      }
      else
      {
        Console.WriteLine($"Sequence {sequence} FAILED. Expected {expectedAnswer} but got {actualAnswer}.");
      }
    }
  }
}
